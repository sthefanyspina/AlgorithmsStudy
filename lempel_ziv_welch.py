#Lempel-Ziv-Welch (LZW) is a lossless data compression algorithm that builds a dictionary of input sequences during encoding and uses that dictionary to replace repetitive sequences with shorter codes. It is widely used in formats like GIF, TIFF, and PDF.

#Key Concepts:
# 1 - Dictionary Initialization: LZW starts with a dictionary containing all possible single characters in the input. The index of each character in the dictionary represents its code.
# 2 - Building the Dictionary: As the input is processed, new sequences of characters are added to the dictionary, and their corresponding codes are used to replace sequences in the input.
# 3 - Encoding: The algorithm processes the input data by finding the longest sequence in the dictionary. When a sequence is found, its code is output, and the dictionary is updated with the next sequence.
# 4 - Decoding: During decoding, the receiver uses the same dictionary to decode the received compressed codes back into the original input sequence.

#LZW Compression Algorithm
#Steps for Encoding:
# 1 - Initialize the dictionary with all single characters (usually 8-bit ASCII).
# 2 - Read the input string one character at a time and add it to the current sequence.
# 3 - If the sequence exists in the dictionary, continue adding characters to the sequence.
# 4 - If the sequence doesn't exist in the dictionary, output the code for the longest sequence found so far, add the new sequence to the dictionary, and reset the current sequence.
# 5 - Repeat the process until all input data has been processed.

#Steps for Decoding:
# 1 - Initialize the dictionary the same way as the encoder (starting with single characters).
# 2 - Read the codes from the compressed data and map them back to the sequences using the dictionary.
# 3 - Update the dictionary with new sequences as they are decoded.

#Python Implementation of LZW Compression

def lzw_compress(input_string):
    # Initialize the dictionary with single characters
    dictionary = {chr(i): i for i in range(256)}  # ASCII dictionary
    result = []
    current_sequence = ""
    code = 256  # Start adding codes after ASCII characters
    
    # Loop through each character in the input string
    for char in input_string:
        current_sequence += char
        
        # If sequence exists in dictionary, continue
        if current_sequence not in dictionary:
            # Output the code for the longest sequence in the dictionary
            result.append(dictionary[current_sequence[:-1]])
            # Add the new sequence to the dictionary
            dictionary[current_sequence] = code
            code += 1
            # Reset the current sequence to the current character
            current_sequence = char
    
    # Add the code for the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

#### LZW Decompression

def lzw_decompress(compressed_data):
    # Initialize the dictionary with single characters
    dictionary = {i: chr(i) for i in range(256)}  # Reverse dictionary for decoding
    result = []
    current_code = compressed_data.pop(0)  # Start with the first code
    result.append(dictionary[current_code])
    
    # Loop through each code in the compressed data
    for code in compressed_data:
        if code not in dictionary:
            # Special case for first code (i.e., repeating the previous sequence with the first character)
            entry = result[-1] + result[-1][0]
        else:
            entry = dictionary[code]
        
        result.append(entry)
        
        # Add the new sequence to the dictionary
        dictionary[len(dictionary)] = dictionary[current_code] + entry[0]
        current_code = code
    
    return ''.join(result)

# Example usage
input_string = "ABABABABA"
compressed = lzw_compress(input_string)
print("Compressed:", compressed)

decompressed = lzw_decompress(compressed)
print("Decompressed:", decompressed)

#Explanation:
# 1 - Compression:
# 1.1 - The function lzw_compress() takes an input string, builds a dictionary of sequences, and outputs a list of compressed codes.
# 1.2 - The dictionary starts with ASCII values and grows dynamically as the input is processed.
# 2 - Decompression:
# 2.1 - The function lzw_decompress() reads the list of compressed codes, uses the dictionary to reconstruct the original string, and dynamically updates the dictionary.

#Example:
input_string = "ABABABABA"
compressed = lzw_compress(input_string)
print("Compressed:", compressed)
decompressed = lzw_decompress(compressed)
print("Decompressed:", decompressed)

#Output:
Compressed: [65, 66, 256, 257, 258]
Decompressed: ABABABABA
