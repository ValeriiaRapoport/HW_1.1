number_to_words1={0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
                  6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
                  11: "одинадцать", 12: "двенадцать", 13: "тринадцать", 14: "черырнадцать", 15: "пятнадцать",
                  16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
number_to_words2={20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят",
                  60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто", }
number_to_words3={100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот",
                  600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот"}
number=int(input("Введите число:  "))
if number<20:
    print(number_to_words1[number])
elif number>=20 and number<100 and number%10==0:
    print(number_to_words2[number])
elif number>=20 and number<100 and number%10!=0:
    tens=number//10
    units=number%10
    print(number_to_words2[tens*10]+" "+number_to_words1[units])
elif number>=100 and number<=999 and number%100==0:
    print(number_to_words3[number])
elif number>=100 and number<=999 and number%100!=0:
    tens=number %100
    hundreds=number-tens
    tens1=tens//10
    units=tens%10
    if tens>=0 and tens<=19:
        print(number_to_words3[hundreds]+" "+number_to_words1[tens])
    elif tens>=10 and tens<=90 and tens%10==0:
        print(number_to_words3[hundreds]+" "+number_to_words2[tens])
    else:
        print(number_to_words3[hundreds]+" "+number_to_words2[tens1*10]+" "+number_to_words1[units])
else:
    print("Ошибка! Введите число от 0 до 999")
