import pandas as pd
import yfinance as yf
from src.basket_cointegration import BasketCointegrationEngine

def run_basket_arbitrage():
    # Example Sector Basket: Tech Majors (e.g., MSFT, AAPL, GOOGL)
    tickers = ["MSFT", "AAPL", "GOOGL"]
    print(f"--> Fetching market data for basket: {tickers}...")
    
    data = yf.download(tickers, start="2023-01-01", end="2026-01-01")["Close"]
    
    engine = BasketCointegrationEngine(data)
    results = engine.run_johansen_test()
    
    print("\n--- Johansen Cointegration Analysis ---")
    print(f"Cointegrating Relations Found (95% CI): {results['num_coint_relations']}")
    print("\nNormalized Basket Weights (Hedge Ratios):")
    for ticker, weight in results["weights"].items():
        print(f"  {ticker}: {weight:.4f}")
        
    spread = engine.calculate_basket_spread(results["weights"])
    print(f"\nLatest Basket Spread Value: {spread.iloc[-1]:.4f}")

if __name__ == "__main__":
    run_basket_arbitrage()
