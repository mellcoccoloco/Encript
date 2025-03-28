import flet as ft
import pyperclip

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

def encrypt_morse(text):
    return ' '.join(MORSE_CODE.get(c.upper(), c) for c in text)

def decrypt_morse(text):
    reverse_morse = {v: k for k, v in MORSE_CODE.items()}
    return ''.join(reverse_morse.get(c, ' ') for c in text.split())

def encrypt_a1z26(text):
    return ' '.join(str(ord(c.upper()) - 64) if c.isalpha() else c for c in text)

def decrypt_a1z26(text):
    return ''.join(chr(int(c) + 64) if c.isdigit() else c for c in text.split())

def encrypt_reverse(text):
    return text[::-1]

def decrypt_reverse(text):
    return text[::-1]

ENCRYPTION_METHODS = {
    "Morse Code": (encrypt_morse, decrypt_morse),
    "A1Z26 (Numbers)": (encrypt_a1z26, decrypt_a1z26),
    "Reverse Cipher": (encrypt_reverse, decrypt_reverse)
}

def main(page: ft.Page):
    page.title = "Encryption Tool"
    page.theme_mode = "light"
    
    input_text = ft.TextField(label="Enter your message", width=400)
    dropdown = ft.Dropdown(
        label="Select encryption method",
        options=[ft.dropdown.Option(method) for method in ENCRYPTION_METHODS.keys()],
        width=400
    )
    output_text = ft.TextField(label="Output", read_only=True, width=400)
    
    def encrypt_message(e):
        if input_text.value and dropdown.value:
            encrypt_func, _ = ENCRYPTION_METHODS[dropdown.value]
            output_text.value = encrypt_func(input_text.value)
            page.update()
    
    def decrypt_message(e):
        if input_text.value and dropdown.value:
            _, decrypt_func = ENCRYPTION_METHODS[dropdown.value]
            output_text.value = decrypt_func(input_text.value)
            page.update()
    
    def copy_to_clipboard(e):
        pyperclip.copy(output_text.value)
    
    encrypt_btn = ft.ElevatedButton("Encrypt", on_click=encrypt_message)
    decrypt_btn = ft.ElevatedButton("Decrypt", on_click=decrypt_message)
    copy_btn = ft.ElevatedButton("Copy", on_click=copy_to_clipboard)
    
    page.add(input_text, dropdown, encrypt_btn, decrypt_btn, copy_btn, output_text)

ft.app(target=main)

