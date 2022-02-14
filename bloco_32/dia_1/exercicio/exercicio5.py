# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta
# a serem compradas e o preço total a partir do tamanho de uma parede(em m²).
import math


def calc_paint(wall_size):
    amount_of_liters = math.ceil(wall_size / 3)
    amount_of_cans = math.ceil(amount_of_liters / 18)
    total_price = amount_of_cans * 80
    values_wall_size = (amount_of_cans, total_price)
    return values_wall_size


print(calc_paint(30))
print(calc_paint(60))
print(calc_paint(120))
