from caesar import is_en, process_letter, decrypt_caesar
def _process_letter(letter: str, shift: int):
    is_upper = letter == letter.upper()
    letter = letter.lower() if is_upper else letter
    letter = chr(ord(letter) + shift)
    letter = letter.upper() if is_upper else letter
    return letter



en_s = ord("a")
size = ord('z') - en_s + 1


def vinegret(letter, key, sign):
    return process_letter(letter, en_s, size, sign * (ord(key.lower()) - en_s)) if is_en(letter.lower()) else letter


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword = keyword*(1 + len(plaintext)//len(keyword))
   
    return ''.join([vinegret(plaintext[i], keyword[i], 1) for i in range(len(plaintext))])



    # PUT YOUR CODE HERE


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword = keyword*(1 + len(ciphertext)//len(keyword))
    return ''.join([vinegret(ciphertext[i], keyword[i], -1) for i in range(len(ciphertext))])
    # PUT YOUR CODE HERE
    return plaintext
