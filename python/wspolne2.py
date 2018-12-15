#!/usr/bin/env python

lista1 = [x**2 for x in range(1,10000)]
lista2 = [x**3 for x in range(1,10000)]

#informujemy o dlugosci listy
print("dlugosc listy pierwszej to {}, a drugiej to {}".format(len(lista1),len(lista2)))
print("dlugosc listy pierwszej to ", len(lista1), ", a drugiej to", len(lista2) )

wspolne = []

#to jest petla po elemntach listy lista1
#for el in lista1:
#    if el in lista2:
#        wspolne.append(el)

# dostalismy wynik ale wolno    
print("Elementy wspólne list to: ", wspolne, " jest ich ", len(wspolne))

# sprobojmy przez sety

set1 = set(lista1)
set2 = set(lista2)

wspolne = set1 & set2
print("Elementy wspólne list to: ", wspolne, " jest ich ", len(wspolne))

for el in wspolne:
    print("Wynik działania: {}, to szescian {} oraz kwadrat {}".format(el, int(el**(1/3)), int(el**0.5)))


