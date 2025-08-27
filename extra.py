frase = input("digite uma frase:")
vogais = 0
consoantes = 0
numeros = 0

for caractere in  frase:
    if caractere.lower() in "aeiou":
        vogais += 1
    elif caractere.isalpha():
        consoantes += 1
    elif caractere.isdigit():
        numeros += 1
print(f"quantidade de vogais: {vogais}")
print(f"quantidade de consoantes: {consoantes}")
print(f"quantidade de numeros: {numeros}")