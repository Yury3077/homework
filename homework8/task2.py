import sqlite3
from collections.abc import Iterator


def create_cursor(func: any):
    """Create a decorator in order to connect with DB and close in the ena of a session"""

    def wrapper(self, *args, **kwargs):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            return func(self, cursor, *args, **kwargs)
        finally:
            cursor.close()
            conn.close()

    return wrapper


class TableData:
    def __init__(self, db_name: str, table_name: str) -> None:
        """Init an instance of class with checking data before"""
        if TableData.__is_valid_table_name(db_name, table_name):
            self.table_name = table_name
            self.db_name = db_name

    @classmethod
    def __is_valid_table_name(cls, db_name: str, table_name: str) -> bool:
        """Validation of input data, return True if db name and table is correct"""
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
        data = cursor.fetchall()
        conn.close()
        for table in data:
            if table[1] == table_name:
                return True
        else:
            raise ValueError("Not find that table or DB")

    @create_cursor
    def __len__(self, cursor) -> int:
        """Measuring a length of set"""
        cursor.execute(f"SELECT * FROM {self.table_name}")
        data = cursor.fetchall()
        return len(data)

    @create_cursor
    def __getitem__(self, cursor, item: str) -> list:
        """Find item in the sequence"""
        cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        data = cursor.fetchall()
        return data

    @create_cursor
    def __contains__(self, cursor, item: str) -> bool:
        """Checking a value in a table"""
        cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        data = cursor.fetchall()
        if data:
            return True
        else:
            return False

    def __iter__(self) -> Iterator:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        return iter(cursor.execute(f"SELECT * from {self.table_name}"))
        conn.close()


if __name__ == "__main__":
    presidents = TableData("example.sqlite", "presidents")
    print(len(presidents))
    t = presidents["Yeltsin"]
    print(t)
    if "Yeltsin" in presidents:
        print("eeee")
    else:
        print("ffff")
    for i in presidents:
        print(i)
