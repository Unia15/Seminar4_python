#Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
#и записать в файл многочлен степени k.


def coefficientPolynomial(k):
    import random
    lst = []
    for i in range(k+1):
        lst.append(random.randint(0, 100))
    return lst


def Polynomial(lstCoef,k):
    result = ""
    i = 0
    while k >= 1:
        if k==1:
            result += (f"{lstCoef[i]}x + ")
        elif lstCoef[i] != 0:
            result += (f"{lstCoef[i]}x^{k} + ")
        k -= 1
        i += 1
    result += (f"{lstCoef[i]} = 0")
    return result


import os 
os.system('cls')

print()
k = int(input("Введите натуральную степень k: "))

lstCoef = coefficientPolynomial(k)
PolyN = Polynomial(lstCoef,k)

print(f"Составлен многочлен {PolyN} натуральной степени {k} из списка коэффициентов {lstCoef} ")

with open("C:/Users/Юлия/Desktop/Учеба/Seminar4/file.txt", "w") as fl:
    fl.write(PolyN)
    print(f"Многочлен записан в файл {fl.name}")

