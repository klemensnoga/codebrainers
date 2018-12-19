#!/usr/bin/env python

import random

def wczytaj_liczby(starsze_liczby):
    """Funcja wczytuje dane z ze standardowego wejścia i sprawdza czy można je przekonwertować
    na liczby całkowite, czy zostały już wcześniej podane oraz czy należą do zakresu [1,49].
    Liczby można podawać pojedynczo lub odzielone przecinkiem."""

    # pusta lista a wpisywane liczby
    liczby = list()

    try:
        # wczytujemy liczby
        wejsciowe = input("Podaj swój typ: ")
        liczby.append(int(wejsciowe))

    except ValueError:
        try:
            # proba sprawdzenia czy dane wejściowe moża zamienić na listę liczb całkowitych
            lista_wejsciowych = wejsciowe.split(",")
            for liczba in lista_wejsciowych:
                liczby.append(int(liczba))
        except ValueError as err:
            print("Podaj liczbę całkowitą lub liczby całkowite oddzielone ',', błąd o treści: '{}'".format(err))
    
    # sprawdzanie czy liczby zawierają się w zakresie [1,49] oraz czy nie zostały wcześniej wylosowane
    for num in liczby: 
        if  num < 1 or num > 49:
            print("Liczba {} poza zakresem 1 do 49.".format(num))
        elif num in starsze_liczby:
            print("Liczba {} zostala wcześniej podana.".format(num))
        else: 
            starsze_liczby.add(num)

    return starsze_liczby

def unikalny_lotek():
    """Funkcja pobierająca 6 liczb całkowitch z stdin oraz losująca 6 liczb z zakresu [1,49].
    Sprawdza ile liczb z stdin pokrywa się z wylosowanymi. """

    #liczba liczb do losowania
    liczba_losowanych = 6

    typy_uzytkownika = set()
    typy_wylosowane = set()

    print("Program wylosuje {} liczb z zakresu 1 do 49. Proszę spróbuj zadnąć które.".format(liczba_losowanych))
    while len(typy_uzytkownika) < liczba_losowanych:
        # wywolaj funkcje wczytaj_liczby() zapisz jej wynik do zbioru
        typy_uzytkownika = wczytaj_liczby(typy_uzytkownika)
        
    # wyslosuj 6 liczb
    while len(typy_wylosowane) < liczba_losowanych:
        typy_wylosowane.add(random.randint(1,49))

    # poprzednie wersje kodu
    #trafione = 0
    #    for tw in typy_wylosowane:
    #       for tu in typy_uzytkownika:
    #           if tw == tu:
    #               trafione += 1

    #trafione = list()
    #for tu in typy_uzytkownika:
    #    if tu in typy_wylosowane:
    #        trafione.append(tu)

    # zbiór wspólny typów użytkownika i liczb wysosowanych
    trafione = typy_uzytkownika & typy_wylosowane

    print("Twoje typy: ",typy_uzytkownika)
    print("Wylosowane liczby: ",typy_wylosowane)
    if trafione:
        if len(trafione) > 1:
            print("Udało Ci się trafić {} z 6 liczb, te liczby to {}.".format(len(trafione), trafione))
        else:
            print("Udało Ci się trafić jedną z 6 liczb, jest to {}.".format(trafione))
    else:   
        print("Niestety nie udało Ci się trafić w żadną z liczb. Spróbuj szczęścia ponownie!")

# uruchamiamy funcje        
unikalny_lotek()