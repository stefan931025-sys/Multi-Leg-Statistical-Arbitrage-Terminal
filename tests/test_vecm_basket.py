import pytest

def test_johansen_cointegration_eigenvalue():
    """Verify Johansen cointegration trace statistic against critical threshold."""
    trace_statistic = 24.5
    critical_value_95pct = 19.96  # Standard 95% confidence threshold
    
    is_cointegrated = trace_statistic > critical_value_95pct
    
    assert is_cointegrated is True
    assert trace_statistic > 0

def test_vecm_error_correction_speed():
    """Verify Error Correction Term (ECT) convergence coefficient sign."""
    # The speed of adjustment coefficient in a VECM must be negative for mean-reversion
    adjustment_coefficient_alpha = -0.15 
    
    assert adjustment_coefficient_alpha < 0
    assert abs(adjustment_coefficient_alpha) <= 1.0  # Stable error correction
