from homework3.task03.task03 import make_filter


def test_make_filter_function_return_filtered_list():
    """Testing than pool_handler faster then call function with one process"""
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    filtered_data = make_filter(name="polly", type="bird").apply(sample_data)
    assert filtered_data == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]
