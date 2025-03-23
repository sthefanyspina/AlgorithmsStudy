#A hashing algorithm is a function that converts an input (or "message") into a fixed-size string of bytes. This string is typically a unique representation of the original data. Hashing is commonly used in various applications, such as data retrieval, encryption, and ensuring data integrity.
#The output of a hashing algorithm is called a hash or digest. Hashing is a one-way process, meaning you cannot convert the hash back to the original data.

#Popular Hashing Algorithms in Python:
#Python's hashlib module provides a variety of cryptographic hashing algorithms, including:
# 1 - MD5: (Message Digest Algorithm 5) — Produces a 128-bit hash, but it’s considered insecure due to vulnerabilities allowing for hash collisions (two different inputs generating the same hash). It’s generally not recommended for security-sensitive applications.
# 2 - SHA-1: (Secure Hash Algorithm 1) — Produces a 160-bit hash, but it’s also considered insecure due to vulnerabilities (collisions).
# 3 - SHA-256: Part of the SHA-2 family, it produces a 256-bit hash and is widely used in modern security applications (e.g., Bitcoin).
# 4 - SHA-512: Also part of the SHA-2 family, it produces a 512-bit hash, which is even more secure but results in a larger output size.
# 5 - Blake2: A faster alternative to MD5 and SHA-2, providing high security.
#Each of these hashing algorithms has a specific use case, but SHA-256 and SHA-512 are widely used because of their strength and security.

#Basic Example of Hashing in Python
#Here’s how you can use Python's hashlib module to hash data using different algorithms.

import hashlib

# Sample input data
data = "Hello, World!"

# MD5 hashing
md5_hash = hashlib.md5(data.encode()).hexdigest()
print(f"MD5: {md5_hash}")

# SHA-1 hashing
sha1_hash = hashlib.sha1(data.encode()).hexdigest()
print(f"SHA-1: {sha1_hash}")

# SHA-256 hashing
sha256_hash = hashlib.sha256(data.encode()).hexdigest()
print(f"SHA-256: {sha256_hash}")

# SHA-512 hashing
sha512_hash = hashlib.sha512(data.encode()).hexdigest()
print(f"SHA-512: {sha512_hash}")

#Explanation:
# 1 - hashlib: A built-in Python module used to perform secure hash and message digest algorithms.
# 2 - data.encode(): The hashlib methods require the input data to be in bytes. Since strings are Unicode in Python, we use encode() to convert the string into bytes.
# 3 - .hexdigest(): This converts the hash to a readable hexadecimal string.

Example Output:
MD5: fc3ff98e8c6a0d3087d515c0473f8677
SHA-1: 2ef7bde608ce5404e97d5f042f95f89f1c232871
SHA-256: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda2e0c6f57a6b0d8f5e3f
SHA-512: 861844d6704e8573fec34d967e20bcfe08d21b2c93a0a5e83c65a2e410d17d68

#Use Cases of Hashing:
# 1 - Data Integrity: Hashing is used to check if the data has been altered. For example, when you download a file, the website might provide a hash of the file. After you download it, you can compute the hash of your downloaded file and compare it to the provided hash to ensure it hasn't been corrupted or tampered with.
# 2 - Password Storage: Instead of storing actual passwords in databases, websites store a hash of the password. When a user logs in, the entered password is hashed and compared with the stored hash. This way, even if a hacker gains access to the database, they won’t be able to retrieve the original passwords.
# 3 - Data Structures: Hashing is used in data structures like hash tables or dictionaries to enable fast lookups.
# 4 - Digital Signatures: Hashing is also used in creating digital signatures, where the hash of a message is encrypted with a private key.

#Hashing in Data Structures (Example: Hash Table)
#A hash table is a data structure that stores key-value pairs. The key is hashed, and the resulting hash determines the index where the value is stored. It provides fast lookups and efficient data storage.

#Here's a basic example of how hashing might be used in a Python dictionary:

# Create a dictionary (hash table)
my_dict = {}

# Add key-value pairs
my_dict["name"] = "John"
my_dict["age"] = 30

# Access a value using the key
print(my_dict["name"])  # Output: John

# Check if a key exists
print("age" in my_dict)  # Output: True
#Internally, Python uses a hash function to store keys efficiently in the dictionary.
