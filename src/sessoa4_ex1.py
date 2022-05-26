# ============================================================
#
# 1. Implemente um programa que faça sucessivas leituras de nomes completos de pessoas 
# (introduzidos pelo utilizador) até que o utilizador decida inserir uma linha em branco/vazia. 
# Os vários nomes inseridos # deverão ser armazenados num ficheiro com o nome pessoas.txt, 
# com um nome completo por linha.
# a) Desenvolva uma função que mostre o conteúdo do ficheiro na consola.
# b) Desenvolva uma função que devolva quantos nomes completos existem no ficheiro
# c) Desenvolva uma função que, dado um nome próprio fornecido pelo utilizador, 
# pesquise os nomes completos existentes no ficheiro e que mostre todos aqueles que 
# comecem pelo nome próprio fornecido.
# d) Desenvolva uma função que coloque numa lista todos os nomes existentes no ficheiro. 
# De seguida, mostre o conteúdo da lista que definiu de forma a verificar que tudo correu bem.
# e) Modifique as funções desenvolvidas para que façam tratamento de exceções. 
# Por exemplo, garantindo que quando tenta abrir um ficheiro não existente 
# o programa não termine repentinamente, com um erro, 
# mas antes que mostre uma mensagem elucidativa ao utilizador.
#
# ============================================================
#
# 2. Crie um ficheiro de texto com o nome texto.txt. 
# Escreva nesse ficheiro um qualquer conteúdo com um número de 
# linhas entre 20 a 30 (Pode ser a cópia de um texto qualquer).
# a) Implemente uma função que verifique se uma dada palavra, fornecida pelo utilizador, 
# aparece no referido texto.
# b) Implemente uma função capaz de retornar o número de linhas em que uma dada palavra, 
# fornecida pelo utilizador, aparece no referido texto.
#
# ============================================================
#
# 3. Com um editor de texto crie um ficheiro com o nome citacoes.txt. 
# Nesse ficheiro coloque algumas frases/citações/pensamentos, uma por parágrafo. 
# Crie um programa capaz de mostrar uma das frases, aleatoriamente, de cada vez que é executado.
#
# ============================================================

def RecolhaNomes(nomeFicheiro):
    try:
        termina = False
        contador = 0
        file = open(nomeFicheiro,'w')
        while(termina != True):
            contador += 1
            nome = input (f"Introduza o nome completo #{contador} (enter para terminar): ")
            if nome == "":
                termina = True
            else:
                file.write(f"{nome} \n")        
        file.close()
    except Exception as e:
        print(e)

def MostraConteudo(nomeFicheiro):
    try:
        file = open(nomeFicheiro,'r')
        for i in file:
            print (i)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def ContaNomes(nomeFicheiro):
    try:
        contador = 0
        file = open(nomeFicheiro,'r')
        for i in file:
            contador += 1
        return contador
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def PesquisaNome(nomeFicheiro, nome):
    try:
        file = open(nomeFicheiro,'r')
        for i in file:
            if  i.startswith(nome):
                print (i)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def InsereEmLista(nomeFicheiro):
    try:
        lista = []
        file = open(nomeFicheiro,'r')
        for i in file:
            lista.append(i)
        print(lista)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def IniciaPrograma(nomeficheiro):
    print("Menu:")
    print("1 - Recolher nomes")
    print("2 - Mostrar conteudo")
    print("3 - Contar nomes")
    print("4 - Pesquisar nomes")
    print("5 - Transformar em lista")
    print("0 - Terminar")
    termina = False
    while(termina == False):
        opcao = int(input (f"Escolha a opção (1, 2, 3, 4, 5 - 0 para terminar):"))
        if opcao == 0:
            termina = True
        elif opcao == 1:
            RecolhaNomes(nomeficheiro)
        elif opcao == 2:
            MostraConteudo(nomeficheiro)  
        elif opcao == 3:
            print(ContaNomes(nomeficheiro))
        elif opcao == 4:
            nome = input (f"Indique o nome a pesquisar:")
            PesquisaNome(nomeficheiro, nome)
        elif opcao == 5:
            InsereEmLista(nomeficheiro)
        else:
            print ("Erro: Opção inválida.")
    print("Programa terminado.")

IniciaPrograma("pessoas.txt")