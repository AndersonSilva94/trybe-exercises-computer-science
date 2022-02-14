# Exercício 10 (Bônus 4): Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
#  - Até 20 litros, desconto de 3% por litro;
#  - Acima de 20 litros, desconto de 5% por litro.
# Gasolina:
#  - Até 20 litros, desconto de 4% por litro;
#  - Acima de 20 litros, desconto de 6% por litro.

# Escreva uma função que receba o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A - álcool, G - gasolina), e retorne o valor a ser pago pelo cliente,
# sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço do litro do álcool é R$ 1,90.

def fuel_price(type_fuel, liters):
    if type_fuel == "A":
        price = 1.90
        discount = 0.03
        if liters > 20:
            discount = 0.05
    elif type_fuel == "G":
        price = 2.50
        discount = 0.04
        if liters > 20:
            discount = 0.06
    total = price * liters
    total -= total * discount
    return total


print(fuel_price('A', 5))
print(fuel_price('G', 23))

# def calc_fuel(type_fuel, quantity):
#    total = 0
#    if type_fuel == 'A':
#        full_alcool = quantity * 1.90
#        if quantity < 20:
#            total = full_alcool - (full_alcool * 0.03)
#        else:
#            total = full_alcool - (full_alcool * 0.05)
#    elif type_fuel == 'G':
#        full_gasoline = quantity * 2.50
#        if quantity < 20:
#            total = full_gasoline - (full_gasoline * 0.04)
#        else:
#            total = full_gasoline - (full_gasoline * 0.06)
#    return total


# print(calc_fuel('A', 5))
# print(calc_fuel('G', 23))
