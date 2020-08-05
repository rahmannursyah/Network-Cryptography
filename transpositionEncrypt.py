def encrypt(key,message):
    ciphertext=[""]*key

    for column in range(key):
        currindex=column

        while currindex<len(message):
            ciphertext[column]+=message[currindex]
            currindex+=key

    return "".join(ciphertext)

message="Common sense is not so common."
key=8
print(encrypt(key,message))