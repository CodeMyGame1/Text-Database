### make it so that you don't decrypt the whole table, but, using hashes that link each row to the next, locate the row which has the info you trying to get

import os 
import dotenv
from TextDatabase import txtDBReader
from util import clear
from pathlib import Path

# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.fernet import Fernet

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def setup(filename, env_key):
    path = Path(__file__).parent
    path = path / f"{filename}"
    path.unlink(missing_ok = True)

    dotenv.unset_key(dotenv_file, env_key)

def unit_test():
    t = txtDBReader("data")
    # t["ello"] = "sus amigos"
    t.get()
    t.file_stream.close()

os.system("clear")

choice = input("Would you like to run the setup (1) or run the unit tests (2)?\n1 or 2: ")
if choice == "1":
    setup("data.txt", "PRIVATE_KEY_data")
elif choice == "2":
    unit_test()