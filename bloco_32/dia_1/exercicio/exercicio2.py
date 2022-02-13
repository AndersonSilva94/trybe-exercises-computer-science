# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

def calc_arithmetic(list_number):
    total = 0
    for number in list_number:
        total += number
    return total / len(list_number)


print(calc_arithmetic([2, 3, 5, 6, 7]))
