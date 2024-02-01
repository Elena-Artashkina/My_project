from lexem import lexical
from syntax import syntaxf
from trans import transliteration
from key_words import keywords


def in_outs():
    with open("INPUT.txt", "r") as fin:
        x = fin.readline()
        print(x)
        y = transliteration(x)
        print(y)
        z = lexical(y)  # обработка строки из INPUT.txt
        print(z)
        line = keywords(z)
        print(line)
        print(syntaxf(line))
    with open("OUTPUT.txt", "w") as fout:
        if (syntaxf(line)):  # проверка синтаксического блока программы
            fout.write("ACCEPT")
        else:
            fout.write("REJECT")


if __name__ == "__main__":
    in_outs()

