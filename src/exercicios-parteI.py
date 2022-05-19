# ============================================================
# ex 1
# Desenvolva um programa que pergunte o seu nome e o ano de nascimento e devolva uma mensagem com o nome introduzido e a idade.
# ============================================================

from datetime import date

nome = input("Introduza o nome: ")
ano_nascimento = int(input ("Introduza o ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"Este ano, o {nome} terá {idade} anos")

# ============================================================
# ex 2
# Desenvolver um programa que faça a leitura de um número inteiro e indique se este é um número par ou ímpar.
# ============================================================

num = int(input ("Introduza o numero: "))
resto = num % 2

if (resto == 0):
    print(f"O numero {num} é par")
else:
    print(f"O numero {num} é impar")

# ============================================================
# ex 3a
# Desde a introdução do Calendário Gregoriano, em 1582, determinou-se que um ano é bissexto se for divisível por 4 e 
# não for divisível por 100 ou então se for divisível por 400.
# Desenvolva um programa que determine se um determinado ano é bissexto.
# ============================================================

ano = int(input ("Introduza o ano: "))

if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 400 == 0)):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} é não bissexto")

# ============================================================
# ex 3b
# Desde a introdução do Calendário Gregoriano, em 1582, determinou-se que um ano é bissexto se for divisível por 4 e 
# não for divisível por 100 ou então se for divisível por 400.
# Melhore o programa, verificando se o ano introduzido pertence à era Gregoriana (após 1582). 
# Se não o for, a determinação de ano bissexto não deverá ser efetuada e deverá ser apresentado um aviso ao utilizador.
# ============================================================

ano = int(input ("Introduza o ano: "))

if (ano > 1582):
    if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 400 == 0)):
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} é não bissexto")
else:
    print(f"O ano {ano} está fora da hera gregoriana")

# ============================================================
# ex 4
# Desenvolver um programa que calcule o salário semanal a pagar a um empregado, 
# tendo em atenção que todas as horas que este trabalha para além das 40 horas serão pagas a dobrar. 
# O programa recebe do utilizador os valores de horas trabalhadas e o valor do salário por hora.
# ============================================================

horas_extra = 0
horas_normais = 0

horas_trabalhadas = int(input ("Introduza o numero de horas trabalhadas: "))
salario_hora = float(input ("Introduza o salário hora: "))

if (horas_trabalhadas > 40):
    horas_normais = 40
    horas_extra = horas_trabalhadas - horas_normais
else:
    horas_normais = horas_trabalhadas

salario_semanal = (horas_normais * salario_hora) + (horas_extra * salario_hora * 2)

print(f"O salario semanal, referente a {horas_trabalhadas} horas de trabalho, corresponde a {salario_semanal}€")

# ============================================================
# ex 5
# Desenvolver um programa capaz de ler do teclado um número inteiro, garantindo que esteja entre 10 e 15 
# e que depois mostre o quadrado e o cubo desse número
# ============================================================

correto = False
num = 0

while correto == False:
    num = int(input ("Introduza o numero inteiro entre 10 e 15: "))
    if (num >= 10) and (num <= 15):
        correto = True
    else:
        print("Erro: o numero introduzido não está compreendido entre 10 e 15.")

print(f"O quadrado de {num} é {num ** 2}")
print(f"O cubo de {num} é {num ** 3}")

# ============================================================
# ex 6
# Desenvolver um programa que, calcule a percentagem de números múltiplos de 4, de uma série de números inteiros digitados pelo utilizador. 
# A apresentação do resultado dever ser feita após o utilizador inserir o número zero (não contando este último para o cálculo da percentagem).
# ============================================================

numeros = []
continua = True
contador = 1

while continua == True:
    num = int(input (f"Introduza um numero #{contador}. (zero para terminar): "))
    if (num == 0):
        continua = False
    else:
        contador += 1
        numeros.append(num)     

