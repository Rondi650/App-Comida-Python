# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from livros import Livro


# Crie duas instâncias da classe Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1935)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1979)

# imprima essas instâncias
print(livro1)
print(livro2)

#  Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
livro3 = Livro("Clean Code", "Robert C. Martin", 2003)

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
print(livro3.emprestar())

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico. 
livro4 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1935)

print(Livro.verificar_disponibilidade(1935))




