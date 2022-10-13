import os
import dotenv
import base64
import ast
import time
from cryptography.fernet import Fernet
from exceptions import FileNotCreatedError, KeyNotCreatedError
from typing import Union
from pathlib import Path
import warnings

# def txtDBInterpreter(stmts):
#     pass

class txtDBReader():
    """
    A class that implements database interactions for text files
    """
    # def __init__(self, filename: str, create_new_file: bool = False, create_new_key: bool = False):
    def __init__(self, filename: str):
        """
        Checks that file and associated key exist

        If file does not exist, create the file if promped
        If key does not exist, create the key if prompted
        """
        self.filename = filename

        self.dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(self.dotenv_file)

        path = Path(__file__).parent
        path = path / f"{filename}.txt"
        self.path = path.resolve()
        if not path.exists():
            print("\033[33mFile not present. Creating file...\033[0m")
        self.file_stream = open(path, "a+")

        if f"PRIVATE_KEY_{filename}" not in os.environ:
            print("\033[33mKey not present for file. Creating key...\033[0m")
            dotenv.set_key(self.dotenv_file, f"PRIVATE_KEY_{filename}", Fernet.generate_key().decode('utf-8'))
            print("\033[33mThe key has been changed. Please restart your code to interact with the database.\033[0m")
        
        dotenv.load_dotenv(self.dotenv_file)
        
        self.file_stream.seek(0)
        if self.file_stream.read() == "":
            obj = {} # include any initial metadata you want
            self.file_stream.write(Fernet(os.environ[f"PRIVATE_KEY_{filename}"].encode('utf-8')).encrypt(str(obj).encode("utf-8")).decode("utf-8"))
            self.file_stream.seek(0)

    # def tokenize(self, sql_stmt):
    #     if sql_stmt = "SELECT"

    def __setitem__(self, key, val):
        self.file_stream.seek(0)
        obj = ast.literal_eval(Fernet(os.environ[f"PRIVATE_KEY_{self.filename}"]).decrypt(self.file_stream.read().encode("utf-8")).decode("utf-8"))
        
        if val == None:
            del obj[key] # Achieves D of CRUD
        else:
            obj[key] = val # Achieves C and U of CRUD

        self.file_stream.seek(0) 
        self.file_stream.truncate(0)
        self.file_stream.write(Fernet(os.environ[f"PRIVATE_KEY_{self.filename}"].encode('utf-8')).encrypt(str(obj).encode("utf-8")).decode("utf-8"))
 
    def __getitem__(self, args: str = None):
        if str == None:
            pass
        
        # str = self.tokenize(str)
        

        

    # def get(self, where: list = None):
    #     if self.file_stream.closed:
    #         self.file_stream = open(self.path, "a+")
    #     self.file_stream.seek(0)
    #     obj = Fernet(os.environ[f"PRIVATE_KEY_{self.filename}"]).decrypt(self.file_stream.read().encode("utf-8")).decode("utf-8")
    #     print(obj)
    #     # if where:
    #     #     if (type(where) == list) and (where != []):
    #     #         if where[0] == "*":
    #     #             pass
    #     #         else:
    #     #             pass
    #     #     else:
    #     #         raise TypeError("'where' argument has to be a non-empty list")
    #     self.file_stream.close()
    
    def update(self):
        pass

    def delete(self):
        pass

    # def __getitem__(self, params):
    #     pass