if (contador - 1 > 0):

    numeros_multiplos = 0

    for i in range(contador - 1):
        if (numeros[i] % 4 == 0):
            numeros_multiplos += 1
            print(f"O numero {numeros[i]}, que se encontra na posição {i} é multiplo de 4")
        else:
            print(f"O numero {numeros[i]}, que se encontra na posição {i} não é multiplo de 4")

    print(f"Num total de {contador - 1} numeros recolhidos, {numeros_multiplos} são multiplos de 4, correspondendo a {numeros_multiplos/(contador - 1) * 100}%")

else:
    print(f"Erro: Não foi introduzido nenhum valor")

# ============================================================
# ex 7
# Desenvolva um programa que faça a leitura de um número positivo menor do que 24
# (garantindo que assim seja) e, em seguida, mostre o quadrado e o cubo de todos os números
# entre 1 e o valor lido, inclusive.
# ============================================================

correto = False

while correto == False:
    num = int(input ("Introduza o numero positivo e menor que 24: "))
    if (num <= 0) or (num >= 24):
        print("Erro: o numero introduzido tem de ser positivo e menor que 24.")
    else:
        correto = True

for i in range (1, num + 1):
    print(f"O quadrado de {i} é {i ** 2}")
    print(f"O cubo de {i} é {i ** 3}")

# ============================================================
# ex 8
# Desenvolver um programa capaz de ler um número inteiro do teclado e que apresente a
# tabuada de multiplicação desse número.
# ============================================================

num = int(input ("Introduza um numero inteiro: "))

for i in range (1,11):
    print(f"{num} x {i} = {num * i}")

# ============================================================
# ex 9a
# Desenvolva um programa capaz de ler 5 números inteiros e no final apresentar a soma
# desses valores.
# ============================================================

soma = 0

for i in range (1, 6):
    num = int(input (f"Introduza um numero inteiro #{i}: "))
    soma = soma + num

print (f"O resultado da soma dos numeros inseridos é {soma}")

# ============================================================
# ex 9b
# Altere o programa para mostrar também a média dos números lidos.
# ============================================================

soma = 0
media = 0

for i in range (1, 6):
    num = int(input (f"Introduza um numero inteiro #{i}: "))
    soma = soma + num

media = soma / 5

print (f"O resultado da soma dos numeros inseridos é {soma}")
print (f"O resultado da média dos numeros inseridos é {media}")

# ============================================================
# ex 10
# Desenvolva um programa capaz de ler três números inteiros e dizer qual dos três é o maior (o
# programa deverá prever a possibilidade de os três números serem iguais).
# ============================================================

maior = 0
contar_iguais = 0

for i in range (1, 4):
    num = int(input (f"Introduza um numero inteiro #{i}: "))
    if (i == 1):
        maior = num
    else:
        if (num > maior):
            maior = num
        elif (num == maior):
            contar_iguais += 1

if (contar_iguais == 2):
    print(f"Os numeros introduzidos são todos iguais")
else:
    print(f"O maior numero introduzido é {maior}")

# ============================================================
# ex 11a
# Desenvolva um jogo em que o primeiro jogador introduz um número secreto, de 1 a 99, e o
# segundo jogador tenta adivinhá-lo.
# Em cada tentativa, o computador deverá dizer se acertou no número ou, caso contrário, se
# o número secreto é maior ou menor que a tentativa feita.
# ============================================================

game_over = False 
correto_secreto = False
num_secreto = 0
num = 0

while correto_secreto == False:
    num_secreto = int(input (f"Introduza um numero secreto inteiro entre 1 e 99: "))
    if (num_secreto) >= 1 and (num_secreto <=99):
        correto_secreto = True
    else:
        print(f"Erro: Tem de introduzir um numero inteiro entre 1 e 99")


