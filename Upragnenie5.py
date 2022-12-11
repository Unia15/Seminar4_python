#Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.


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
            result += (f"{lstCoef[i]}*x + ")
        elif lstCoef[i] != 0:
            result += (f"{lstCoef[i]}*x^{k} + ")
        k -= 1
        i += 1
    result += (f"{lstCoef[i]} = 0")
    return result


def SumPolynomial(polyLst1,polyLst2):
    count1 =0
    count2=0
    new_poly = ""

    for i in range(len(polyLst2)):
        result = 0
        if i == len(polyLst2) - 1:
            result += int(polyLst1[-1])+int(polyLst2[-1])
            new_poly += str(result)
        elif i == len(polyLst2) - 2:
            result += int(polyLst1[-2][:-2])+int(polyLst2[-2][:-2])
            new_poly += str(result) + polyLst1[-2][-2:] + " + " 
        else:
            result += int(polyLst1[count1][:-4])+int(polyLst2[count2][:-4])
            new_poly += str(result) + polyLst1[count1][-4:] + " + " 
            count1 += 1
            count2 += 1
    return new_poly

import os 
os.system('cls')

print("Программа считывает многочлены из 2х файлов и формирует файл, содержащий их сумму.")
k = int(input("Введите натуральную степень для формирования 2х многочленов k: "))
p = 2
while p >= 1:
    lstCoef = coefficientPolynomial(k)
    PolyN = Polynomial(lstCoef,k)
    with open("C:/Users/Юлия/Desktop/Учеба/Seminar4/file"+ str(p) + ".txt", "w") as fl:
        fl.write(PolyN)
        print(f"Многочлен записан в файл {fl.name}")
    p-=1

with open("C:/Users/Юлия/Desktop/Учеба/Seminar4/file1.txt", "r") as fl:
    poly1 = fl.read()
    polyLst1 = poly1.replace(" = 0","").split(" + ")
with open("C:/Users/Юлия/Desktop/Учеба/Seminar4/file2.txt", "r") as fl:
    poly2 = fl.read()
    polyLst2 = poly2.replace(" = 0","").split(" + ")

sumPoly = SumPolynomial(polyLst1, polyLst2)+" = 0"

print(f"Суммой двух многочленов: ")
print(f"1. {poly1}")
print(f"2. {poly2}")
print(f"Является многочлен {sumPoly},")
with open("C:/Users/Юлия/Desktop/Учеба/Seminar4/file3.txt", "w") as fl:
    fl.write(sumPoly)
    print(f"который записан в файл {fl.name}")
