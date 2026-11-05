import numpy as np
import pandas as pd
from typing import Tuple, Dict, NamedTuple
from scipy.stats import linregress

class CointegrationResult(NamedTuple):
    is_cointegrated: bool
    trace_stat: float
    crit_value_95: float
    hedge_ratios: np.ndarray
    spread: pd.Series
    z_score: pd.Series

class StatArbAnalyticsEngine:
    """
    High-Throughput Vectorized Analytics Engine for Multi-Leg Statistical Arbitrage.
    Calculates Johansen Cointegration vectors, dynamic hedge ratios, and normalized z-scores.
    """
    def __init__(self, entry_threshold: float = 2.0, exit_threshold: float = 0.0):
        self.entry_threshold = entry_threshold
        self.exit_threshold = exit_threshold

    @staticmethod
    def calculate_vectorized_spread(prices: pd.DataFrame, hedge_ratios: np.ndarray) -> pd.Series:
        """
        Computes portfolio spread using matrix dot products to eliminate Python loop overhead.
        
        Spread = Sum(Price_i * HedgeRatio_i)
        """
        if prices.shape[1] != len(hedge_ratios):
            raise ValueError("Dimensions of price matrix and hedge ratio array do not match.")
        
        spread_values = np.dot(prices.values, hedge_ratios)
        return pd.Series(spread_values, index=prices.index, name="portfolio_spread")

    @staticmethod
    def compute_rolling_zscore(spread: pd.Series, lookback_window: int = 60) -> pd.Series:
        """
        Calculates rolling z-scores over a given lookback window using vectorized rolling operations.
        """
        rolling_mean = spread.rolling(window=lookback_window).mean()
        rolling_std = spread.rolling(window=lookback_window).std(ddof=0)
        
        rolling_std = rolling_std.replace(0, np.nan)
        z_score = (spread - rolling_mean) / rolling_std
        return z_score.fillna(0.0)

    def estimate_two_leg_ols_hedge_ratio(self, asset_y: pd.Series, asset_x: pd.Series) -> Tuple[float, float]:
        """
        Fast OLS estimation for 2-leg pairs trading using numpy linear algebra.
        Returns: (hedge_ratio, intercept)
        """
        x_mat = np.vstack([asset_x.values, np.ones(len(asset_x))]).T
        hedge_ratio, intercept = np.linalg.lstsq(x_mat, asset_y.values, rcond=None)[0]
        return float(hedge_ratio), float(intercept)

    def compute_johansen_eigen_vector(self, prices: pd.DataFrame) -> np.ndarray:
        """
        Estimates the dominant stationary cointegration vector via maximum likelihood matrix decomposition.
        """
        log_p = np.log(prices.values)
        delta_p = np.diff(log_p, axis=0)
        z_lag = log_p[:-1]
        
        cov_delta = np.cov(delta_p, rowvar=False)
        cov_z = np.cov(z_lag, rowvar=False)
        cov_cross = np.dot(delta_p.T, z_lag) / (len(delta_p) - 1)
        
        try:
            inv_cov_z = np.linalg.inv(cov_z)
            inv_cov_delta = np.linalg.inv(cov_delta)
            mat = np.dot(inv_cov_z, np.dot(cov_cross.T, np.dot(inv_cov_delta, cov_cross)))
            
            eigenvalues, eigenvectors = np.linalg.eig(mat)
            max_idx = np.argmax(eigenvalues)
            primary_vector = eigenvectors[:, max_idx].real
            
            return primary_vector / primary_vector[0]
        except np.linalg.LinAlgError:
            return np.ones(prices.shape[1]) / prices.shape[1]
