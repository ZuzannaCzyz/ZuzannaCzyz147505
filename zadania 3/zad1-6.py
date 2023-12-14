def imie_nazwisko(name, surname):
    wynik = f"Cześć {name} {surname}!"
    return wynik


name = "Jan"
surname = "Kowalski"
result = imie_nazwisko(name, surname)
print(result)


def pomnoz(a, b):
    return a * b


liczba1 = 5
liczba2 = 6
wynik2 = pomnoz(liczba1, liczba2)
print(wynik2)


def czy_parzysta(liczba):
    return liczba % 2 == 0


liczba = 6
wynik = czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


def sprawdz_suma(a, b, c):
    return a + b >= c


arg1 = 5
arg2 = 3
arg3 = 8

wynik = sprawdz_suma(arg1, arg2, arg3)
if wynik:
    print("Suma dwóch pierwszych jest większa lub równa trzeciej")
else:
    print("Suma dwóch pierwszych jest mniejsza niż trzecia")


def sprawdz_wartosc(lista, wartosc):
    return wartosc in lista


moja_lista = [1, 2, 3, 4, 5]
szukana_wartosc = 3

wynik = sprawdz_wartosc(moja_lista, szukana_wartosc)
if wynik:
    print(f"Lista zawiera wartość {szukana_wartosc}")
else:
    print(f"Lista nie zawiera wartości {szukana_wartosc}")


def przetworz_listy(lista1, lista2):
    polaczona_lista = list(set(lista1 + lista2))

    wynik = [x ** 3 for x in polaczona_lista]

    return wynik


lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

wynik = przetworz_listy(lista1, lista2)
print(wynik)
