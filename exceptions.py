class FileNotCreatedError(Exception):
    def __init__(self):
        super().__init__("This database file does not exist. Please set create_new_file to True next time.")

class KeyNotCreatedError(Exception):
    def __init__(self):
        super().__init__("You haven't registered a key for this database file. Please set create_new_key to True next time.")