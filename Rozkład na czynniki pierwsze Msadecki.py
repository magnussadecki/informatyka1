def rozklad_na_czynniki_pierwsze(n):
    k = 2  # Pierwsza liczba pierwsza
    czynniki = []  # Tutaj będziemy przechowywać czynniki pierwsze

    while n > 1:
        while n % k == 0:
            czynniki.append(k)  # Dodajemy czynnik pierwszy do listy
            n //= k  # Skracamy n przez czynnik pierwszy
        k += 1  # Przechodzimy do następnej liczby pierwszej

    return czynniki

n = int(input("Podaj liczbę większą od 1: "))
if n <= 1:
    print("Podana liczba musi być większa od 1.")
else:
    czynniki_pierwsze = rozklad_na_czynniki_pierwsze(n)
    print(f"Czynniki pierwsze liczby {n}: {' '.join(map(str, czynniki_pierwsze))}")
