alphabet_no_hex = "ghijklmnopqrstuvwxyz"
alphabet_hex = "abcdef"
digits = "0123456789"

def transliteration(data):
    data = data.lower()
    symbols = []

    for symbol in data:
        if symbol in alphabet_no_hex:
            symbols.append((symbol, "letter"))
        elif symbol in alphabet_hex:
            symbols.append((symbol, "letter_hex"))
        elif symbol in digits:
            symbols.append((symbol, "number"))
        elif symbol in "-":
            symbols.append((symbol, "sign"))
        elif symbol in "+":
            symbols.append((symbol, "sign"))
        elif symbol in "$":
            symbols.append((symbol, "dollar"))
        elif symbol in "=":
            symbols.append((symbol, "equally"))
        elif symbol in ";":
            symbols.append((symbol, "semicolon"))
        elif symbol in " ":
            symbols.append((symbol, "space"))
        else:
            symbols.append((symbol, "error"))

    return symbols
