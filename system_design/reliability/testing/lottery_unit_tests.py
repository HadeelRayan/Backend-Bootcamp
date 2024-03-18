# test_lottery.py
import pytest
import lottery_system as lot


def test_pick_one_name():
    names = ["Hadeel", "Zein", "Saleem"]
    # Test that the picked name is in the list
    assert lot.pick_one_name(names) in names


def test_pick_n_names_unique():
    names = ["Alice", "Hadeel", "Zein", "Saleem", "Eve"]
    n = 3
    # Test that the function returns a unique set of names
    picked_names = lot.pick_n_names(names, n)
    assert len(set(picked_names)) == n
    # Ensure all picked names are from the original list
    assert all(name in names for name in picked_names)


def test_pick_n_names_length():
    names = ["Alice","Hadeel", "Zein", "Saleem", "Eve"]
    n = 3
    # Test that the function returns exactly n names
    assert len(lot.pick_n_names(names, n)) == n


def test_pick_n_names_with_invalid_n():
    names = ["Alice", "Hadeel", "Zein"]
    n = 4
    # Test picking more names than in the list
    with pytest.raises(ValueError):
        lot.pick_n_names(names, n)
