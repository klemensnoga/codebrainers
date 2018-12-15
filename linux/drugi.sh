!#/usr/bin/env bash

# Tworzymy katalog 2018.12.15.cwiczenia, flaga -p zapewnia, ze nie bedzie bledu jesli istnieje
mkdir -p 2018.12.15.cwiczenia
cd 2018.12.15.cwiczenia

echo "To jest pierwszy skrypt"

# By zapisac do pliku uzywamy przekierowania > gdy nadpisujemylub >> zapisujemy na koncu pliku  
echo "Ten napis zapiszemy do pliku stdout.txt" $(date) >> stdout.txt

echo "Sprawdzmy czy poprzednie echo rzeczywiscie zostal zapisany"


more stdout.out