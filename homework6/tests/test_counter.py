from homework6.counter import User


def test_count_number_of_instances():
    """Testing that method calculate amount of created instances"""
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_reset_amount_of_instance_in_class():
    """Testing that method reset amount of created instances"""
    User()
    User.reset_instances_counter()
    assert User.get_created_instances() == 0
