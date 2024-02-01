
alphabet_hex = "abcdef"

def lexical(symbols):
    words = []
    word = ""

    state = "SPACE"  # начальное состояние
    state_machine = {
        "SPACE": {
            "letter": "ID",
            "letter_hex": "ID",
            "number": "INT",
            "sign": "SPACE",
            "space": "SPACE",
            "dollar": "HEX",
            "equally": "SPACE",
            "semicolon": "SPACE",
            "error": "ERROR",
        },
        "ID": {
            "letter": "ID",
            "letter_hex": "ID",
            "number": "ID",
            "sign": "SPACE",
            "space": "SPACE",
            "dollar": "SPACE",
            "equally": "SPACE",
            "semicolon": "SPACE",
            "error": "ERROR",
        },
        "INT": {
            "letter": "ERROR",
            "letter_hex": "ERROR",
            "number": "INT",
            "sign": "SPACE",
            "space": "SPACE",
            "dollar": "SPACE",
            "equally": "SPACE",
            "semicolon": "SPACE",
            "error": "ERROR",
        },
        "HEX": {
            "letter": "ERROR",
            "letter_hex": "HEX",
            "number": "HEX",
            "sign": "SPACE",
            "space": "SPACE",
            "dollar": "SPACE",
            "equally": "SPACE",
            "semicolon": "SPACE",
            "error": "ERROR",
        }
    }  # состояния автомата


    for sim, lex in symbols:
        if state == "SPACE":
            if lex == "letter" or lex == "number" or lex == "letter_hex":
                word += sim
                state = state_machine[state][lex]
            elif lex == "error":
                return []
            else:
                words.append((sim, lex))
                state = state_machine[state][lex]

        elif state == "ID":
            if lex == "letter" or lex == "number" or lex == "letter_hex":
                word += sim
                state = state_machine[state][lex]
            elif lex == "error":
                return []
            else:
                words.append((word, 'identifier'))
                word = ""
                words.append((sim, lex))
                state = state_machine[state][lex]

        elif state == "INT":
            if lex == "number":
                word += sim
                state = state_machine[state][lex]
            elif lex == "error" or lex == "letter" or lex == "letter_hex":
                return []
            else:
                words.append((word, 'integer'))
                word = ""
                words.append((sim, lex))
                state = state_machine[state][lex]

        elif state == "HEX":
            if lex == "letter_hex" or lex == "number":
                word += sim
                state = state_machine[state][lex]
            elif lex == "error" or lex == "letter":
                return []
            else:
                words.append((word, 'hex'))
                word = ""
                words.append((sim, lex))
                state = state_machine[state][lex]

    if word != "":
        if word.isdigit():
            words.append((word, "integer"))
        elif word in alphabet_hex:
            words.append((word, "hex"))
        else:
            words.append((word, "identifier"))
    return(words)


