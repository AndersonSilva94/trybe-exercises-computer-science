characters_file = open("meus_personagens_favoritos.txt", mode="w")

characters_file.write("Daenerys Targaryen\n")
characters_file.write("Simon Spier\n")
characters_file.write("Scooby-doo\n")

print("Homem Aranha", file=characters_file)

more_characters = ["Robert Langdom\n", "Arya Stark\n"]

characters_file.writelines(more_characters)

characters_file.close()
