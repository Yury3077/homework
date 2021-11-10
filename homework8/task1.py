class KeyValueStorage(dict):
    """
    Class for saving key and values from txt file
    Read file line by line and save data into dict
    and get beck if asked instance return value or use method as a key in the dict
    """

    def __init__(self, file_name: str):
        """
        Initial an instance and save data into a dict
            param:
                file_name: path to txt file
        """
        self.file_name = file_name
        with open(self.file_name, "r") as fl:
            for line in fl:
                str_line = line.strip()
                list_data = str_line.split("=")
                if list_data[0].isidentifier():
                    if list_data[1].isdigit():
                        self[list_data[0]] = int(list_data[1])
                    else:
                        self[list_data[0]] = list_data[1]
                else:
                    raise ValueError("Str in not appropriate for a key of the dict ")

    def __getattr__(self, item: str) -> str or int:
        return self[item]


if __name__ == "__main__":
    storage = KeyValueStorage("task1.txt")
    t = storage["last_name"]
    c = storage.song
    print(storage.__dict__)
    print(t)
    print(c)
