def bracket_check():
    stroka = input()
    skobka = 0
    for i in stroka:
        if i == "(":
            skobka += 1
        elif i == ")":
            skobka -= 1
    if skobka != 0 or stroka[0] == ")":
        print("нет")
    else:
        print("является")
bracket_check()