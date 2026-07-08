def encrypt(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isuppper() else ord('a')
            result += chr((ord(ch) - start + shift) % 26 + start)
        else:
            result += ch
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(text, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(text, shift)
print("Decrypted:", decrypted)