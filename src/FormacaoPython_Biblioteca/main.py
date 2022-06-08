from Biblioteca import *
from Livro import *

def main():

    try:
        bib = Biblioteca("teste")
        operador = 1
        while operador != 0 :
            print ("------------------------")
            print ("---- Menu de Opções ----")
            print ("------------------------")
            print ("- (1) Inserir livro    -")
            print ("- (2) Eliminar livro   -")
            print ("- (3) Listar livros    -")
            print ("------------------------")
            print ("- (0) Terminar         -")
            print ("------------------------")
            operador = int(input("Digite uma opção: "))

            if operador == 1:
                isbn = input(f"Digite o isbn: ")
                titulo = input(f"Digite o titulo: ")
                autor = input(f"Digite o autor: ")
                editora = input(f"Digite a editora: ")
                ano = input(f"Digite o ano: ")
                bib.AdicionaLivro(Livro(isbn, titulo, autor, editora, ano))

            if operador == 2:
                isbn = input(f"Digite o isbn: ")
                bib.RemoveLivro(isbn)

            if operador == 3:
                bib.ImprimirLivros()

    except Exception as e:
        print (f"Ocorreu um erro. Detalhes: {e}")

if __name__ == '__main__':
    main()
