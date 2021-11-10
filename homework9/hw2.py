"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
# ...    [][2]

"""
from contextlib import contextmanager


class ContextManager:
    """
    Context manager that ignoring exceptions

    """

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        print("Entering Context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")
        return isinstance(exc_value, self.exception)


@contextmanager
def ignoring_error(error_name):
    managed_resource = None
    try:
        yield managed_resource
    except error_name:
        print("caught:", error_name)
    finally:
        print("closed something")


if __name__ == "__main__":
    with ContextManager(IndexError):
        raise IndexError
