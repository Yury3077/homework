"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
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


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Find amount of element in dict(tree)
    param:
        tree (dict): dict that have different structures inside: str, list, tuple, dict, set, int, bool
        element (any): value that we need to find in a dict
    return: the number of occurrences of this element in the tree
    """
    count = 0
    if isinstance(tree, dict):
        tree = tree.values()
    for item in tree:
        if item == element:
            count += 1
        if isinstance(item, dict):
            elem_tree = item.values()
            count += find_occurrences(elem_tree, element)
        if isinstance(item, list) or isinstance(item, set) or isinstance(item, tuple):
            count += find_occurrences(item, element)
    return count


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
