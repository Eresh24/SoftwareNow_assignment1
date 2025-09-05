import sys

def encrypt_text(text, shift1, shift2):
    """
    Encrypt text according to the specified rules:
    - Lowercase a-m: shift forward by shift1 * shift2
    - Lowercase n-z: shift backward by shift1 + shift2  
    - Uppercase A-M: shift backward by shift1
    - Uppercase N-Z: shift forward by shift2²
    - Other chars: unchanged
    """
    encrypted_text = ""
    
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':  # First half of lowercase
                shift = shift1 * shift2
                new_pos = (ord(char) - ord('a') + shift) % 26
                encrypted_text += chr(new_pos + ord('a'))
            else:  # Second half of lowercase (n-z)
                shift = shift1 + shift2
                new_pos = (ord(char) - ord('a') - shift) % 26
                encrypted_text += chr(new_pos + ord('a'))
                
        elif char.isupper():
            if 'A' <= char <= 'M':  # First half of uppercase
                shift = shift1
                new_pos = (ord(char) - ord('A') - shift) % 26
                encrypted_text += chr(new_pos + ord('A'))
            else:  # Second half of uppercase (N-Z)
                shift = shift2 * shift2  # shift2 squared
                new_pos = (ord(char) - ord('A') + shift) % 26
                encrypted_text += chr(new_pos + ord('A'))
                
        else:
            # Spaces, tabs, newlines, special characters, numbers unchanged
            encrypted_text += char
            
    return encrypted_text

def decrypt_text(text, shift1, shift2):
    """
    Decrypt text by reversing the encryption operations.
    We need to determine what the ORIGINAL character was, not what alphabet half 
    the encrypted character is in.
    """
    decrypted_text = ""
    
    for char in text:
        if char.islower():
            # Try both possible original positions to see which one makes sense
            char_pos = ord(char) - ord('a')
            
            # Test if original was in first half (a-m) - would have been shifted forward by shift1 * shift2
            shift_forward = shift1 * shift2
            possible_orig_pos1 = (char_pos - shift_forward) % 26
            
            # Test if original was in second half (n-z) - would have been shifted backward by shift1 + shift2
            shift_backward = shift1 + shift2
            possible_orig_pos2 = (char_pos + shift_backward) % 26
            
            # Determine which original position is correct based on alphabet half
            # First half: 0-12 (a-m), Second half: 13-25 (n-z)
            if possible_orig_pos1 <= 12:  # Original was a-m (first half)
                decrypted_text += chr(possible_orig_pos1 + ord('a'))
            else:  # Original was n-z (second half)
                decrypted_text += chr(possible_orig_pos2 + ord('a'))
                
        elif char.isupper():
            char_pos = ord(char) - ord('A')
            
            # Test if original was in first half (A-M) - would have been shifted backward by shift1
            shift_backward = shift1
            possible_orig_pos1 = (char_pos + shift_backward) % 26
            
            # Test if original was in second half (N-Z) - would have been shifted forward by shift2²
            shift_forward = shift2 * shift2
            possible_orig_pos2 = (char_pos - shift_forward) % 26
            
            # Determine which original position is correct based on alphabet half
            # First half: 0-12 (A-M), Second half: 13-25 (N-Z)
            if possible_orig_pos1 <= 12:  # Original was A-M (first half)
                decrypted_text += chr(possible_orig_pos1 + ord('A'))
            else:  # Original was N-Z (second half)
                decrypted_text += chr(possible_orig_pos2 + ord('A'))
                
        else:
            # Unchanged characters remain unchanged
            decrypted_text += char
            
    return decrypted_text

def verify_decryption(original_file, decrypted_file):
    """
    Compare original and decrypted files to verify decryption success
    """
    try:
        with open(original_file, "r", encoding="utf-8") as f1:
            original = f1.read()
        with open(decrypted_file, "r", encoding="utf-8") as f2:
            decrypted = f2.read()
            
        if original == decrypted:
            print("Decryption successful: Files match.")
            return True
        else:
            print("Decryption failed: Files do not match.")
            # Show first mismatch for debugging
            for i, (a, b) in enumerate(zip(original, decrypted)):
                if a != b:
                    print(f"First mismatch at position {i}: original='{a}', decrypted='{b}'")
                    break
            if len(original) != len(decrypted):
                print(f"Length difference: original={len(original)}, decrypted={len(decrypted)}")
            return False
            
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        return False
    except Exception as e:
        print(f"Error during verification: {e}")
        return False

def read_int(prompt):
    """Get integer input with error handling"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def read_text_file(filename):
    """Read text file with error handling"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
        sys.exit(1)

def write_text_file(filename, content):
    """Write text file with error handling"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"'{filename}' created successfully.")
    except Exception as e:
        print(f"Error writing '{filename}': {e}")
        sys.exit(1)

def main():
    print("Text Encryption/Decryption Program")
    print("-" * 40)
    
    # 1. Get user inputs
    shift1 = read_int("Enter shift1 value: ")
    shift2 = read_int("Enter shift2 value: ")
    
    # 2. Read original file
    print("\nReading 'raw_text.txt'...")
    raw_text = read_text_file("raw_text.txt")
    
    # 3. Encrypt and save
    print("Encrypting text...")
    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    write_text_file("encrypted_text.txt", encrypted_text)
    
    # 4. Decrypt and save
    print("Decrypting text...")
    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
    write_text_file("decrypted_text.txt", decrypted_text)
    
    # 5. Verify decryption
    print("\nVerifying decryption...")
    verify_decryption("raw_text.txt", "decrypted_text.txt")

if __name__ == "__main__":
    main()