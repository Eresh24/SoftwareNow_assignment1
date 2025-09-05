"""
HIT137 Assignment 2 - Question 1: File-based Shift Cipher

Requirements satisfied:
- Reads plain text from raw_text.txt
- Encrypts to encrypted_text.txt
- Decrypts to decrypted_text.txt
- Verifies decrypted_text.txt matches raw_text.txt byte-for-byte

Design note:
The cipher shifts letters within their 13-letter halves to keep the mapping bijective:
  Lowercase:
    - a–m: shift forward by shift1 * shift2, confined to [a..m]
    - n–z: shift backward by (shift1 + shift2), confined to [n..z]
  Uppercase:
    - A–M: shift backward by shift1, confined to [A..M]
    - N–Z: shift forward by (shift2 ** 2), confined to [N..Z]
Non-letters (spaces, punctuation, digits, tabs, newlines) are unchanged.
"""

import os
import sys

# Helpers for character tests

def is_first_half_lower(ch):
    return 'a' <= ch <= 'm'

def is_second_half_lower(ch):
    return 'n' <= ch <= 'z'

def is_first_half_upper(ch):
    return 'A' <= ch <= 'M'

def is_second_half_upper(ch):
    return 'N' <= ch <= 'Z'

# Shift helpers (confined to 13-letter half)

def _shift_within_half(base_ord, ch, delta):
    """
    Shift character ch within a 13-letter half [base_ord .. base_ord+12]
    by delta (can be any int, positive/negative). Wraps mod 13.
    """
    span = 13
    pos = ord(ch) - base_ord          # 0..12
    new_pos = (pos + (delta % span)) % span
    return chr(base_ord + new_pos)

# Build per-case encryption/decryption maps

def build_lowercase_map(shift1, shift2):
    """
    Lowercase rules:
      a–m: forward by (shift1 * shift2), stay within [a..m]
      n–z: backward by (shift1 + shift2), stay within [n..z]
    Returns (enc_map, dec_map).
    """
    enc = {}
    for code in range(ord('a'), ord('z') + 1):
        ch = chr(code)
        if is_first_half_lower(ch):
            delta = shift1 * shift2
            enc[ch] = _shift_within_half(ord('a'), ch, delta)
        else:
            delta = -(shift1 + shift2)
            enc[ch] = _shift_within_half(ord('n'), ch, delta)
    dec = {v: k for k, v in enc.items()}
    return enc, dec

def build_uppercase_map(shift1, shift2):
    """
    Uppercase rules:
      A–M: backward by shift1, stay within [A..M]
      N–Z: forward by (shift2**2), stay within [N..Z]
    Returns (enc_map, dec_map).
    """
    enc = {}
    for code in range(ord('A'), ord('Z') + 1):
        ch = chr(code)
        if is_first_half_upper(ch):
            delta = -shift1
            enc[ch] = _shift_within_half(ord('A'), ch, delta)
        else:
            delta = shift2 * shift2
            enc[ch] = _shift_within_half(ord('N'), ch, delta)
    dec = {v: k for k, v in enc.items()}
    return enc, dec

# Core operations

def encrypt_file(input_file, output_file, shift1, shift2):
    """
    Reads input_file, encrypts characters according to the rules,
    writes encrypted text to output_file.
    """
    try:
        lower_map, _ = build_lowercase_map(shift1, shift2)
        upper_map, _ = build_uppercase_map(shift1, shift2)

        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()

        out_chars = []
        for ch in text:
            if 'a' <= ch <= 'z':
                out_chars.append(lower_map[ch])
            elif 'A' <= ch <= 'Z':
                out_chars.append(upper_map[ch])
            else:
                out_chars.append(ch)  # keep non-letters unchanged

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("".join(out_chars))

        print(f"'{output_file}' created/overwritten.")
        return True

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"Error during encryption: {e}")
        return False

def decrypt_file(input_file, output_file, shift1, shift2):
    """
    Reads encrypted input_file, decrypts using inverse maps,
    writes plaintext to output_file.
    """
    try        :
        _, lower_dec = build_lowercase_map(shift1, shift2)
        _, upper_dec = build_uppercase_map(shift1, shift2)

        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()

        out_chars = []
        for ch in text:
            if 'a' <= ch <= 'z':
                out_chars.append(lower_dec[ch])
            elif 'A' <= ch <= 'Z':
                out_chars.append(upper_dec[ch])
            else:
                out_chars.append(ch)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("".join(out_chars))

        print(f"'{output_file}' created/overwritten.")
        return True

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
        return False
    except KeyError as e:
        print(f"Error: decryption map missing key {repr(e)}. Check maps.")
        return False
    except Exception as e:
        print(f"Error during decryption: {e}")
        return False

def verify_decryption(original_file, decrypted_file):
    """
    Compares original_file with decrypted_file and reports byte-for-byte equality.
    """
    try:
        with open(original_file, "r", encoding="utf-8") as f:
            a = f.read()
        with open(decrypted_file, "r", encoding="utf-8") as f:
            b = f.read()

        if a == b:
            print("Decryption successful: Files match perfectly!")
            return True

        print("Decryption failed: Files do not match.")
        print(f"Original length: {len(a)}")
        print(f"Decrypted length: {len(b)}")
        #Show first difference context
        show_first_diff(original_file, decrypted_file)
        return False

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error during verification: {e}")
        return False

def show_first_diff(a_path, b_path, context=24):
    """
    Prints the first differing index and a small context window.
    Helps diagnose any mismatch during testing.
    """
    try:
        with open(a_path, "r", encoding="utf-8") as fa, open(b_path, "r", encoding="utf-8") as fb:
            a = fa.read()
            b = fb.read()
        if a == b:
            print("No diff.")
            return
        i = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), None)
        if i is None:
            if len(a) != len(b):
                print(f"Lengths differ: {len(a)} vs {len(b)}")
            else:
                print("No diff found within min length; potential encoding issue.")
            return
        start = max(0, i - context)
        end = min(len(a), i + context)
        print(f"First difference at index {i}:")
        print("ORIG:", repr(a[start:end]))
        print("DECR:", repr(b[start:end]))
    except Exception as e:
        print(f"Error showing diff: {e}")

# I/O and driver

def get_shift_values():
    """
    Prompt user for integer shift values with validation.
    """
    while True:
        try:
            s1 = int(input("Enter shift1 value: "))
            s2 = int(input("Enter shift2 value: "))
            return s1, s2
        except ValueError:
            print("Please enter valid integers for shift values.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(0)

def main():
    """
    Main driver:
    - Checks raw_text.txt exists
    - Prompts for shift1, shift2
    - Encrypts -> encrypted_text.txt
    - Decrypts -> decrypted_text.txt
    - Verifies equality with original
    """
    print("HIT137 SoftwareNow Assignment 2 - Question 1: File-based Shift Cipher")

    src = "raw_text.txt"
    enc = "encrypted_text.txt"
    dec = "decrypted_text.txt"

    if not os.path.exists(src):
        print("Error: 'raw_text.txt' file not found in current directory.")
        print("Create this file with some text content before running the program.")
        return

    shift1, shift2 = get_shift_values()
    print(f"Using shift1={shift1}, shift2={shift2}")

    if not encrypt_file(src, enc, shift1, shift2):
        return

    if not decrypt_file(enc, dec, shift1, shift2):
        return

    verify_decryption(src, dec)

    print("\nProgram completed.")
    print("Generated files:")
    print(f"- {enc}")
    print(f"- {dec}")

if __name__ == "__main__":
    main()
