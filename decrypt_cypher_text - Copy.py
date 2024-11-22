def decrypt_cypher_text(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        ascii_value = ord(char)
        decrypted_ascii = ascii_value - key
        decrypted_ascii = decrypted_ascii % 256
        decrypted_char = chr(decrypted_ascii)
        decrypted_text += decrypted_char
    
    return decrypted_text

encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu"
key = 3

decrypted_text = decrypt_cypher_text(encrypted_text, key)
print(f"Decrypted text: {decrypted_text}")
