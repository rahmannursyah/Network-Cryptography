import math
def decrypt(key,message):
    numofcolumns=int(math.ceil(len(message)/float(key)))
    numofrows=key
    numofshades=(numofcolumns*numofrows)-len(message)

    plaintext=[""]*numofcolumns
    column=0
    row=0

    for symbol in message:
        plaintext[column]+=symbol
        column+=1

        if(column==numofcolumns) or (column==numofcolumns-1 and row>=numofrows-numofshades):
            column=0
            row+=1

    return "".join(plaintext)

message="Cenoonommstmme oo snnio. s s c"
key=8
print(decrypt(key,message))