# Wykorzystując pętle for
from typing import List


def wyswietl_liczby(lista):
    wynik = []
    for i in range(len(lista)):
        wynik.append(lista[i] * 2)
    print(wynik)


lista1: list[int] = [2, 5, 7, 6, 11]
wyswietl_liczby(lista1)


# Wykorzystując listę składaną
def wyswietl_skladana(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


lista2 = [2, 5, 7, 6, 11]
wynik2 = wyswietl_skladana(lista2)
print(wynik2)
