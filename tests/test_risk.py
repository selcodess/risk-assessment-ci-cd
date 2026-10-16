import pytest
from risk import assess_risk


@pytest.mark.parametrize("probability,impact,level", [
    (1, 1, "LOW"), (2, 4, "MEDIUM"), (3, 5, "HIGH"), (5, 5, "HIGH")
])
def test_levels(probability, impact, level):
    assert assess_risk(probability, impact)["level"] == level


def test_human_review_for_high_risk():
    assert assess_risk(4, 5)["human_review_required"] is True


@pytest.mark.parametrize("p,i", [(0, 4), (6, 1), (1, -1)])
def test_out_of_range(p, i):
    with pytest.raises(ValueError):
        assess_risk(p, i)


def test_non_integer():
    with pytest.raises(TypeError):
        assess_risk(2.5, 4)
