#!/usr/bin/env python

import random

def unikalny_lotek():
    typy_uzytkownika = set()
    typy_wylosowane = set()

    print("Program wylosuje 6 liczb z zakresu 1 do 49. Proszę spróbuj zadnąć które.")
    while len(typy_uzytkownika) < 6:
        x = int(input("Podaj swój typ: "))
        if  x < 1 or x > 49:
            print("Liczba poza zakresem 1 do 49")
        elif x in typy_uzytkownika:
            print("Podałeś już tą liczbe!")
        else:
            typy_uzytkownika.add(x)
        
    while len(typy_wylosowane) < 6:
        typy_wylosowane.add(random.randint(1,49))

    i = list()

        #for x in typy_wylosowane:
        #    for y in typy_uzytkownika:
        #        if y == x:
        #            i += 1

    #for x in typy_uzytkownika:
    #    if x in typy_wylosowane:
    #        i.append(x)

    i = typy_uzytkownika & typy_wylosowane

    print("Twoje typy: ",typy_uzytkownika)
    print("Wylosowane kule: ",typy_wylosowane)
    print("Udało Ci się trafić {} z 6, te kule to {}.".format(len(i), i))

unikalny_lotek()