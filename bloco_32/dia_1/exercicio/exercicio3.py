# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de
# asteriscos de lado de tamanho n

def create_square(number):
    for x in range(number):
        print(number * '*')


create_square(5)
create_square(2)