import pytest
from ai_engine import analyze_description


def test_security_example():
    result = analyze_description("unauthorized access to sensitive user information")
    assert result["category"] == "Data security"
    assert 0 <= result["similarity"] <= 1


def test_supply_chain_example():
    assert analyze_description("supplier cannot deliver materials on time")["category"] == "Supply chain"


def test_unknown_description():
    result = analyze_description("galactic banana nebula")
    assert result["category"] == "Uncertain"
    assert result["reference"] is None


def test_empty_description():
    with pytest.raises(ValueError):
        analyze_description("   ")
