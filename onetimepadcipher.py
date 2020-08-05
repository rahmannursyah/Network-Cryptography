import secrets

SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" # 52

def generaterandomOTPkey(message):
    otpkey=''
    for letter in range(len(message)):
        otpkey+=secrets.choice(SYMBOLS)

    return otpkey

def main():
    message=""""Encryption works. Properly implemented strong crypto systems are one of the few things
that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can
frequently find ways around it." ― Edward Snowden"""
    key=generaterandomOTPkey(message)
    print("One Time Pad Key:")
    print(key)
    print("")

    print("One Time Pad ciphertext:")
    ciphertext=cipher(key, message)
    print(ciphertext)
    print("")

    print("One Time Pad plaintext:")
    plaintext=plain(key, ciphertext)
    print(plaintext)    

def cipher(key, message):
    return(encryptmessage(key, message))

def plain(key, ciphertext):
    return(decryptmessage(key, ciphertext))

def encryptmessage(key, message):
    encryptedtext=[]
    keyindex=0
    key=key

    for msg in message:
        index=SYMBOLS.find(msg)
        if index!=-1:
            index+=SYMBOLS.find(key[keyindex])
            index%=len(SYMBOLS)

            if msg.isupper():
                encryptedtext.append(SYMBOLS[index].upper())
            elif msg.islower():
                encryptedtext.append(SYMBOLS[index].lower())

            keyindex+=1
            # if keyindex==len(key):
            #     keyindex=0  

        else:
            encryptedtext.append(msg)
    return ''.join(encryptedtext)

def decryptmessage(key, ciphertext):
    decryptedtext=[]
    keyindex=0
    key=key

    for msg in ciphertext:
        index=SYMBOLS.find(msg)
        if index!=-1:
            index-=SYMBOLS.find(key[keyindex])
            index%=len(SYMBOLS)

            if msg.isupper():
                decryptedtext.append(SYMBOLS[index].upper())
            elif msg.islower():
                decryptedtext.append(SYMBOLS[index].lower())

            keyindex+=1
            # if keyindex==len(key):
            #     keyindex=0  

        else:
            decryptedtext.append(msg)
    return ''.join(decryptedtext)
if __name__ == "__main__":
    main()