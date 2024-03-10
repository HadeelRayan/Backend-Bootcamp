import assertion


def tests():
    assertion.assert_equal(5, 5)
    assertion.assert_equal(4, 6)
    assertion.assert_bigger(10, 5)
    assertion.assert_bigger(5, 10)
    assertion.assert_smaller(5, 7)
    assertion.assert_smaller(4, 1)
    assertion.assert_included_in_list(3, [1, 2, 3])
    assertion.assert_included_in_list(3, [5, 2, 2])
    assertion.assert_key_in_dic("name", {"name": "Hadeel", "age": 25})
    assertion.assert_key_in_dic("gender", {"name": "Hadeel", "age": 25})
    assertion.assert_included_in_dict(25, {"name": "Hadeel", "age": 25})
    assertion.assert_included_in_dict(30, {"name": "Hadeel", "age": 25})


def main():
    tests()


if __name__ == "__main__":
    main()
