'''
Create a program that reads the text file "raw_text.txt", encrypts its contents using a
simple encryption method, and writes the encrypted text to a new file
"encrypted_text.txt". Then create a function to decrypt the content and a function to
verify the decryption was successful.
Requirements
The encryption should take two user inputs (shift1, shift2), and follow these rules:
• For lowercase letters:
o If the letter is in the first half of the alphabet (a-m): shift forward by shift1 *
shift2 positions
o If the letter is in the second half (n-z): shift backward by shift1 + shift2
positions
• For uppercase letters:
o If the letter is in the first half (A-M): shift backward by shift1 positions
o If the letter is in the second half (N-Z): shift forward by shift2² positions
(shift2 squared)
• Other characters:
o Spaces, tabs, newlines, special characters, and numbers remain
unchanged
Main Functions to Implement
Encryption function: Reads from "raw_text.txt" and writes encrypted content to
"encrypted_text.txt".

Decryption function: Reads from "encrypted_text.txt" and writes the decrypted
content to "decrypted_text.txt".
Verification function: Compares "raw_text.txt" with "decrypted_text.txt" and prints
whether the decryption was successful or not.
Program Behavior
When run, your program should automatically:
1. Prompt the user for shift1 and shift2 values
2. Encrypt the contents of "raw_text.txt"
3. Decrypt the encrypted file
4. Verify the decryption matches the original

'''


import os
import string

def encrypt_text(text, shift1, shift2):
    encrypted_text = ""
    for i, char in enumerate(text):
        if char.islower():
            shift = shift1 if i % 2 == 0 else shift2
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            shift = shift1 if i % 2 == 0 else shift2
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(text, shift1, shift2):
    decrypted_text = ""
    for i, char in enumerate(text):
        if char.islower():
            shift = shift1 if i % 2 == 0 else shift2
            decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif char.isupper():
            shift = shift1 if i % 2 == 0 else shift2
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def verify_decryption(original_file, decrypted_file):
    if not os.path.exists(original_file) or not os.path.exists(decrypted_file):
        print("Verification failed: One of the files does not exist.")
        return

    with open(original_file, "r") as f1, open(decrypted_file, "r") as f2:
        if f1.read() == f2.read():
            print("Decryption successful: Files match.")
        else:
            print("Decryption failed: Files do not match.")

def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    # Check if raw_text.txt exists
    if not os.path.exists("raw_text.txt"):
        print("Error: 'raw_text.txt' does not exist. Please create it first.")
        return

    # Read raw text
    with open("raw_text.txt", "r") as f:
        raw_text = f.read()

    # Encrypt and write to file (overwrite if exists)
    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)
    print("'encrypted_text.txt' created/overwritten.")

    # Decrypt and write to file (overwrite if exists)
    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted_text)
    print("'decrypted_text.txt' created/overwritten.")

    # Verify decryption
    verify_decryption("raw_text.txt", "decrypted_text.txt")

if __name__ == "__main__":
    main()

