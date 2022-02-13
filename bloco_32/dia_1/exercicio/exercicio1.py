# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.

def returns_greater_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(returns_greater_number(10, 9))
print(returns_greater_number(8, 20))
