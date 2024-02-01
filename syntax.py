


def syntaxf(res):

    state = "space"  # начальное состояние
    state_machine = {
        "space": {
            "space": "space",
            "kw_const": "const"
        },
        "const": {
            "space": "const",
            "identifier": "identifier"
        },
        "identifier": {
            "space": "identifier",
            "equally": "equally",
            "identifier": "identifier"
        },
        "equally": {
            "space": "equally",
            "dollar": "dollar",
            "sign": "sign",
            "integer": "integer",
        },
        "dollar": {
            "space": "dollar",
            "hex": "hex",
        },
        "hex": {
            "space": "hex",
            "semicolon": "semicolon",
        },
        "sign": {
            "space": "sign",
            "integer": "integer"
        },
        "integer": {
            "spase": "digit",
            "integer": "integer",
            "semicolon": "semicolon"
        },
        "semicolon": {
            "space": "semicolon"
        }
    }

    if len(res) == 0:
        return False

    for word, class_word in res:
        if class_word in state_machine[state]:
            state = state_machine[state][class_word]
        else:
            return False
    if state == "semicolon":
        return True

