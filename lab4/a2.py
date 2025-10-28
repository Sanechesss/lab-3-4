n = int(input("Введите n: "))
m = int(input("Введите m: "))
print("\nПРЯМОУГОЛЬНИК:")
for i in range(n):
    for j in range(m):
        print("#", end="")
    print()
print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(n):
    for j in range(i + 1):
        print("#", end="")
    print()
print("\nРАМКА:")
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()