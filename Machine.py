import flet as ft
import pyperclip

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': '//', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def encrypt_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), char) for char in text)

def decrypt_morse(text):
    return ''.join(REVERSE_MORSE_CODE_DICT.get(char, char) for char in text.split())

def encrypt_a1z26(text):
    return ' '.join(str(ord(char.upper()) - 64) if char.isalpha() else char for char in text)

def decrypt_a1z26(text):
    return ''.join(chr(int(num) + 64) if num.isdigit() else num for num in text.split())

def encrypt_polar_cenit(text):
    swap_dict = str.maketrans("POLARECNIT", "CENITPOLAR")
    return text.translate(swap_dict)

def decrypt_polar_cenit(text):
    swap_dict = str.maketrans("CENITPOLAR", "POLARECNIT")
    return text.translate(swap_dict)

def main(page: ft.Page):
    page.title = "Text Encryption & Decryption"
    page.theme_mode = ft.ThemeMode.LIGHT

    input_text = ft.TextField(label="Enter text", width=400)
    output_text = ft.TextField(label="Result", width=400, read_only=True)
    
    encryption_methods = {
        "Morse Code": (encrypt_morse, decrypt_morse),
        "A1Z26 (Letters to Numbers)": (encrypt_a1z26, decrypt_a1z26),
        "Polar Cenit": (encrypt_polar_cenit, decrypt_polar_cenit)
    }
    
    dropdown = ft.Dropdown(
        label="Select Encryption Method",
        options=[ft.dropdown.Option(method) for method in encryption_methods.keys()]
    )

    def encrypt(e):
        if input_text.value and dropdown.value:
            output_text.value = encryption_methods[dropdown.value][0](input_text.value)
            page.update()
    
    def decrypt(e):
        if input_text.value and dropdown.value:
            output_text.value = encryption_methods[dropdown.value][1](input_text.value)
            page.update()
    
    def copy_to_clipboard(e):
        if output_text.value:
            pyperclip.copy(output_text.value)

    encrypt_btn = ft.ElevatedButton("Encrypt", on_click=encrypt)
    decrypt_btn = ft.ElevatedButton("Decrypt", on_click=decrypt)
    copy_btn = ft.ElevatedButton("Copy", on_click=copy_to_clipboard)
    
    page.add(
        input_text, dropdown, encrypt_btn, decrypt_btn, output_text, copy_btn
    )

ft.app(target=main)