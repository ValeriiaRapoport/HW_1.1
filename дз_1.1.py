height = int(input(" Задайте высоту треугольника:   "))
for i in range(height):
    print(" "* (height - 1 - i) + "*" * (1+i*2))