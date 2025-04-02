#RSA (Rivest-Shamir-Adleman) is one of the most widely used public-key cryptosystems for secure data transmission. It is an asymmetric encryption algorithm, meaning it uses two different keys: a public key for encryption and a private key for decryption.

#Key Steps in RSA Algorithm:
# 1 - Key Generation:
# 1.1 - Select two large prime numbers p and q.
# 1.2 - Compute n = p * q. n will be part of both the public and private keys.
# 1.3 - Compute the totient function φ(n) = (p-1) * (q-1).
# 1.4 - Select an integer e such that 1 < e < φ(n) and e is coprime to φ(n) (i.e., gcd(e, φ(n)) = 1).
# 1.5 - Compute d such that d * e ≡ 1 (mod φ(n)). d is the modular inverse of e modulo φ(n).
# 2 - Encryption:
# 2.1 - The public key consists of (n, e).
# 2.2 - To encrypt a message M, calculate the ciphertext C using the formula:C = M^e modn
# 3 - Decryption:
# 3.1 - The private key consists of (n, d).
# 3.2 - To decrypt a ciphertext C, calculate the original message M using the formula: M = C^d modn

#RSA in Python

import random
from sympy import isprime, mod_inverse

# Step 1: Key Generation
def generate_keys(bits=1024):
    # Generate two large prime numbers p and q
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    while p == q:
        q = generate_prime(bits)
    
    # Compute n = p * q
    n = p * q
    
    # Compute φ(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Choose public key e such that gcd(e, φ(n)) = 1
    e = choose_public_key(phi_n)
    
    # Compute private key d such that d * e ≡ 1 (mod φ(n))
    d = mod_inverse(e, phi_n)
    
    # Return public and private keys
    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

# Function to generate a prime number
def generate_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        if isprime(prime_candidate):
            return prime_candidate

# Function to choose public key e
def choose_public_key(phi_n):
    e = random.randrange(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    return e

# Function to calculate gcd (greatest common divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Step 2: Encryption
def encrypt(message, public_key):
    n, e = public_key
    # Convert the message to an integer
    message_int = int.from_bytes(message.encode(), 'big')
    # Encrypt the message using the formula C = M^e mod n
    ciphertext = pow(message_int, e, n)
    return ciphertext

# Step 3: Decryption
def decrypt(ciphertext, private_key):
    n, d = private_key
    # Decrypt the ciphertext using the formula M = C^d mod n
    decrypted_int = pow(ciphertext, d, n)
    # Convert the integer back to a string
    message = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode()
    return message

# Example usage
public_key, private_key = generate_keys(bits=512)  # 512 bits for demonstration (use larger size in practice)

message = "Hello, RSA!"
print(f"Original message: {message}")

# Encrypt the message
ciphertext = encrypt(message, public_key)
print(f"Encrypted ciphertext: {ciphertext}")

# Decrypt the message
decrypted_message = decrypt(ciphertext, private_key)
print(f"Decrypted message: {decrypted_message}")

#Breakdown of the Code:
# 1 - Key Generation (generate_keys):
# 1.1 - We generate two large prime numbers p and q.
# 1.2 - Compute n and φ(n).
# 1.3 - Choose a public exponent e and compute the corresponding private exponent d.
# 2 - Encryption (encrypt):
# 2.1 - Convert the plaintext message to an integer (because RSA operates on numbers).
# 2.2 - Apply the RSA encryption formula: C = M^e mod n.
# 3 - Decryption (decrypt):
# 3.1 - Apply the RSA decryption formula: M = C^d mod n.
# 3.2 - Convert the decrypted integer back to the original message.

#Notes:
#Security: In practice, RSA uses much larger keys (2048-bit, 3072-bit, etc.), but for demonstration purposes, we use 512 bits.
#Libraries: We use the sympy library for checking if a number is prime (isprime) and for computing the modular inverse (mod_inverse).
