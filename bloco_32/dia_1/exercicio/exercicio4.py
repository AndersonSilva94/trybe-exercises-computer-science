# Crie uma função que receba uma lista de nomes e
# retorne o nome com a maior quantidade de caracteres.
# Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" .

def find_biggest_name(list_name):
    biggest_name = ''
    for name in list_name:
        if len(biggest_name) < len(name):
            biggest_name = name
    return biggest_name


print(find_biggest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))
print(find_biggest_name(["Josevaldo", "Lucas", "Nádia", "Fê", "Cairo", "Joana"]))
