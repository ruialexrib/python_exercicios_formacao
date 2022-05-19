# ============================================================
# ex 1
# Desenvolva um algoritmo que mostre os números inteiros de 1 a 20.
# ============================================================

for i in range(1,21):
    print(i)

# ============================================================
# ex 2
# Altere o algoritmo anterior de forma a mostrar os nú meros inteiros de 25 a 50.
# ============================================================

limite_inferior = 25
limite_superior = 50

for i in range(limite_inferior, limite_superior + 1):
    print(i)

# ============================================================
# ex 3
# Altere o algoritmo anterior para que o intervalo de números a mostrar seja fornecido pelo
# utilizador.
# ============================================================

limite_inferior = int(input ("Introduza o limite inferior: "))
limite_superior = int(input ("Introduza o limite superior: "))

for i in range(limite_inferior, limite_superior + 1):
    print(i)

# ============================================================
# ex 4
# Desenvolver um algoritmo que leia um número inteiro e que apresente a tabuada de
# multiplicação desse número.
# ============================================================

num = int(input ("Introduza um numero inteiro: "))

for i in range (1,11):
    print(f"{num} x {i} = {num * i}")

# ============================================================
# ex 5
# Desenvolver um algoritmo capaz de ler 7 números inteiros e no final apresentar qual o
# valor máximo e o valor mínimo introduzidos. Acrescente ao algoritmo a funcionalidade
# que lhe permita apresentar a média dos valores lidos.
# ============================================================

max = 0
min = 0
soma = 0
media = 0

for i in range (1,8):
    num = int(input (f"Introduza um numero inteiro #{i}: "))

    if i == 1:
        max = num
        min = num
    else:
        if num > max:
            max = num
        elif num < min:
            min = num
    
    soma = soma + num

media = soma / 7

print(f"O valor máximo introduzido foi {max}.")
print(f"O valor minimo introduzido foi {min}.")
print(f"A média dos valores introduzidos doi de {media}.")

# ============================================================
# ex 6
# Desenvolver um algoritmo que leia dois números inteiros (N1 e N2) e que mostre todos
# os números entre N1 e N2 que sejam múltiplos de 4.
# ============================================================

n1 = int(input (f"Introduza um numero inteiro para N1: "))
n2 = int(input (f"Introduza um numero inteiro para N2: "))

for i in range(n1 + 1, n2):
    if i % 4 == 0:
        print(f"O numero {i} é multiplo de 4")

# ============================================================
# ex 7
# Desenvolver um algoritmo que calcule o somatório de 1 até um número N, sendo N um
# valor fornecido pelo utilizador.
# ============================================================

soma = 0

n = int(input (f"Introduza um numero inteiro para N: "))

for i in range (1, n + 1):
    soma = soma + i

print(f"O somatório de 1 até {n} é igual a {soma}")

# ============================================================
# ex 8
# Desenvolver um algoritmo que faça a leitura de um n úmero inteiro positivo e que, para
# esse número, mostre todos os seus divisores.
# ============================================================

n = int(input (f"Introduza um numero inteiro positivo para N: "))

for i in range (n, 0, -1):
    print(f"Divisores de {i}:")
    for j in range (i , 0, -1):
        if i % j == 0:
            print (j)

# ============================================================
# ex 9
# Desenvolva um algoritmo que faça a leitura de um número inteiro positivo maior ou igual
# a dois e que diga se o número fornecido é ou não um número primo (um número primo é
# aque le que só tem dois divisores: ele próprio e o número 1).
# ============================================================

correto = False
nr_divisores = 0

while correto == False:
    num = int(input (f"Introduza um numero inteiro positivo maior ou igual a 2: "))
    if (num >= 2):
        correto = True
    else:
        print(f"Erro: O valor introduzido tem de ser inteiro positivo maior ou igual a 2.")

for j in range (num, 0, -1):

    nr_divisores = 0

    for i in range (j, 0, -1 ):
        if j % i == 0:
            nr_divisores += 1

    if nr_divisores == 2:
        print(f"O numero {j} é primo")

# ============================================================
# ex 10
# Elabore um algoritmo que, dada uma sequência de números inteiros terminada por 0
# (zero), calcule a percentagem de valores introduzidos superiores a 10.
# Nota: O zero não deverá contar para efeitos de
# cálculo!
# ============================================================

numeros = []
continua = True
contador = 1
contador_nrs_superiores = 0

while continua == True:
    num = int(input (f"Introduza um numero #{contador}. (zero para terminar): "))
    if (num == 0):
        continua = False
    else:
        contador += 1
        numeros.append(num)    

for i in range (0, contador - 1):
    print (i)
    if numeros[i] > 10:
        contador_nrs_superiores += 1

print(f"A percentagem de numeros introduzidos, superiores a 10 é igual a {contador_nrs_superiores/(contador - 1) * 100}%")

# ============================================================
# ex 11
# Desenvolver um algoritmo capaz de calcular o valor máximo e o valor mínimo de uma
# série de números inteiros positivos lidos do teclado e cuja marca de fim é 1.
# ============================================================

numeros = []
contador = 1
continua = True
max = 0
min = 0

while continua == True:
    num = int(input (f"Introduza um numero #{contador}. (-1 para terminar): "))
    if (num == -1):
        continua = False
    else:
        if num <= 0:
            print(f"O numero introduzido tem de ser inteiro positivo.")
        else:
            contador += 1
            numeros.append(num)   

for i in range (0,contador - 1):
    if i == 0:
        max = numeros[i]
        min = numeros[i]
    else:
        if numeros[i] > max:
            max = numeros[i]
        elif numeros[i] < min:
            min = numeros[i]

print(f"O minimo dos valores introduzidos é {min}")
print(f"O máximo dos valores introduzidos é {max}")

# ============================================================
# ex 12
# Desenvolver um algoritmo que leia um número inteiro no intervalo [10, 99] e diga se o
# correspondente invertido desse número é múltiplo de 7.
# Exemplo: valor lido 12, invertido fica 21, 21 é múltiplo de 7.
# ============================================================

correto = False
while correto == False:
    num = int(input (f"Introduza um numero inteiro entre 10 e 99: "))
    if num >= 10 and num <= 99:
        correto = True
    else:
        print(f"Erro: O valor introduzido tem de ser inteiro entre 10 e 99")

numero_invertido = int(str(num)[::-1])

if numero_invertido % 7 == 0:
    print(f"O numero invertido {numero_invertido} é multiplo de 7")
else:
    print(f"O numero invertido {numero_invertido} não é multiplo de 7")



