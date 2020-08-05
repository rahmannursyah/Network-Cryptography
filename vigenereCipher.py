# Vigenere Cipher (Polyalphabetic Substitution Cipher)

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    # myMessage = "Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf."
    # myMessage = "COMMONSENSEISNOTSOCOMMON"
    myMessage = """"Hhogjxgogq qagva. Cxgsydaj qzvdhgqcemq yluizv nzlvlr mkhemzy suy acp ws zzh zql epvtyv
ntpe gba udh dtwg bt. Mqzagecaglhfk, tylcuaqn etnceolb ce hz brxjlzurltye ohuw isig TKD wmc
qzrwmhhfaj nvtv zukh lzbafg cf." ― Toenxv Vhaloma"""
    # myKey = 'ASIMOV'
    myKey = 'DUMPLINGS'

    # myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.
    myMode = 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    #code here
    translated=[]
    keyindex=0
    key=key.upper()

    for symbol in message:
        # cari posisi key dan tambahin
        num=LETTERS.find(symbol.upper())
        if num!=-1:
            if mode=="encrypt":
                num+=LETTERS.find(key[keyindex])
            elif mode=="decrypt":
                num-=LETTERS.find(key[keyindex])
            num%=len(LETTERS)

            # append 
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyindex+=1
            # reset posisi keyindex
            if keyindex==len(key):
                keyindex=0

        else:
            translated.append(symbol)

    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()