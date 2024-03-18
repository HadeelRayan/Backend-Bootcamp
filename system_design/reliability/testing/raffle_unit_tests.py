import pytest
from raffle_system import Raffle


@pytest.fixture
def sample_raffle():
    raffle = Raffle(max_people=10, max_tickets=30, ticket_price=100)
    return raffle


def test_add_person(sample_raffle):
    sample_raffle.add_person("Hadeel")
    assert "Hadeel" in sample_raffle.participants, f"Function should return {True}, but returned {False}"
    assert "Zein" not in sample_raffle.participants, f"Function should return {False}, but returned {True}"
    assert sample_raffle.participants["Hadeel"] == 0


def test_buy_ticket(sample_raffle):
    sample_raffle.add_person("Hadeel")
    sample_raffle.buy_ticket("Hadeel", 5)
    assert sample_raffle.participants["Hadeel"] == 5
    assert sample_raffle.total_earnings == 500


def test_total_tickets_sold(sample_raffle):
    sample_raffle.add_person("Alice")
    sample_raffle.add_person("Bob")
    sample_raffle.buy_ticket("Alice", 3)
    sample_raffle.buy_ticket("Bob", 2)
    assert sample_raffle.total_tickets_sold() == 5
    assert int(sample_raffle.total_tickets_sold()) >= 0


def test_select_winner(sample_raffle):
    sample_raffle.add_person("Hadeel")
    sample_raffle.add_person("Zein")
    sample_raffle.buy_ticket("Hadeel", 1)
    sample_raffle.buy_ticket("Zein", 1)
    # Since it's random, we test it multiple times to increase confidence
    winners = [sample_raffle.select_winner() for _ in range(100)]
    assert "Hadeel" in winners and "Zein" in winners
    assert len(set(winners)) == 2
