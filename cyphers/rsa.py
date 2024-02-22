import random
from math import sqrt
import typing as tp


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """

    if 1 < n < 4:
        return True

    if n%2 == 0 or n == 1:
        return False

    for i in list(range(3, int(sqrt(n) + 1), 2)):
        if n % i == 0:
            return False
    return True
    


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    # PUT YOUR CODE HERE

    if b == 0:
        return a

    return(gcd(b,a%b))


def extended_euclid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclid(b % a, a)
        return (gcd, y - (b // a) * x, x)



def count_x_y(q,r,a,b):
    y = lambda i: 1 if r[i] == 0 else 0 if r[i-1] == 0 else (y(i+1), y(i+2) - y(i+1)*q[i])
    return(y(0), y(1))


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """

    a = e
    b = phi
    
    # inicializing arrays of rests and `div`s
    r = [0 for i in range(10000)]
    q = [0 for i in range(10000)]

    # start position to be able include `b` and `a` as r(-1) and r(0)
    N = 1
    r[N + (-1)] = b
    r[N + 0]  = a

    # COUNTING GCD

    n = N + 1

    q[n] = r[n-2]//r[n-1]
    r[n] = r[n-2] - r[n-1]*q[n]
    #print(f'{r[n-2]} = {r[n-1]}*{q[n]} + {r[n]}')
    while r[n] != 0:
        n+=1
        q[n] = r[n-2]//r[n-1]
        r[n] = r[n-2] - r[n-1]*q[n]
        #print(f'{r[n-2]} = {r[n-1]}*{q[n]} + {r[n]}')

    n+=1
    GCD = r[n-1]

    # Counting ax + by = GCD(a,b)

    x = [0 for i in range(n+1)]
    y = [0 for i in range(n+1)]
    y[n] = 1
    for i in range(n-1, 0, -1):
        y[i] = x[i+1] - y[i+1]*q[i-1]
        #print(f"{y[i]} = {x[i+1]} - {y[i+1]}*{q[i-1]}")
        x[i] = y[i+1]
        
    # Finding multiplicative inverse
    #print(f'{a}*{x[N + 1]} + {b}*{y[N + 1]} = {r[n-2]}')
    return(x[N + 1]%b)



def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = p*q
    # PUT YOUR CODE HERE

    phi = (p-1)*(q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))

