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

import string

# To take the string fro raw_text.txt and to encrypt
def encrypt_funcion(text,shift1,shift2):
    encrypted_text = ""
    
    #to check each character in the text
    for i,char in enumerate(text):
        if char.islower():
            
            # to check if the index is even or odd and to shift the character and wrap around using modulo
            shift = shift1 if i  % 2 == 0 else shift2
            new_char = chr((ord(char)- ord('a') + shift) % 26 + ord('a'))
            encrypted_text += new_char
            
            # to check if the character is in the second half of the alphabet
        elif char.isupper():
            shift = shift1 if i  % 2 == 0 else shift2
            new_char = chr((ord(char)- ord('A') + shift) % 26 + ord('A'))
            encrypted_text += new_char
            
            # to check if the character is not an alphabet
        else:
            encrypted_text += char 
    return encrypted_text

# To take the string from encrypted_text.txt and to decrypt     
def decrypt_function(text,shift1,shift2):
    decrypted_text = ""
    
    #to check each character in the text
    for i,char in enumerate(text):
        if char.islower():
            
            # to check if the index is even or odd and to shift the character and wrap around using modulo
            shift = shift1 if i  % 2 == 0 else shift2
            new_char = chr((ord(char)- ord('a') - shift) % 26 + ord('a'))
            decrypted_text += new_char
            
            # to check if the character is in the second half of the alphabet
        elif char.isupper():
            shift = shift1 if i  % 2 == 0 else shift2
            new_char = chr((ord(char)- ord('A') - shift) % 26 + ord('A'))
            decrypted_text += new_char
            
            # to check if the character is not an alphabet
        else:
            decrypted_text += char 
    return decrypted_text
    
# To verify the decryption was successful
def verify_function(original,decrypted):
    with open(original,"r") as file1, open(decrypted,"r") as file2:
        original_text = file1.read()
        decrypted_text = file2.read()
        
        if original_text == decrypted_text:
            print("Decryption was successful!")
        else:
            print("Decryption failed. The texts do not match.")



def main():
    shift1 = int(input("Enter thre first shift value: "))
    shift2 = int(input("Enter the second shift value:"))
    with open("raw_text.txt","r") as file:
        raw_text = file.read()
    
    #to encrypt the raw_text and to write it to encrypted_text.txt
    encrypted_text = encrypt_funcion(raw_text,shift1,shift2)
    with open("encrypted_text.txt","w") as file:
        file.write(encrypted_text)
    
    #to decrypt the encrypted_text and to write it to decrypted_text.txt
    decrypted_text = decrypt_function(encrypted_text,shift1,shift2)
    with open("decrypted_text.txt","w") as file:
        file.write(decrypted_text)
        
    #to verify the decryption
    verify_function("raw_text.txt","decrypted_text.txt")
    
if __name__=="__main__":
    main()