"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """
    Decorate class in order to count a number of reset_instances
    """

    class Decorated_cl(cls):
        cls.counter = 0

        def __new__(cls):
            instance_obj = super(cls, cls).__new__(cls)
            cls.counter += 1
            return instance_obj

        @classmethod
        def get_created_instances(cls):
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            reset_instence = cls.counter
            cls.counter = 0
            return reset_instence

    return Decorated_cl


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(user.get_created_instances())
