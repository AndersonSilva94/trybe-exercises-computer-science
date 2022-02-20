# Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses valores.
# Caso algum valor da entrada seja inválido, por exemplo uma letra,
# uma mensagem deve ser exibida, na saída de erros, no seguinte formato:
# "Erro ao somar valores, {valor} é um valor inválido". Ao final, você deve imprimir a soma dos valores válidos.

numbers_or_letters = input("Digite seus valores, separados por um espaço, e aperte enter: ")
verify_inputs = numbers_or_letters.split()

def verify_input_function(value):
    value_input = 0
    for inputs in verify_inputs:
        if inputs.isdigit() == False:
            print("Erro ao somar valores, ", inputs, " é um valor inválido")
            return
        else:
            value_input += int(inputs)
    print(value_input)

verify_input_function(numbers_or_letters)
