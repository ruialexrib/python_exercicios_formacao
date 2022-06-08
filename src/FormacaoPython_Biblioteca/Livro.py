class Livro:

    #ctor
    def __init__(self, isbn, titulo, autor, editora, ano):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano

    @property
    def Isbn(self):
        return self.__isbn
    @Isbn.setter
    def Isbn(self, valor):
        self.__isbn = valor

    @property
    def Titulo(self):
        return self.__titulo
    @Titulo.setter
    def Titulo(self, valor):
        self.__titulo = valor

    @property
    def Autor(self):
        return self.__autor
    @Autor.setter
    def Autor(self, valor):
        self.__autor = valor

    @property
    def Editora(self):
        return self.__editora
    @Editora.setter
    def Editora(self, valor):
        self.__editora = valor

    @property
    def Ano(self):
        return self.__ano
    @Ano.setter
    def Ano(self, valor):
        self.__ano = valor

    def Imprimir(self):
            print (f"Isbn: {self.Isbn}")
            print (f"Titulo: {self.Titulo}")
            print (f"Autor: {self.Autor}")
            print (f"Editora: {self.Editora}")
            print (f"Ano: {self.Ano}")