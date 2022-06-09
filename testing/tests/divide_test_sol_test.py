import pytest
from divide_test_sol import sale_on_the_ticket
def test_addult_full_price():
    assert sale_on_the_ticket(30.0, 35) == 30.0


def test_young_half_price():
    assert sale_on_the_ticket(30.0, 16) == 15.0


def test_senior_for_third():
    assert sale_on_the_ticket(30.0, 70) == 10.0


def test_children_free():
    assert sale_on_the_ticket(30.0, 5) == 0.0


def test_youngster_at_18_for_half_price():
    assert sale_on_the_ticket(30.0, 18) == 15.0


def test_negative_age_raise_exception():
    with pytest.raises(ValueError):
        sale_on_the_ticket(30.0, -666)


def test_negative_price_throw_exception():
    with pytest.raises(ValueError):
        sale_on_the_ticket(-30.0, 12)


def test_seniors_for_free():
    assert sale_on_the_ticket(30.0, 100) == 0

