import tkinter as tk
from tkinter import messagebox





class Biblioteca:

    __morada = ""
    __listaLivros = []

    # ctor
    def __init__(self, morada):
        if morada is not None and morada != "":
            self.setMorada(morada)
        else:
            raise ValueError("morada is null or empty")
    
    # setters and getters
    def getMorada(self):
        return self.__morada
    def setMorada (self, value):
        self.__morada = value

    # public methods
    def addBook(self, book):
        self.__listaLivros.append(book)

    def searchBook(self, isbn):
        for book in self.__listaLivros:
            if book.isbn == isbn:
                return book
            return False

    def getBooks(self):
        return self.__listaLivros



class Book:

    isnb = ""
    titulo = ""
    autor = ""
    editora = ""
    ano = ""
    
    def __init__(self, isbn, titulo, autor, editora, ano):
        self.isnb = isbn
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano





class BibliotecaView:

    # membros
    __window = None
    __title = None

    __model = None

    __txtMorada = None
    __moradaText = None

    __lblMorada = None
    __lblCount = None
    __countText = None

    __btnAdicionar = None
    __btnListar = None
    __btnCancelar = None

    # ctor
    def __init__(self, title, morada):
        self.__title = title
        self.__morada = morada
        self.__model = Biblioteca(morada)
        # inicia o form        
        self.__start_form()   

    #eventos
    def __cmdAdicionar_click(self):
        b = Book("","","","","")
        bookview = BookView("Novo livro", b)
        print(bookview.getModel())
        self.__model.addBook(bookview.getModel())        
        self.__countText.set( f"Nº de livros: {len(self.__model.getBooks())}")

    def __cmdListar_click(self):
        for book in self.__model.getBooks():
            messagebox.showinfo(title=None, message=f"Livro titulo: {book.titulo}" )
    
    def __cmdCancelar_click(self):
        self.__close_form()

    # métodos privados
    def __close_form(self):
        self.__window.destroy()

    def __start_form(self):

        # root window
        self.__window = tk.Tk()
        self.__window.geometry("400x150")  
        self.__window.title(self.__title)

      # vars
        self.__moradaText = tk.StringVar()
        self.__moradaText.set(self.__morada)
        self.__countText = tk.StringVar()
        self.__countText.set( f"Nº de livros: {len(self.__model.getBooks())}")

        # labels
        self.__lblMorada = tk.Label(self.__window, text = "Morada")
        self.__lblCount = tk.Label(self.__window, textvariable = self.__countText)

        # textbox
        self.__txtMorada = tk.Entry(self.__window, textvariable = self.__moradaText)

        # buttons
        self.__btnAdicionar = tk.Button(self.__window, text="Adicionar", command = self.__cmdAdicionar_click)
        self.__btnListar = tk.Button(self.__window, text="Listar", command = self.__cmdListar_click)
        self.__btnCancelar = tk.Button(self.__window, text="Cancelar", command = self.__cmdCancelar_click)

        # grid
        self.__lblMorada.grid(row = 1, column = 0)
        self.__txtMorada.grid(row = 1, column = 1, ipadx="100")

        self.__btnAdicionar.grid(row = 2, column = 1)
        self.__btnListar.grid(row = 3, column = 1)
        self.__btnCancelar.grid(row = 4, column = 1)

        self.__lblCount.grid(row = 5, column = 0)

        self.__window.mainloop()   





class BookView:

    # membros
    __window = None
    __title = None
    __model = None
    __isEdit = False

    __lblIsbn = None
    __lblTitulo = None
    __lblAutor = None
    __lblEditora = None
    __lblAno = None

    __txtIsbn = None
    __isbnText = None
    __txtTitulo = None
    __tituloText = None
    __txtAutor = None
    __autorText = None
    __txtEditora = None
    __editoraText = None
    __txtAno = None
    __anoText = None

    __isbnText = None

    __btnGravar = None

    # ctor
    def __init__(self, title, model = None):
        self.setModel(model)
        self.__title = title
        self.__isEdit = model is not None    
        # inicia o form        
        self.__start_form()

    # eventos
    def __cmdGravar_click(self):
        isbn = self.__txtIsbn.get()
        titulo = self.__txtTitulo.get()
        autor = self.__txtAutor.get()
        editora = self.__txtEditora.get()
        ano = self.__txtAno.get()
        m = Book(isbn, titulo, autor, editora, ano)
        self.setModel(m)
        self.__close_form()

    def __cmdCancelar_click(self):
        self.__close_form()

    # métodos privados
    def __close_form(self):
        self.__window.quit()
        self.__window.destroy()

    def __start_form(self):

        # root window
        self.__window = tk.Tk()
        self.__window.geometry("400x150")  
        self.__window.title(self.__title)

        # vars
        self.__isbnText = tk.StringVar()
        self.__tituloText = tk.StringVar()
        self.__autorText = tk.StringVar()
        self.__editoraText = tk.StringVar()
        self.__anoText = tk.StringVar()

        # labels
        self.__lblIsbn = tk.Label(self.__window, text = "ISBN")
        self.__lblTitulo = tk.Label(self.__window, text = "Titulo")
        self.__lblAutor = tk.Label(self.__window, text = "Autor")
        self.__lblEditora = tk.Label(self.__window, text = "Editora")
        self.__lblAno = tk.Label(self.__window, text = "Ano")

        # textbox

        if self.__isEdit:
            self.__isbnText.set(self.__model.isnb)
            self.__tituloText.set(self.__model.titulo)
            self.__autorText.set(self.__model.autor)
            self.__editoraText.set(self.__model.editora)
            self.__anoText.set(self.__model.ano)

        self.__txtIsbn = tk.Entry(self.__window, textvariable = self.__isbnText)
        self.__txtTitulo = tk.Entry(self.__window, textvariable = self.__tituloText)
        self.__txtAutor = tk.Entry(self.__window, textvariable = self.__autorText)
        self.__txtEditora = tk.Entry(self.__window, textvariable = self.__editoraText)
        self.__txtAno = tk.Entry(self.__window, textvariable = self.__anoText)
        
        # buttons
        self.__btnGravar = tk.Button(self.__window, text="Gravar", command = self.__cmdGravar_click)
        self.__btnCancelar = tk.Button(self.__window, text="Cancelar", command = self.__cmdCancelar_click)

        # grid
        self.__lblIsbn.grid(row = 1, column = 0)
        self.__lblTitulo.grid(row = 2, column = 0)
        self.__lblAutor.grid(row = 3, column = 0)
        self.__lblEditora.grid(row = 4, column = 0)
        self.__lblAno.grid(row = 5, column = 0)

        self.__txtIsbn.grid(row = 1, column = 1, ipadx="100")
        self.__txtTitulo.grid(row = 2, column = 1, ipadx="100")
        self.__txtAutor.grid(row = 3, column = 1, ipadx="100")
        self.__txtEditora.grid(row = 4, column = 1, ipadx="100")
        self.__txtAno.grid(row = 5, column = 1, ipadx="100")

        self.__btnGravar.grid(row = 6, column = 1)
        self.__btnCancelar.grid(row = 7, column = 1)

        self.__window.mainloop()       

    # getters and setters
    def getModel(self):
        return self.__model
    def setModel(self, model):
        if model is not Book:
            self.__model = model
        else:
            raise ValueError("model is not a Book")





bibl = BibliotecaView("Detalhes da Biblioteca", "Biblioteca de teste")