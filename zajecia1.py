# liczba = 0
# print(liczba)
# print(liczba+liczba)
# print("ala")
# def funkcja():
#     liczba = 0
#     print(liczba)
#     print(liczba+liczba)
#     print("ala")

print("ala ma " + "5 lat ") #konkatencja
print(0 + 1)
print(2 - 1)
print(2 * 1)
print(2 // 1) #dzielenie bez reszty
print(2 ** 1) #potegowanie
print(2 % 1) #dzielenie modulo 
print(5)
print("Ala ma 5 lat")
# print("ala ma "+ 5 +"lat") blad
print("ala ma " +str(5) + " lat")

#formatowanie wejscia

print("ala ma {} lat".format(5))
print("ala ma {1} lat a marta {0}".format(5,10))

imie = "Malgorzata"
print(imie[4])
print(imie.lower())
imie = imie.lower()#obie formy poprawne
print(imie)
"Wojtek".lower().lstrip().rsplit() #mechanizm lancuchowania

#listy

lista = []
print(type(lista))

lista2 = [1, 2, 3, 4, 5, 6, 7,]
lista2[3]
lista3 = lista + lista2
print(lista3)

lista4=[1, "ala", imie, 3.4, [1,3]] #Listy moga przechowywac rozne typy danych

print(lista4[4][1])#wypisanie elementu z listy dwupoziomowej

macierz= [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print(macierz[1][1])#wypisanie 5 ( zaczyna sie od 0)

#slownik

slownik = {}
print(type(slownik))
#<class 'dict'>
slownik["imie"] = "Marek"
print(slownik)

slownik2 = {
    'imie ': 'Marek',
    'wiek ': 21,
    'wzrost ': '192'} #drugi sposob na napisanie slwonika
print(slownik2)
print(slownik2)
print(slownik2.keys())
print(slownik2.items())
print(slownik2['imie '])

#import

# from math import *
# from math import pow
# pow(2, 2)

import math as m
m.pow(2, 2)
print (2)


