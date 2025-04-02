#A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set. The key feature of a Bloom Filter is that it can tell if an element definitely is not in the set, but it may tell you that an element is in the set when it actually is not, due to potential false positives.

#Key Properties:
# 1 - False Positives: The Bloom Filter may incorrectly indicate that an element is in the set (false positive), but it will never incorrectly tell you an element is not in the set (no false negatives).
# 2 - Space Efficient: It uses less memory compared to traditional data structures like sets or lists for membership testing.

#How it Works:
#A Bloom Filter uses multiple hash functions to hash an element into multiple positions of a bit array. These positions are marked as "set" (1). When you want to test whether an element is in the set, you hash the element using the same hash functions, and check if all corresponding bits are set to 1. If any of the bits are 0, the element is definitely not in the set.

#Steps:
# 1 - Initialization: Create a bit array of a fixed size, initialized to 0.
# 2 - Add Operation: For each element to add, hash it with multiple hash functions and set the corresponding bit positions to 1.
# 3 - Test Operation: To test whether an element is in the set, hash the element with the same hash functions and check the corresponding bit positions:
# 3.1 - If all the bits are 1, the element may be in the set.
# 3.2 - If any of the bits are 0, the element is definitely not in the set.

#Python Example:
#Here’s an implementation of a simple Bloom Filter in Python using the hashlib module for hashing:

import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size  # Size of the bit array
        self.num_hashes = num_hashes  # Number of hash functions
        self.bit_array = [0] * self.size  # Initialize a bit array of 0s

    def _hash(self, item, i):
        """Generate a hash for the item and hash index `i`."""
        return int(hashlib.md5((str(i) + item).encode('utf-8')).hexdigest(), 16) % self.size

    def add(self, item):
        """Add an item to the Bloom Filter."""
        for i in range(self.num_hashes):
            hash_value = self._hash(item, i)
            self.bit_array[hash_value] = 1

    def contains(self, item):
        """Check if the item is in the Bloom Filter."""
        for i in range(self.num_hashes):
            hash_value = self._hash(item, i)
            if self.bit_array[hash_value] == 0:
                return False
        return True

# Example Usage
bloom = BloomFilter(500, 10)

# Add items to the Bloom Filter
bloom.add("apple")
bloom.add("banana")
bloom.add("cherry")

# Check if items are in the Bloom Filter
print(bloom.contains("apple"))   # True
print(bloom.contains("banana"))  # True
print(bloom.contains("grapes"))  # False (most likely)

#Explanation of the Code:
# 1 - Initialization:
# 1.1 - The BloomFilter class initializes with two main parameters: size (size of the bit array) and num_hashes (the number of hash functions used).
# 2 - Hash Function:
# 2.1 - The _hash function generates a hash value for the element by concatenating the index of the hash function (i) with the item itself. The result is passed through MD5 and then reduced modulo the size of the bit array.
# 3 - Adding an Element:
# 3.1 - When an element is added with the add method, we compute multiple hash values (one for each hash function) and mark the corresponding bit positions in the bit array as 1.
# 4 - Testing Membership:
# 4.1 - To check if an element exists in the Bloom Filter, the contains method computes hash values for the element and checks the corresponding bits in the bit array. If any bit is 0, the element is not in the set. If all bits are 1, it may be in the set (false positives possible).

#Limitations:
# 1 - False Positives: Due to the nature of the Bloom Filter, it can return false positives.
# 2 - No Deletion: It does not support removal of elements, since the bits corresponding to multiple elements may overlap.

#Use Cases:
# 1 - Database Query Optimization: Checking if a value exists in a database before querying it.
# 2 - Networking: To check whether a URL is part of a blocked set.
# 3 - Distributed Systems: Used in systems like Apache HBase, Apache Cassandra, or Google Bigtable for fast membership testing.
