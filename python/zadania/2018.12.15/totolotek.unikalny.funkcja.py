#!/usr/bin/env python

import random

def wczytaj_liczby(starsze_liczby):

    liczby = list()

    try:
        liczby.append(int(input("Podaj swój typ: ")))
    except ValueError as err:
        print("Podaj liczbę całkowitą, błąd o treści: '{}'".format(err))
    
    for num in liczby: 
        if  num < 1 or num > 49:
            print("Liczba {} poza zakresem 1 do 49.".format(num))
        elif num in starsze_liczby:
            print("Liczba {} zostala wcześniej podana.".format(num))
        else: 
            starsze_liczby.add(num)

    return starsze_liczby

def unikalny_lotek():
    typy_uzytkownika = set()
    typy_wylosowane = set()

    print("Program wylosuje 6 liczb z zakresu 1 do 49. Proszę spróbuj zadnąć które.")
    while len(typy_uzytkownika) < 6:
        # wywolaj funkcje wczytaj_liczby() zapisz jej wynik do zbioru
        typy_uzytkownika = wczytaj_liczby(typy_uzytkownika)
        
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