# String yg mau di encrypt
message="A"

# The encryption/decryption key
key=132

# Every possible symbol that can be encrypted
SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

def encryptedCaesar(message,key):
    translated=""
    for symbol in message:
        if symbol in SYMBOLS:
             symbolindex=SYMBOLS.find(symbol)
             translatedindex=(symbolindex+key) % 66
             translated=translated+SYMBOLS[translatedindex]    
        else:
            translated=translated+symbol
    return translated

def decryptCaesar(cipher,key):
    translated=""
    for symbol in cipher:
        if symbol in SYMBOLS:
             symbolindex=SYMBOLS.find(symbol)
             translatedindex=(symbolindex-key) % 66
             translated=translated+SYMBOLS[translatedindex]    
        else:
            translated=translated+symbol
    return translated

cipher=encryptedCaesar(message,key)
print(cipher)
plain=decryptCaesar(cipher,key)
print(plain)