while game_over == False:
    correto_tentativa = False

    while correto_tentativa == False:
        num = int(input (f"Introduza uma tentativa de numero inteiro entre 1 e 99: "))
        if (num) >= 1 and (num <=99):
            correto_tentativa = True
        else:
            print(f"Erro: Tem de introduzir um numero inteiro entre 1 e 99")

    if (num > num_secreto):
        print(f"A sua tentiva {num} é maior que o numero secreto")
    elif (num < num_secreto):
        print(f"A sua tentiva {num} é menor que o numero secreto")
    else:
        print(f"Parabéns !! A sua tentiva foi igual ao numero secreto {num_secreto}.")
        game_over = True

print(f"GAME OVER")

# ============================================================
# ex 11b
# Desenvolva um jogo em que o primeiro jogador introduz um número secreto, de 1 a 99, e o
# segundo jogador tenta adivinhá-lo.
# Em cada tentativa, o computador deverá dizer se acertou no número ou, caso contrário, se
# o número secreto é maior ou menor que a tentativa feita.
# Melhore o jogo, indicando no final quantas tentativas foram necessárias para acertar.
# ============================================================

game_over = False 
correto_secreto = False
num_secreto = 0
num = 0
tentativas = 0

while correto_secreto == False:
    num_secreto = int(input (f"Introduza um numero secreto inteiro entre 1 e 99: "))
    if (num_secreto) >= 1 and (num_secreto <=99):
        correto_secreto = True
    else:
        print(f"Erro: Tem de introduzir um numero inteiro entre 1 e 99")


while game_over == False:
    correto_tentativa = False

    while correto_tentativa == False:
        num = int(input (f"Introduza uma tentativa de numero inteiro entre 1 e 99: "))
        if (num) >= 1 and (num <=99):
            correto_tentativa = True
            tentativas += 1
        else:
            print(f"Erro: Tem de introduzir um numero inteiro entre 1 e 99")

    if (num > num_secreto):
        print(f"A sua tentiva {num} é maior que o numero secreto")
    elif (num < num_secreto):
        print(f"A sua tentiva {num} é menor que o numero secreto")
    else:
        print(f"Parabéns !! A sua tentiva foi igual ao numero secreto {num_secreto}. Acertou em {tentativas} tentativas !")
        game_over = True

print(f"GAME OVER")

# ============================================================
# ex 11c
# Desenvolva um jogo em que o primeiro jogador introduz um número secreto, de 1 a 99, e o
# segundo jogador tenta adivinhá-lo.
# Em cada tentativa, o computador deverá dizer se acertou no número ou, caso contrário, se
# o número secreto é maior ou menor que a tentativa feita.
# Melhore o jogo, indicando no final quantas tentativas foram necessárias para acertar.
# Melhore novamente o jogo, dando a indicação “está quente” quando a tentativa feita esteja
# a menos de 5 unidades do número secreto.
# ============================================================

game_over = False 
correto_secreto = False
num_secreto = 0
num = 0
tentativas = 0

while correto_secreto == False:
    num_secreto = int(input (f"Introduza um numero secreto inteiro entre 1 e 99: "))
    if (num_secreto) >= 1 and (num_secreto <=99):
        correto_secreto = True
    else:
        print(f"Erro: Tem de introduzir um numero inteiro entre 1 e 99")


while game_over == False:
    correto_tentativa = False

    while correto_tentativa == False:
        num = int(input (f"Introduza uma tentativa de numero inteiro entre 1 e 99: "))
        if (num) >= 1 and (num <=99):
            correto_tentativa = True
            tentativas += 1
        else:
            print(f"Erro: Tem de introduzir um numero inteiro entre 1 e 99")

    if (abs(num - num_secreto) < 5):
        print(f"Está quente !!!")
    if (num > num_secreto):
        print(f"A sua tentiva {num} é maior que o numero secreto")
    elif (num < num_secreto):
        print(f"A sua tentiva {num} é menor que o numero secreto")
    else:
        print(f"Parabéns !! A sua tentiva foi igual ao numero secreto {num_secreto}. Acertou em {tentativas} tentativas !")
        game_over = True

print(f"GAME OVER")