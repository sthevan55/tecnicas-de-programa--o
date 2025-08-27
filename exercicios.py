#exercicio 1
#for i in range (1,11):
#    print(i)

#exercicio 2
#numero = int(input("digite um numero para ver a tabuada"))
#print(f"tabuada do numero {numero}")
#for i in range(1,11):
#    resultado = numero * i
#    print(f"{numero} x {i} = {resultado}")

#exercicio 3
#contador = 10
#while contador >= 1:
#    print(contador)
#    contador -= 1
#print("fogo!!!")

#exercicio 4
#soma= 0
#for i in range(5):
#    num = int(input(f"digite o {i+1} numero:"))
#    soma += num   
#print(f"o resultado dos numeros é: {soma}")

#exercicio 5
#zcontador = 0
#while True:
#    nome = input("digite um nome (digite fim para encerrar o programa:)")
#    if nome == "fim":
#        break
#    contador += 1
#print("o programa foi encerrado")
#print(f"a quantidade de nomes foi: {contador}")

# nivel intermediario exercicio 1
#quantidade = int(input("quantas notas vode deseja inserir? "))
#soma = 0
#for i in range(1 , quantidade + 1):
#    nota = float(input(f"digite a nuta {i}: "))
#    soma += nota
#media = soma / quantidade
#print(f"a media das {quantidade} notas é: {media:.2f}")

#exercicio 2
#senha = input("digite a senha")
#while senha != "python123":
#    print("senha incorreta, digite novamente")
#    senha = input("digite a senha:")
#print("acesso liberado!")

#exercicio 3
# palavra = input("digite uma palavra:")
# vogais = "aeiouAEIOU"
# qtd_vogais = 0
# qtd_consoantes = 0
# for letra in palavra:
#     if letra.isalpha():
#          if letra in vogais:
#               qtd_vogais += 1       
# else: qtd_consoantes += 1
# print(f"quantidade de vogais: {qtd_vogais}")
# print(f"quantidade de consoantes: {qtd_consoantes}")

#exercicio 4
#for numero in range(1, 21):
#    if numero % 2 == 0:
#        print(f"{numero} é par")
#    else:
#        print(f"{numero} é impar")

#nivel avançado 1
# saldo = 1000.0
# while True:
#     print("\n=== MENU CAIXA ELETRONICO ===")
#     print("1 - ver saldo")
#     print("2 - sacar")
#     print("3-depositar")
#     print("4 - sair")

#     opção = input("escolha uma opção:")
#     if opção == "1":
#         print(f"seu saldo atual é: R$ {saldo:.2f}")

#     elif opção == "2":
#         valor = float(input("digite o valor para saque:"))
#         if valor <= saldo:
#             saldo -= valor
#             print(f"saque realizado com sucesso! novo saldo: R$ {saldo:.2f}")
#         else:
#             print("saldo insuficiente!")

#     elif opção   == "3":
#         valor = float(input("digite o valor depositado:"))
#         saldo += valor
#         print(f"deposito realizado! Novo saldo R$ {saldo:.2f}")

#     elif opção == "4":
#         print("saindo... obrigado por usar o caixa eletônico!")
#         break

#     else: 
#         print("opçao invalida, tente novamente.")      

