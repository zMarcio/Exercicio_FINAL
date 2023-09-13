vogais = ["a", "e", "i", "o", "u"]

words = []

while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()

    if not word:
        break

    final_world = ""

    for letter in word:
        if letter.lower() in "aeiou":
            final_world += letter * 2 
        else:
            final_world += letter
    words.append(final_world)

for word in words:
    print(word, sep='\n')