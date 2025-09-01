#Desafio 5:
# nota = float(input("Digite a nota do aluno:"))
# if nota >= 7:
#     print("voce foi aprovado")

# else:
#     print("voce foi reprovado")

#Exercícios de Estruturas de Decisão

#Nível Básico exercicio 1
# idade = int(input("qual sua idade:"))
# if idade >= 18:
#     print("voce é maior de idade")

# else:
#     print("voce é menor de idade!")

# exercicio 2
# numero = int(input("DIgite um numero inteiro:"))
# if numero >=  0:
#     print("O numero é positivo!")

# elif numero <= 0:
#     print("O numero é negativo!")

# else:
#     print("O numero é Zero!")

#xercicio 3
# repita = True
# senha = "errada"

# while repita:
#  senha_fixa = "python123"

#  senha_digitada = input("Ditite uma senha:")

#  if senha_digitada == senha_fixa:
#      print("Login Bem Sucedido!")
#      repita = False
#  else:
#      print("Senha incorreta!")

#exercicio 4
# numero = int(input("Digite um numero inteiro:"))

# if numero % 2 == 0:
#     print("O numero é par!")

# else:
#     print("O numero é impar!")

# exercicio 5
# nota = float(input("Digite a nota do aluno:"))
# if nota >= 7:
#     print("voce foi aprovado")

# else:
#     print("voce foi reprovado")

#Nível Intermediário

# exercicio 1
# num1 = float(input("Digit o primeiro numero:"))
# num2 = float (input("Digite o segundo numero"))

# if num1 > num2:
#     print(f"o maior numero é: {num1}")
# elif num2 > num1:
#      print(f"o maior numero é: {num2}")

# else:
#      print("Os numero são iguais (Dgite numeros diferentes).")

#exercicio 2
# cor = input("Dgite a cor do semáforo (vermelho, verde, amarelo):").lower()

# if cor == "vermelho":
#     print("parar")

# elif cor == "amarelo":
#     print("Atenção")

# elif cor == "verde":
#     print("acelere")
    
# else:
#     print("Cor inválida. Digite vermelho, amarelo ou verde.")

#exercicio 3
# a = float(input("Digite o primeiro lado: "))
# b = float(input("Digite o segundo lado: "))
# c = float(input("Digite o terceiro lado: "))

# if a + b > c and a + c > b and b + c > a:
#     print("É possível formar um triângulo.")
# else:
#     print("Não é possível formar um triângulo.")

#exercicio 4
# ano = int(input("digite um ano: "))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print("Ano Bissexto!")

# else:
#     print("Não é Bissexto!")

# Nível Avançado

# exercicio 1
# num1 = float(input("Digite o primeiro numero:"))
# num2 = float(input("Dgite o segundo numero:"))
# operador = input("Digite o operado (+, -, *, /):")

# if operador == "+":
#     print("resultado:", num1 + num2)

# elif operador == "-":
#     print("resultado:", num1 - num2)

# elif operador == "*":
#       print("resultado:", num1 * num2)

# elif operador == "/":
#      if num2 != 0:
#           print("resultado:", num1 / num2)
#      else:
#         print("Erro: Divisão por zero!")

# else:
#      print("Operador inválido!")

#exercicio 2
# a = float(input("Digite o primeiro lado:"))
# b = float(input("Digite o segundo lado:"))
# c = float(input("Digite o terceiro lado:"))

# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Triangulo é equilátero:")
#     elif a == b or b == c or a == c:
#         print("Triangulo Isósceles")
#     else:
#         print("Trinagulo Escaleno:")
# else:
#     print("Não é um trinagulo válido.")

#exericio 3
# peso = float(input("Digite o seu peso:"))
# altura = float(input("digite sua altura:"))
# imc = peso / (altura ** 2)
# print(f"O seu immc é: {imc:.2f}")

# if imc < 18.5:
#     print("abaixo do peso")
# elif imc < 25:
#     print("peso normal")
# elif imc < 30:
#     print("sobrepeso")
# else:
#     print("Obesidade")

# peso_min = 18.5 * (altura ** 2)
# peso_max = 24.9 * (altura ** 2)

# print(f"\nPara estar dentro do seu peso normal, você deveria estar pesando no minimo {peso_min:.2f} e no maximo {peso_max:.2f} kg.")

#exercico 4
# senha = input("Digite sua senha:")
# if len(senha) >= 8 and any(c.isupper() for c in senha) and any(c.isdigit() for c in senha):
#     print("Senha válida!")
# else:
#     print("senha inválida! A senha Deve ter no minimo 8 caracteres, uma letra maiúscula e um número.")

#exercicio 5
# import random
# numero_secreto = random.randint(1, 10)
# acertou = False

# while  not acertou:
#     palpite = int(input("Adivinhe o número de (1 a 10):"))

#     if palpite == numero_secreto:
#         print("Você acertou!")
#         acertou = True

#     elif palpite > numero_secreto:
#         print("Muito alto!")

#     else:
#         print("Muito baixo!")

#exercicio 6
# valor = float(input("Digite o valor da compra: R$"))
# tipo = input("Digite o tipo de cliente (normal, premium , vip):").lower()

# if tipo == "premium":
#     desconto  = 0.15

# elif tipo ==  "vip":
#     if valor > 200:
#         desconto = 0.25
#     else:
#         desconto = 0.10
# else:
#     desconto = 0.0

# total = valor - (valor * desconto)
# print(f"Total de desconto: R$ {total:.2f}")

# exercicio 7
# ano = int(input("Digite um ano:"))

# if ano % 400 == 0:
#     print("Ano bissexto!")
# elif ano % 4 == 0 and ano % 100 != 0:
#     print("Ano bissexto!")
# else:
#     print("Não é bissexto!")

# exercicio 8
# valor = float(input("Digite o valor em reais (R$):"))
# moeda = input("Converter para (dólar ou euro):").lower()

# if moeda == "dólar":
#     convertido = valor / 5.00
#     print(f"valor  em dólar: US$ {convertido:.2f}")
# elif moeda == "euro":
#     convertido = valor / 5.50
#     print(f"Valor em euro: € {convertido:.2f}")
# else:
#     print("Moeda inválida!")

# exercicio 9
# notas = [9, 6.5, 4, 8, 5.9]

# for nota in notas:
#     if nota >=7:
#         print(f"Nota {nota} Aprovado")
#     elif nota >=5:
#         print(f"Nota {nota}: Recuperação")
#     else:
#         print(f"Nota {nota}: Reprovado")

# exercicio 10
# senha_correta ="12345"
# tentativas = 0

# while tentativas <3:
#     senha = input("Digite a senha:")

#     if senha == senha_correta:
#         print("Acesso permitido!")
#         break
#     else:
#         print("Senha incorreta!")
#         tentativas +=  1
# if tentativas == 3:
#     print("conta bloqueada!")

# # exercicio 11
# num = int(input("Digite um número:"))

# if num % 3 == 0 and num % 5 == 0:
#     print("O número é múltiplo de 3 e 5")
# elif num % 3 == 0:
#     print("O número é múltiplo de 3")
# elif num % 5 == 0:
#     print("O número é múltiplo de 5")
# else:
#     print("O número não é múltiplo de 3 nem de 5")