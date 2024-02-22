import typing as tp

def process_letter(letter: str, start: int, diff: int, shift: int):
    is_upper = letter == letter.upper()
    letter = letter.lower() if is_upper else letter
    letter = caesarize(letter, start, diff, shift)
    letter = letter.upper() if is_upper else letter
    return letter



def caesarize(letter, start, diff, shift):
    """
    Encoding one symbol based on start and diff parameters

    start: alphabet start charcode
    diff : length of alphabet
    """
    return chr(start + (ord(letter) - start + shift) % diff)

def is_ru(letter):
    """
    Checking if symbol is cyrillic
    """

    ru_s, ru_e = ord('а'),ord('я')

    letter = letter.lower()
    return ru_s <= ord(letter) <= ru_e

def is_en(letter):
    """
    Checking if symbol is latin
    """

    en_s,en_e = ord('a'),ord('z')

    letter = letter.lower()
    return en_s <= ord(letter) <= en_e

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    """

    НЕАДЕКВАТНАЯ РЕАЛИЗАЦИЯ
    Eng Translatioin: NEADEKWANTNAYA REALIZATSIYA
    Chinese: 刺蝟不同意
    Indonesian: Hanya seorang siplusist yang berani menulis hal seperti itu

    ru_s, ru_e = ord('а'), ord('я')
    ru_size = ru_e - ru_s + 1 

    en_s, en_e = ord('a'), ord('z')
    en_size = en_e - en_s + 1 

    return ''.join(map(lambda letter: process_letter(letter, ru_s, ru_size, shift) if is_ru(letter) else ( process_letter(letter, en_s, en_size, shift) if is_en(letter) else letter), plaintext))

    """


    # ОЧЕНЬ ЧИТАЕМАЯ И ЭФФЕКТИВНАЯ ФУНКЦИЯ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    return ''.join([process_letter(letter, ord('а'), ord('я') - ord('a') + 1, shift) if  ord('а') <= ord(letter.lower()) <= ord('я') else process_letter(letter, ord('a'), ord('z') - ord('a') + 1, shift) if ord('a') <= ord(letter.lower()) <= ord('z') else letter for letter in plaintext])
    
def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    return encrypt_caesar(ciphertext, -shift)
    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """

    best_shift = 0
    array = [0]*33
    for i in range(34):
        for word in decrypt_caesar(ciphertext, i).split(' '):
            if word in dictionary:
                array[i] += 1
        if best_shift < array[i]:
            best_shift = array[i]

    # PUT YOUR CODE HERE
    return best_shift
