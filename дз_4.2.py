def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def main():
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        result = gcd(num1, num2)
        print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}.")
    except ValueError:
        print("Пожалуйста, введите корректные целые числа.")
if __name__ == "__main__":
    main()
