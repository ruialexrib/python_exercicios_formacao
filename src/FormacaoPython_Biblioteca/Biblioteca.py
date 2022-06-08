from Livro import *
from os.path import exists

class Biblioteca:    

    #ctor
    def __init__(self, nome):
        self.__nome = nome
        self.__listaLivros = []

        file_exists = exists(f"{nome}.txt")
        if file_exists:
            self.__ReadFile()

    def __del__(self):
        self.__WriteFile()

    @property
    def Nome(self):
        return self.__nome
    @Nome.setter
    def Nome(self, value):
        self.__nome = value

    @property
    def Livros(self):
        return self.__listaLivros
    @Livros.setter
    def Livros(self, value):
        self.__listaLivros = value

    def ExisteLivro(self, isbn):
        for livro in self.__listaLivros:
            if livro.Isbn == isbn:
                return True
        return False

    def AdicionaLivro(self, livro):
        if type(livro) is Livro:
            if not self.ExisteLivro(livro.Isbn):
                self.__listaLivros.append(livro)
            else:
                raise NameError(f"O livro com Isbn:{livro.Isbn} já existe")

    def RemoveLivro(self, isbn):
        for livro in self.__listaLivros:
            if livro.Isbn == isbn:
                self.__listaLivros.remove(livro)
    
    def ImprimirLivros(self):
        for livro in self.__listaLivros:
            print ("---")
            livro.Imprimir()


    def __ReadFile(self):
        file = open(f"{self.Nome}.txt", "r")
        for line in file.readlines():
            l = line.split("|")
            livro = Livro(l[0], l[1], l[2], l[3], l[4].replace("\n", ""))
            self.__listaLivros.append(livro)

    def __WriteFile(self):
        file = open(f"{self.Nome}.txt", "w")
        for livro in self.__listaLivros:
            file.write(f"{livro.Isbn}|{livro.Titulo}|{livro.Autor}|{livro.Editora}|{livro.Ano}\n")
        file.close