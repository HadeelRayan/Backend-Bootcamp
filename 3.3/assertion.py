
def assert_equal(tested_value, compare_value):
    if tested_value == compare_value:
        print("assert equal: Test Passed")
    else:
        print("assert equal: Test Failed: Expected", tested_value, "got", compare_value)


def assert_bigger(tested_value, compare_value):
    if tested_value > compare_value:
        print("assert bigger than: Test Passed")
    else:
        print("assert bigger than: Test Failed: Expected bigger than", tested_value)


def assert_smaller(tested_value, compare_value):
    if tested_value < compare_value:
        print("assert smaller than: Test Passed")
    else:
        print("assert smaller than: Test Failed: Expected smaller than", tested_value)


def assert_included_in_list(tested_value, list_to_check):
    if tested_value in list_to_check:
        print("assert included in list: Test Passed")
    else:
        print("assert included in list: Test Failed: value", tested_value, "not included in", list_to_check)


def assert_key_in_dic(tested_key, dict_to_check):
    if tested_key in dict_to_check.keys():
        print("assert key in dictionary: Test Passed")
    else:
        print("assert key in dictionary: Test Failed: key", tested_key, "not included in", dict_to_check)


def assert_included_in_dict(tested_value, dict_to_check):
    if tested_value in dict_to_check.values():
        print("assert included in dictionary: Test Passed")
    else:
        print("assert included in dictionary: Test Failed: value", tested_value, "not included in", dict_to_check)
