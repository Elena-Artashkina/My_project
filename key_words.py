keywords1 = ["and", "array", "asm", "begin", "break", "case", "const",
            "constructor", "continue", "destructor", "div", "do", "downto",
            "else", "end", "false", "file", "for", "function", "goto", "if",
            "implementation", "in", "inline", "interface", "label", "mod", "nil",
            "not", "object", "of", "on", "operator", "or", "packed", "procedure",
            "program", "record", "repeat", "set", "shl", "shr", "string", "then",
            "to", "true", "type", "unit", "until", "uses", "var", "while", "with", "xor"]


# ключевые слова Pascal


def keywords(words):
    res = []

    for word, lex in words:
        if word in keywords1:
            if word == "const":
                res.append((word, f"kw_{word}"))
            else:
                res.append((word, "keyword"))
        else:
            res.append((word, lex))

    return res
