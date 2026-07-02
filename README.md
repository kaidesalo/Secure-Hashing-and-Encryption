# Secure Hashing and Excryption Demo
This project demonstrates three basic cybersecurity concepts utilizing Python and OpenSSL:
- SHA-256 Hashing Generation
- Caesar Cipher Encryption and Decryption
- Digital Signature Creation and Verification

### Requirements
- Python 3.8 or later
- OpenSSL installed and available from the command line

To verify OpenSSL is installed: `openssl version`

### Runnning the Programs
#### Run the Python programs with:

`python hash_generator.py`

`python caesar_cipher.py`

#### Use OpenSSL to create and verify digital signatures:

`openssl dgst -sha256 -sign private.pem -out signature.bin message.txt`

`openssl dgst -sha256 -verify public.pem -signature signature.bin message.txt`

### Summary
This project demonstrates the basics of hashing, encryption, and digital signatures.
