# Codingan caesar file cipher beserta penjelasan module yang dipakai

import caesarEncryptDecrypt, os, sys

filename=input("Input the filename with extension that you want to open: ")
mode=input("(encrypt) untuk encrypt file (decrypt) untuk decrypt file: ")
output_file_name=input("Input the filename with extension to save the new file: ")
key = 10

if not os.path.exists(filename): # untuk mengecek apakah directory atau path dari file yg mau dibuka exist atau tidak
    print(f"{filename}doesn't exist. Quitting program...")
    sys.exit()

if os.path.exists(output_file_name): # untuk mengecek apakah nama dari output file kita sudah ada atau belum, kalo ada akan override file tersebut
    print(f"{output_file_name} already exist. This will override the existing file... (C) to Continue (Q) to quit")
    response=input(">>")
    if(response.lower().startswith("q")):
        sys.exit() # kalo inputan keyboard = q program akan exit

file=open(filename, 'r') # untuk membuka file dengan mode read
file_content=file.read()
file.close()

if mode.lower()=="encrypt" :
    translated=caesarEncryptDecrypt.encryptedCaesar(file_content, key) # untuk encrypt isi file yg kita buka dengan caesar encryption
        
elif mode.lower()=="decrypt":
    translated=caesarEncryptDecrypt.decryptCaesar(file_content, key) # untuk decrypt isi file yg kita buka dengan caesar decryption
        

output_file=open(output_file_name,'w') # untuk membuka file dengan mode write
output_file.write(translated)
output_file.close()
print(f"SUCCESSFULLY {mode.upper()}ED THE FILE")      