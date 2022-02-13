# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou
# "não é triangulo" , caso não seja possível formar um triângulo.

def type_triangle(sideA, sideB, sideC):
    is_triangle = (
        sideA + sideB > sideC and
        sideB + sideC > sideA and
        sideA + sideC > sideB
    )
    if not is_triangle:
        return "Não é triângulo"
    elif sideA == sideB == sideC:
        return "Triângulo equilátero"
    elif sideA == sideB or sideB == sideC or sideA == sideC:
        return "Triângulo isóceles"
    else:
        return "Triângulo escaleno"


print(type_triangle(2, 1, 4))
print(type_triangle(4, 4, 4))
print(type_triangle(4, 4, 6))
print(type_triangle(2, 3, 4))
