# coding: utf-8
print("pares e impares")
num1= int(input("escriba un número entero: "))
num2= int(input("escriba un número entero mayor o igual queee: "))
if num2 < num1:
    print("¡le he da pedido un número entero mayor o igual que!")
else:
 for i in range(num1, num2 + 1):
  if i % 2 == 0:
     print("el número i es pares")
 else:
     print("el número i es impares")
