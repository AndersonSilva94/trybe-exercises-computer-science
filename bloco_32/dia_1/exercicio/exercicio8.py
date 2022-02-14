# Exercício 8 (Bônus 2): Faça um programa que, dado um valor n qualquer, tal que n > 1 ,
# imprima na tela um triângulo retângulo com n asteriscos de base.
# Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:

def create_triangle(number):
    n = 1
    asterisk = '*'
    while n <= number:
        print(asterisk * n)
        n += 1


create_triangle(5)
create_triangle(3)
