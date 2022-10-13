# BULLETIN BOARD
- [ ] create [relational database](https://www.oracle.com/database/what-is-a-relational-database/)
- [ ] obfuscate code
- [ ] add functionality for changing key by decrypting with old key and then encrypting with new key (might be unsafe while the info is decrypted and in a runtime variable, then just do a one liner)
	- can't add environment variables through code, so might be a bit hard
- [ ] get RSA encryption for python (through cryptography.hazmat.primitives.asymmetric.rsa)
- [ ] loading bar for decrypting information (in green text)
- [ ] should I make everything use \_\_getitem\_\_ / \_\_setitem\_\_, or assign separate functions to each command? (Create, Read, Update, and Delete)
- [ ] handle all possible exceptions that may occur
	- [ ] user input
	- [ ] if database file is moved while script is running
- [ ] first convert to binary, and then encrypt
- [ ] make it so you can chain CRUD functions (like one return value will be obj that can be used by next function in chain, so to actually be usable by whoever's using the dependency, it has to be converted out of that obj format using dependency's or Python's functions)
- [ ] data.txt being created in Operation Caerus/Code, not in Operation Caerus/Code/Misc/Text Database (bc i'm running this code from the Operation Caerus/Code folder, so we need to implement the pathlib.Path thingy)
- [ ] probs remove the "create_new_file" and "create_new_key" args; we can just return a dictionary with the results of initializing the text database instance, just like in JS
- [ ] make it so that the key is derived from an image
- [ ] make unit test to delete data.txt and clear .env file

for other stuff:
- what if we made a currency system, using the RSA signing?
- what if we made a mock cryptocurrency using the RSA signing?
  - simplified version of mining (guessing hashes) to verify transactions and what not
- what if we made a REAL cryptocurrency? (might be a bit hard)

enter venv:
- source Text\ Database/bin/activate

exit venv:
- deactivate