def decrypt(message, key):
    decrypted_message = ""
    for char in message:
        if char.isalpha(): 
            shift = 65 if char.isupper() else 97 
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char 
    return decrypted_message

ciphertext = "o	WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"

for key in range(26):
    decrypted_text = decrypt(ciphertext, key)
    print(f"Key {key}: {decrypted_text}")
