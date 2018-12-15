# coding: utf-8
import math
math.inf
math.pi()
math.pi
math.cos(mat.pi)
math.cos(math.pi)
math.pow(2,5)
math.pow(2,255)
get_ipython().run_line_magic('pinfo2', 'math.pow')
get_ipython().run_line_magic('pinfo2', 'math.pi')
1 0.5j
a =1 0.5j
a =1 0.5i
get_ipython().set_next_input('a =complex');get_ipython().run_line_magic('pinfo2', 'complex')
a =complex(1,2)
a
1+2j
1+2j.conjugate
a = 1+2j.conjugate
a = 1+2j.conjugate()
a
1+2j.conjugate()
1+2j.real()
1+2j.real
1+2j.imag
liczba = 2
get_ipython().run_line_magic('pinfo2', 'liczba')
potega  =  liczba**8
potega
liczba_rzeczywista = liczba/3
liczba_rzeczywista
napis = "Ala ma kota"
napis2 = "a kot ma psa"
napis3 = napis + napis2 
napis3
napis3 = napis + " " + napis2 
napis3
"Ala ma kota" = napis3
napis2 = napis2 + napis3 + napis
napis2
napis2 = ""
napis2
del napis2
napis2
imiona = ["Henry", "Macbeth", "Lady Macbeth", "Ophelia" ]
imiona
numer = 24
numer
numer = 7.5
numer
calkowita = 4
calkowita2 = 8
mnozenie = calkowita*calkowita2
mnozenie
type(mnozenie)
dzielenie = calkowita2 / calkowita
dzielenie
type(dzielenie)
dzielenie_calkowite = calkowita2 // calkowita
dzielenie_calkowite
type(dzielenie_calkowite)
get_ipython().run_line_magic('pinfo2', 'int')
d = 98/99
d
l1 =99
l2 =98
wynik =l1/l2
wynik
wynik =l1//l2
wynik
type(wynik)
wynik =l1/l2
type(wynik)
wynik =l1%l2
wynik 
print(1)
print("ala ma kota")
print(wynik)
print(wynik*2+ 28)
print(wynik*2+ 28+" to jest wymn!)
print(wynik*2+ 28+" to jest wymn!")
print(str(wynik*2+ 28)+" to jest wymn!")
print("{} to jest wymn!".format((wynik*2+28)))
print("{} to jest wymn! A to inny {}".format((wynik*2+28, 2*16)))
print("{} to jest wymn! A to inny {}".format(wynik*2+28, 2*16))
print("{1} to jest wymn! A to inny {0}".format(wynik*2+28, 2*16))
print("%d to jest wymn! A to inny %d" % wynik*2+28, 2*16)
print("%d to jest wymn! A to inny %d" % (wynik*2+28), 2*16)
print("%d to jest wymn! A to inny %d" % (wynik*2+28), (2*16))
print("{1} to jest wymn! A to inny {0}".format(wynik*2+28, 2*16))
print(wynik*2+ 28+" to jest wymn!)
print(wynik*2+ 28+" to jest wymn!")
print(str(wynik*2+ 28)+" to jest wymn!")
imiona
type(imiona)
imiona.append("Hamlet")
imiona
imiona.append("Hamlet", 2)
imiona.extend("Hamlet", 2)
imiona.extend(("Hamlet", 2))
imiona
kortka = ('Henry', 'Macbeth', 'Lady Macbeth', 'Ophelia', 'Hamlet')
krotka = kortka
del kortka
kortka
krotka
type(krotka)
krotka.append(2)
krotka.count()
krotka.count("Henry")
krotka.count("Henryk")
krotka.index("Henryk")
krotka.index("Henry")
krotka.index("Hamlet")
krotka[4]
krotka[3]
krotka[3:4]
imiona
imiona[3]
imiona[4]
imiona[5]
imiona[6]
imiona[7]
imiona[0]
len(imiona)
for imie in imiona:
        print(imie)
        
get_ipython().run_line_magic('pinfo2', 'imiona.index')
get_ipython().run_line_magic('pinfo2', 'for')
imiona
nawiska=["Kowalski","Nowak", "McCain","Obama"]
ludzie = [imiona, nazwiska]
nazwiska = nawiska
del nawiska
listalist = [imiona,nazwiska]
listalist
len(listalist)
type(listalist)
listalist.append(imie)
listalist.append(2/3)
len(listalist)
listalist
lista
lista = [0,1,2,3,4,5,6,7,8,9]
len(lista)
lista[2]
lista[0]
lista[9]
lista.append(12)
lista.append(15)
lista.append(117)
lista2 = ["ala", "kot"]
lista.extend(lista2)
lista
lista[0] = "kot"
lista
get_ipython().run_line_magic('pinfo2', 'lista.insert')
lista.insert(3,"tutaj sie dolozylem")
lista
lista[3] = "tutaj"
lista
len(lista)
lista[10]
lista.insert(5,"insert")
len(lista)
lista[10]
lista
lista.insert(20,"insert")
lista
lista[19]
lista[18]
lista[17]
lista[-1]
lista[-10]
lista[0]
lista[-1]
lista[-0]
lista[-20]
lista[10:15]
lista[2:15:3]
lista
lista[:10]
przod = lista[:10]
koniec =lista[-10:]
przod
koniec
koniec[:3]
lista[10:15]
lista[15:10]
lista[15:10:-1]
lista.odwrocona = lista[::-1]
listaodwrocona = lista[::-1]
listaodwrocona.reverse()
listaodwrocona
listaodwrocona.reverse()
print(listaodwrocona.reverse())
listaodwrocona.reverse()
listaodwrocona
listaodwrocona.reverse()
listaodwrocona
przod
get_ipython().run_line_magic('pinfo2', 'przod.pop')
przod.pop[3]
przod.pop(3)
przod
przod.pop()
przod.pop()
przod.pop()
przod.pop()
przod.pop()
przod.pop()
przod.pop()
przod.pop()
przod.pop()
przod.pop()
lista=[0,1,2,3]
lista
krotka = (0,1,2,3)
krotka[2]
krotka[3]
krotka[4]
krotka[-1]
krotka[-2]
krotka[-3]
krotka[-4]
krotka[:-3]
krotka[:-2]
krotka[:]
krotka[2] = 5
krotka = lista
krotka[2] 
krotka[2] = 5
krotka[2]
krotka = (1,2,3,"alla")
krotka = (1,2,3,"alla", ("henio",lista))
krotka
type(krotka)
len(krotka)
list(krotka)
a = krotka
typ(a)
type(a)
b = (1,)
type(b)
b = 1,
type(b)
b[0] = "ala"
b = 1
type(b)
b = (1)
type(b)
b = (1,)
type(b)
b = (1+2+3 + 4+ 50*100)
b
b = (1+2+3 + 4+ 50*100,)
b
b = (1+2+3 +, 4+ 50*100)
b = (1+2+3 +4, 4+ 50*100)
b
{1,2,3,4,5}
zbior = {1,2,3,4,5}
zbior
type(zbior)
zbior[2]
zbior.add("ale")
type(zbior)
zbior
zbior.add("piwo")
zbior.add("cervanza")
zbior
zbior.add("ale")
zbior
print i in zbior:
for i in zbior:
        print(i)
        
zbior.pop("ale")
zbior.pop()
get_ipython().run_line_magic('pinfo2', 'zbior.discard')
zbior.discard("ale")
zbior
zbior.discard("ale")
zbior
lista1 = [for i in range(20): i]
lista1 = [i,for i in range(20): i]
lista1 = [i,for i in range(20)]
lista1 = [1, 2,3,4,5]
lista1 = [1, 4, 9]
lista1 = [1, 2,3,4,5]
lista2 = [1, 2,3,4,5]
lista1
lista2
lista1 = [1, 4, 9]
lista2 = [1, 2,3,4,5]
print(lista1,lista2)
lista = lista1 + lista2
lista
set(lista)
wspolne = []
for element in lista1:
        if element in lista2:
            wspolne.append(element)
            
wspolne
for element in lista1:
        if element in lista2:
            wspolne.append(element)
            
for element in lista1:
        if element in lista2:
            wspolne.append(element)
            
wspolne
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '')
get_ipython().run_cell_magic('timeit', 'wspolne.py', '')
get_ipython().run_cell_magic('timeit', '%run wspolne2.py', '')
get_ipython().run_line_magic('timeit', '%run wspolne2.py')
get_ipython().run_line_magic('timeit', '%run wspolne2.py')
get_ipython().run_line_magic('timeit', '%run wspolne2.py')
get_ipython().run_line_magic('timeit', '%run wspolne2.py')
get_ipython().run_line_magic('pinfo2', '%save')
get_ipython().run_line_magic('save', 'moje.komendy.py')
get_ipython().run_line_magic('save', '1 100 moje.komendy.py')
get_ipython().run_line_magic('save', '1-100 moje.komendy.py')
get_ipython().run_line_magic('pinfo2', '%save')
get_ipython().run_line_magic('save', 'moje.komendy.py')
get_ipython().run_line_magic('save', 'moje.komendy.py 1000')
get_ipython().run_line_magic('save', 'moje.komendy.py 10-100')
get_ipython().run_line_magic('save', 'moje.komendy.py 1-1000')
get_ipython().run_line_magic('save', 'dzien.1.sobota.12.08.py 1-2000')
