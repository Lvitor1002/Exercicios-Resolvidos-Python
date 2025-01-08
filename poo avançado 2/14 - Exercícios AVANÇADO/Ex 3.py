'''
Sistema de Gestão de Biblioteca
Desenvolva um sistema de gestão de biblioteca que permita aos usuários cadastrar livros, 
realizar empréstimos e devoluções, e consultar informações sobre os livros disponíveis. 
Implemente classes como Book (representando um livro), Library (representando a biblioteca) e User (representando um usuário do sistema).
'''


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                return f"O livro '{book.title}' foi emprestado com sucesso."
        return "Livro não disponível para empréstimo."

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                return f"O livro '{book.title}' foi devolvido com sucesso."
        return "Livro não encontrado ou já devolvido."

# Exemplo de uso:
library = Library()
book1 = Book("Python for Data Science", "Jake VanderPlas", "978-1491912058")
book2 = Book("Deep Learning", "Ian Goodfellow", "978-0262035613")
library.add_book(book1)
library.add_book(book2)
print(library.borrow_book("978-1491912058"))
print(library.return_book("978-1491912058"))
