from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# The following third-party library (pycryptodome) is allowed for this assignment

def decrypt_aes_cbc():
    # Read the binary files containing the encryption key, IV, and ciphertext
    with open("key.bin", "rb") as key_file:
        key = key_file.read() # Read the 256-bit encryption key
    
    with open("iv.bin", "rb") as iv_file:
        iv = iv_file.read() # Read the initialization vector (IV) for CBC mode
    
    with open("ciphertext.bin", "rb") as cipher_file:
        ciphertext = cipher_file.read() # Read the encrypted data
    
    # Create an AES cipher object with the given key and IV, using CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext and remove the padding to retrieve the original plaintext
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    # Write the decrypted plaintext to output file
    with open("paragraph.txt", "w", encoding="utf-8") as output_file:
        output_file.write(plaintext.decode('utf-8')) # Decode bytes to a UTF-8 string

# Run the decryption function when the script is executed
if __name__ == "__main__":
    decrypt_aes_cbc()
