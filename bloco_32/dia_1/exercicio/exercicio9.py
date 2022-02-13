# Exercício 3: Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N .
# Por exemplo, para N = 5 , o valor esperado será 15 .

def sum_numbers(number):
    n = 1
    total = 0
    while n <= number:
        total += n
        n += 1
    print(total)


sum_numbers(5)
sum_numbers(3)
