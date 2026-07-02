import hashlib

def hash_string(text):
    return hashlib.sha256(text.encode()).hexdigest()

def hash_file(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

choice = input("Hash (1) String or (2) File? ")

if choice == "1":
    text = input("Enter text: ")
    print("SHA-256:", hash_string(text))

elif choice == "2":
    filename = input("Enter filename: ")
    print("SHA-256:", hash_file(filename))