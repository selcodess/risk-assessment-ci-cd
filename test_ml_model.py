import pytest
from ml_model import predict_category, train_model


def test_security_prediction():
    assert predict_category("customer password was stolen") == "Data security"


def test_supply_prediction():
    assert predict_category("supplier delivery is delayed") == "Supply chain"


def test_financial_prediction():
    assert predict_category("company expenses exceed the budget") == "Financial"


def test_model_reused():
    assert train_model() is train_model()


@pytest.mark.parametrize("invalid", ["", "   ", None, 123])
def test_invalid_input(invalid):
    with pytest.raises(ValueError):
        predict_category(invalid)
