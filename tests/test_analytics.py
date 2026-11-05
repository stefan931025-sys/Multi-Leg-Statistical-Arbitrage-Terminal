import pytest
import numpy as np
import pandas as pd
from core.analytics import StatArbAnalyticsEngine

@pytest.fixture
def analytics_engine():
    return StatArbAnalyticsEngine(entry_threshold=2.0, exit_threshold=0.0)

@pytest.fixture
def synthetic_cointegrated_data():
    """Generates synthetic cointegrated prices: Asset Y = 1.5 * Asset X + noise"""
    np.random.seed(42)
    n_points = 500
    asset_x = np.cumsum(np.random.normal(0, 1, n_points)) + 100.0
    noise = np.random.normal(0, 0.5, n_points)
    asset_y = 1.5 * asset_x + 10.0 + noise
    
    df = pd.DataFrame({
        "Asset_Y": asset_y,
        "Asset_X": asset_x
    }, index=pd.date_range("2026-01-01", periods=n_points, freq="1min"))
    return df

def test_vectorized_spread_calculation(analytics_engine):
    """Verifies that matrix dot product produces correct spread across multiple assets."""
    prices = pd.DataFrame({
        "A": [10.0, 11.0, 12.0],
        "B": [5.0, 5.5, 6.0]
    })
    hedge_ratios = np.array([1.0, -2.0])
    
    spread = analytics_engine.calculate_vectorized_spread(prices, hedge_ratios)
    np.testing.assert_array_almost_equal(spread.values, np.array([0.0, 0.0, 0.0]))

def test_vectorized_spread_dimension_mismatch(analytics_engine):
    """Ensures a ValueError is raised when matrix dimensions don't align."""
    prices = pd.DataFrame({"A": [10, 11], "B": [5, 6]})
    invalid_hedge_ratios = np.array([1.0, -2.0, 0.5])
    
    with pytest.raises(ValueError, match="Dimensions of price matrix and hedge ratio array do not match"):
        analytics_engine.calculate_vectorized_spread(prices, invalid_hedge_ratios)

def test_compute_rolling_zscore_properties(analytics_engine):
    """Verifies mean-reverting z-score statistical properties over rolling window."""
    np.random.seed(42)
    spread = pd.Series(np.random.normal(0, 1, 200))
    
    z_score = analytics_engine.compute_rolling_zscore(spread, lookback_window=50)
    
    assert len(z_score) == len(spread)
    assert not z_score.isna().any()
    assert z_score.max() < 5.0
    assert z_score.min() > -5.0

def test_ols_hedge_ratio_accuracy(analytics_engine, synthetic_cointegrated_data):
    """Tests if OLS estimate recovers the true synthetic hedge ratio (1.5)."""
    asset_y = synthetic_cointegrated_data["Asset_Y"]
    asset_x = synthetic_cointegrated_data["Asset_X"]
    
    hedge_ratio, intercept = analytics_engine.estimate_two_leg_ols_hedge_ratio(asset_y, asset_x)
    
    assert pytest.approx(hedge_ratio, abs=0.05) == 1.5
    assert pytest.approx(intercept, abs=1.0) == 10.0

def test_johansen_eigen_vector_output_shape(analytics_engine, synthetic_cointegrated_data):
    """Verifies Johansen eigenvector decomposition outputs normalized vector of correct length."""
    vector = analytics_engine.compute_johansen_eigen_vector(synthetic_cointegrated_data)
    
    assert len(vector) == 2
    assert pytest.approx(vector[0]) == 1.0
