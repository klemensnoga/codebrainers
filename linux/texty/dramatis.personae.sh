#!/usr/bin/env bash

#grep -c Hamlet william.sheakespeare
#grep -c Macbeth william.sheakespeare
#grep -c "Lady Macbeth" william.sheakespeare
#grep -c 'Lady Macbeth' william.sheakespeare
#grep -c Lady\ Macbeth william.sheakespeare
#grep -c Ophelia william.sheakespeare
#grep -c Henry william.sheakespeare

#definujemy plik
text=william.sheakespeare

#definujemy liste imion
names="Hamlet Macbeth Ophelia Henry and"

# robimy petle po kolejnych imonach
for name in $names
#zawartosc petli pod spodem
do
	# wyswietlamy nazwe zmiennej
	echo -n  $name ": "
	# sprawdzamy ile razy zmienna wystepuje w pliku
	grep -c -i $name $text
	grep -c -i -w $name $text
done

echo $text

text="Praca skonczona!"

echo $text