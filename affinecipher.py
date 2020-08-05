import sys
import cryptomath

SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" # 52

def main():
    message=""""Encryption works. Properly implemented strong crypto systems are one of the few things
that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can
frequently find ways around it." ― Edward Snowden"""
    key=267
    # mode='encrypt'

    ciphertext=encryptmessage(key, message)
    print("")
    print("Affine ciphertext:")
    print(ciphertext)
    print("")

    plaintext=decryptmessage(key,ciphertext)
    print("Affine plaintext:")
    print(plaintext)
    print("")
    
def getkeyparts(key):
    keyA=key//len(SYMBOLS)
    keyB=key%len(SYMBOLS)
    return (keyA, keyB)

def encryptmessage(key, message):
    keyA, keyB=getkeyparts(key)
    print(f"Affine key: {key}")
    print(f"Affine Key-a: {keyA}")
    print(f"Affine Key-b: {keyB}")
    modinversekeyA=cryptomath.findModInverse(keyA, len(SYMBOLS))
    print(f"Affine ModInverse Key-a: {modinversekeyA}")

    encryptedtext=''

    for letter in message:
        if letter in SYMBOLS:
            indexletter=SYMBOLS.find(letter)
            encryptedtext+=SYMBOLS[(indexletter*keyA+keyB) % len(SYMBOLS)]
        else:
            encryptedtext+=letter
    return encryptedtext

def decryptmessage(key, message):
    keyA, keyB=getkeyparts(key)
    modinversekeyA=cryptomath.findModInverse(keyA, len(SYMBOLS))

    decryptedtext=''

    for letter in message:
        if letter in SYMBOLS:
            indexletter=SYMBOLS.find(letter)
            decryptedtext+=SYMBOLS[(indexletter-keyB) * modinversekeyA % len(SYMBOLS)]
        else:
            decryptedtext+=letter
    return decryptedtext

if __name__ == "__main__":
    main()