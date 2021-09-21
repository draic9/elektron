import math

# miejsca zerowe funkcji kwadratowej biorąc abc z inputu
a = input("podaj a: ")
b = input("podaj b: ")
c = input("podaj c: ")

a = int(a)
b = int(b)
c = int(c)

delta = b** - 4 * a * c
konw = math.sqrt(delta)
x1 = (-b - konw) / 2*a
x2 = (+b + konw) / 2*a

print(f"delta wynosi {delta}")
print(f"x1 to {x1}")
print(f"x2 to {x2}")
