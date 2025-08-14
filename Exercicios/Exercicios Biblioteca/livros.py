
# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []
    
    def __init__(self, titulo, autor,  ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro.     
    def __str__(self):
        return f'{self._titulo} por {self._autor}, ano {self._ano_publicacao}, status: {self.ativo}'
    
    @property
    def ativo(self):
        return f'Disponivel' if self._disponivel else 'Nao disponivel'
    
# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.    
    def emprestar(self):
        self._disponivel = False
        
        
# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.  
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [str(livro) for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel] # <-- LIST COMPREHENSION
        return "\n".join(livros_disponiveis)
    
    '''
    ESSE FOR E O MODO TRADICIONAL DO LIST COMPREHENSION:
    
    resultado = []
    for livro in Livro.livros:
        if livro._ano_publicacao == ano and livro._disponivel:
            resultado.append(livro)
    return resultado
    
    '''