# Affine Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    # You might want to copy & paste this text from the source code at
    # https://www.nostarch.com/crackingcodes/affineHacker.py
    myMessage ="FUUDSR LDYARE"

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard.
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    global SILENT_MODE
# ketikkan code dari slide 8 - 11 atau menggunakan versi Anda.
    print("Hacking...")
    print("Ctrl-C or Ctrl-D to quit at any time")

    for key in range(len(affineCipher.SYMBOLS)**2):
        keyA=affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS))!=1:
            continue

        decryptedtext=affineCipher.decryptMessage(key,message)
        if not SILENT_MODE:
            print(f"Tried key {key}... ({decryptedtext[:40]})")

        if detectEnglish.isEnglish(decryptedtext):
            print("Possible encryption hack: ")
            print(f"Key: {key}")
            print(f"Decrypted message: {decryptedtext[:200]}")
            print("Enter D for done, or just press Enter to continue hacking: ")
            response=input("> ")
            if response.upper()=="D":
                return decryptedtext
        
    return None

# If affineHacker.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()