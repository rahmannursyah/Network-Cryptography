message=".XbpXo8Xka8Obsbopb8.fmebo9"
SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

for key in range(len(SYMBOLS)):
    translated=""
    for symbol in message:
        if symbol in SYMBOLS:
             symbolindex=SYMBOLS.find(symbol)
             translatedindex=(symbolindex-key) % 66
             translated=translated+SYMBOLS[translatedindex]    
        else:
            translated=translated+symbol

    print(f"Key: #{key}: {translated}")