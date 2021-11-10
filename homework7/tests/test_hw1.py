from homework7.hw1 import find_occurrences


def test_find_str_in_dict_tree():
    """Testing that function find str inside dict that can contains multiple nested structures"""
    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
        "set_some": ("RED", "1", None, 6, True, (1, "RED")),
    }
    assert find_occurrences(example_tree, "RED") == 8
