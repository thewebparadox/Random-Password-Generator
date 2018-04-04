import random

def passgenerator():
    lettersl1 = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])
    lettersl2 = random.choice(["s", "t", "u", "v", "w", "x", "y", "z"])

    lettersl3 = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])
    lettersl4 = random.choice(["s", "t", "u", "v", "w", "x", "y", "z"])

    lettersl5 = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])
    lettersl6 = random.choice(["s", "t", "u", "v", "w", "x", "y", "z"])

    lettersc1 = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"])
    lettersc2 = random.choice(["S", "T", "U", "V", "W", "X", "Y", "Z"])

    lettersc3 = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"])
    lettersc4 = random.choice(["S", "T", "U", "V", "W", "X", "Y", "Z"])

    lettersc5 = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"])
    lettersc6 = random.choice(["S", "T", "U", "V", "W", "X", "Y", "Z"])

    numbers1 = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    numbers2 = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    numbers3 = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])

    schars1 = random.choice(["!", "@", "$", "%", "^", "#", "&", "(", "_", ")", "~", "/"])
    schars2 = random.choice(["!", "@", "$", "%", "^", "#", "&", "(", "_", ")", "~", "/"])
    schars3 = random.choice(["!", "@", "$", "%", "^", "#", "&", "(", "_", ")", "~", "/"])

    schars4 = random.choice([schars1, schars2, schars3])
    schars5 = random.choice([schars1, schars2, schars3])
    schars6 = random.choice([schars1, schars2, schars3])
    schars7 = random.choice([schars1, schars2, schars3])

    numbers4 = random.choice([numbers1, numbers2, numbers3])
    numbers5 = random.choice([numbers1, numbers2, numbers3])
    numbers6 = random.choice([numbers1, numbers2, numbers3])
    numbers7 = random.choice([numbers1, numbers2, numbers3])

    lettersl = random.choice([lettersl1, lettersl2, lettersl3, lettersl4, lettersl5, lettersl6])
    lettersc = random.choice([lettersc1, lettersc2, lettersc3, lettersc4, lettersc5, lettersc6])

    letters1 = random.choice([lettersl, lettersc])
    letters2 = random.choice([lettersl1, lettersc1])
    letters3 = random.choice([lettersl2, lettersc2])
    letters4 = random.choice([lettersl3, lettersc3])
    letters5 = random.choice([lettersl4, lettersc4])
    letters6 = random.choice([lettersl5, lettersc5])
    letters7 = random.choice([lettersl6, lettersc6])

    pass0 = random.choice([numbers4, schars4, letters1, schars5, numbers5, schars6, letters2, schars7, numbers6, letters3, numbers7, letters4, letters5, letters6, letters7])
    pass1 = random.choice([schars4, letters1, schars5, numbers4, schars6, letters2, schars7, numbers5, letters3, numbers6, letters4, numbers7, letters5, letters6, letters7])
    pass2 = random.choice([numbers4, schars4, letters1, schars5, numbers5, schars6, letters2, schars7, numbers6, letters3, numbers7, letters4, letters5, letters6, letters7])
    pass3 = random.choice([schars4, letters1, schars5, numbers4, schars6, letters2, schars7, numbers5, letters3, numbers6, letters4, numbers7, letters5, letters6, letters7])
    pass4 = random.choice([numbers4, schars4, letters1, schars5, numbers5, schars6, letters2, schars7, numbers6, letters3, numbers7, letters4, letters5, letters6, letters7])
    pass5 = random.choice([schars4, letters1, schars5, numbers4, schars6, letters2, schars7, numbers5, letters3, numbers6, letters4, numbers7, letters5, letters6, letters7])
    pass6 = random.choice([numbers4, schars4, letters1, schars5, numbers5, schars6, letters2, schars7, numbers6, letters3, numbers7, letters4, letters5, letters6, letters7])
    pass7 = random.choice([schars4, letters1, schars5, numbers4, schars6, letters2, schars7, numbers5, letters3, numbers6, letters4, numbers7, letters5, letters6, letters7])
    pass8 = random.choice([numbers4, schars4, letters1, schars5, numbers5, schars6, letters2, schars7, numbers6, letters3, numbers7, letters4, letters5, letters6, letters7])
    pass9 = random.choice([schars4, letters1, schars5, numbers4, schars6, letters2, schars7, numbers5, letters3, numbers6, letters4, numbers7, letters5, letters6, letters7])

    print('\n')
    print(f'Your password is: {pass0}{pass1}{pass2}{pass3}{pass4}{pass5}{pass6}{pass7}{pass8}{pass9}')
    print('\n')

while 1:
    print('\n')
    ask = input("generate password: ")

    if ask == "yes":
        passgenerator()
