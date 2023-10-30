def szybkie_potegowanie(a, n):
  

  w = 1
  while n > 0:
    if n % 2 == 1:
      w *= a
    a *= a
    n //= 2
  return w


if __name__ == "__main__":
  a = int(input("Podaj podstawę: "))
  n = int(input("Podaj wykładnik: "))
  print(f"{a} do potegi {n} wynosi: {szybkie_potegowanie(a, n)}")