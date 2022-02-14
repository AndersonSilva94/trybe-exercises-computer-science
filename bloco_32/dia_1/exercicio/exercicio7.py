# Exercício 7 (Bônus 1): Dada uma lista, descubra o menor elemento.
# Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2 .

def find_smallest_number(list_numbers):
    smallest_number = list_numbers[0]
    for number in list_numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number


print(find_smallest_number([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))
print(find_smallest_number([5, 9, -3, 19, 70, 8, 100, 2, 35, 27]))
print(find_smallest_number([5, 9, 30, 19, 70, 8, 100, 20, 35, 27]))
