import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen

class BasketCointegrationEngine:
    """Performs Johansen cointegration test on a multi-asset basket (3+ assets)."""
    
    def __init__(self, price_data: pd.DataFrame):
        self.price_data = price_data.dropna()

    def run_johansen_test(self, det_order: int = 0, k_ar_diff: int = 1) -> dict:
        """Runs the Johansen cointegration test to determine cointegrating vectors."""
        # Johansen test expects log prices
        log_prices = np.log(self.price_data)
        
        # Run Johansen Test (det_order: 0 = no deterministic trend, 1 = constant)
        res = coint_johansen(log_prices, det_order, k_ar_diff)
        
        # Extract Eigenvalues and Trace Statistics
        trace_stat = res.lr1
        trace_crit = res.cvt  # 90%, 95%, 99% confidence levels
        
        # Check for number of cointegrating vectors at 95% confidence (index 1)
        num_coint_vectors = np.sum(trace_stat > trace_crit[:, 1])
        
        # Extract the primary cointegrating vector (first eigenvector)
        hedge_ratios = res.evec[:, 0]
        # Normalize weights relative to the first asset
        normalized_weights = hedge_ratios / hedge_ratios[0]
        
        weights_dict = dict(zip(self.price_data.columns, normalized_weights))
        
        return {
            "num_coint_relations": num_coint_vectors,
            "weights": weights_dict,
            "eigenvalues": res.eig,
            "trace_stats": trace_stat
        }

    def calculate_basket_spread(self, weights: dict) -> pd.Series:
        """Calculates the stationary portfolio basket spread based on normalized weights."""
        log_prices = np.log(self.price_data)
        spread = pd.Series(0.0, index=log_prices.index)
        
        for col, weight in weights.items():
            spread += log_prices[col] * weight
            
        return spread
