def binary_search(tab, szukana):
    l = 0
    p = len(tab) - 1

    while l <= p:
        sr = (l + p) // 2

        if tab[sr] == szukana:
            return sr
        elif tab[sr] < szukana:
            l = sr + 1
        else:
            p = sr - 1

    return -1  # Liczba nie została znaleziona

tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

szukana = int(input("Podaj liczbę, którą chcesz znaleźć: "))

pozycja = binary_search(tab, szukana)

if pozycja != -1:
    print(f"Liczba {szukana} występuje w zbiorze w komórce o indeksie {pozycja}.")
else:
    print(f"Liczba {szukana} nie została znaleziona w zbiorze.")