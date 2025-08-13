def exercicios_um_classe():
    
    class Restaurante():
        nome = ''
        categoria = ''
        ativo = False
        
    """RESTAURANTE PRACA"""   
    restaurante_praca = Restaurante()
    restaurante_praca.nome = 'praca'
# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
    restaurante_praca.categoria = 'Italiana'
    
# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
    nome_do_restaurante = restaurante_praca.nome
    
# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
    if restaurante_praca.ativo:
        print('O restaurante está ativo.')
    else:
        print('O restaurante está inativo.')
        
# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
    categoria = Restaurante.categoria
    
# Altere o valor do atributo nome para 'Bistrô'.
    restaurante_praca.nome = 'Bistro'
    
# Imprima no console o nome e a categoria da instância restaurante_praca.
    print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')


    '''RESTAURANTE PIZZA'''
    
# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
    restaurante_pizza = Restaurante()
    restaurante_pizza.nome = 'Pizza Place'
    restaurante_pizza.categoria = 'Fast Food'
    
# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
    if(restaurante_pizza.categoria == 'Fast Food'):
        print('Categoria Fast Food')
    else:
        print('Nao e Fast Food')
        
# Mude o estado da instância restaurante_pizza para ativo.
    restaurante_pizza.ativo = True
    
def exercicio_classe_musica():

    class Musica:
        musicas = []
        
        def __init__(self,nome, artista, duracao = 0):
            self.nome = nome
            self.artista = artista
            self.duracao = duracao    
            Musica.musicas.append(self)
            
        def listar_musicas():
            print(f'{'MUSICA'.ljust(20)} | {'ARTISTA'.ljust(20)} | {'DURACAO'}')
            print('-' * 60)
            for musica in Musica.musicas:
                print(f'{musica.nome.ljust(20)} | {musica.artista.ljust(20)} | {musica.duracao}') 
            
    musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
    musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
    musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

    Musica.listar_musicas()

def exercicio_classe_carro():
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
    class Carro:
        carros = []
        
        def __init__(self, modelo, cor, ano = 0):
            self.modelo = modelo
            self.cor = cor
            self.ano = ano
            Carro.carros.append(self)
            print(Carro.carros)
            
        def __str__(self):
            return f'{self.modelo},{self.cor},{self.ano}'
        
        def listar_carros():
            for carro in Carro.carros:
                print(f'{carro.modelo} | {carro.cor} | {carro.ano}')


    Uno = Carro('Uno','prata',2005)
    Ka = Carro('Ford KA', 'Azul Marinho',2008)
    Opalla = Carro('Opalla','Preto', 1989)

    print(Uno)
    print(Ka)
    print(Opalla)

    Carro.listar_carros()

def exercicio_classes_restaurantes():
# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    class Restaurante:
        bares = []
        def __init__(self,nome,categoria, ativo = False, ano_abertura = 0, faturamento = 0):
            self.nome = nome
            self.categoria = categoria
            self.ativo = ativo
            self.ano_abertura = ano_abertura
            self.faturamento = faturamento
            Restaurante.bares.append(self)
            
        def __str__(self):
           return f'{self.nome} | {self.categoria} | {self.ativo} | {self.ano_abertura} | {self.faturamento}'
            
        def listar_bares():
            for bar in Restaurante.bares:
                print(f'{bar.nome} , {bar.categoria} , {bar.ativo}, {bar.ano_abertura}, {bar.faturamento}')
                      
    Jackan = Restaurante('Jackan','Italiana',True,2005,5000)
    Rondi_bar = Restaurante('Rondi_bar','Cerveja',False,2014,4500)
    Samara_bar = Restaurante('Samara_bar','Miojo',True,2015,5500)
    
    Rondi_bar.ativo = True
    Restaurante.listar_bares()
    
    print(Jackan)
    print(Rondi_bar)
    print(Samara_bar)
    
    print(Rondi_bar.ativo)

def exercicio_classes_cliente():
# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
    class Cliente:
        def __init__(self, nome='', idade=0, email='', telefone=''):
            self.nome = nome
            self.idade = idade
            self.email = email
            self.telefone = telefone

    # Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
    cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
    cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
    cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')
        
def atributos_de_classe_e_instacia():
    class Cliente:
        # ATRIBUTO DE CLASSE
        desconto_padrao = 0.05  # 5% para todos os clientes

        def __init__(self, nome, saldo):
            # ATRIBUTOS DE INSTÂNCIA
            self.nome = nome
            self.saldo = saldo

        def aplicar_desconto(self):
            desconto = self.saldo * Cliente.desconto_padrao
            self.saldo -= desconto
            print(f"{self.nome} recebeu desconto de R${desconto:.2f}. Saldo final: R${self.saldo:.2f}")


    # Criando instâncias
    cliente1 = Cliente("João", 1000)
    cliente2 = Cliente("Maria", 2000)

    # Usando o método (ambos usam o mesmo desconto da classe)
    cliente1.aplicar_desconto()
    cliente2.aplicar_desconto()

    # Alterando o atributo de classe (afeta todos)
    Cliente.desconto_padrao = 0.10  # agora é 10% para todos

    print("\nApós mudar o desconto padrão:")
    cliente1.aplicar_desconto()
    cliente2.aplicar_desconto()

    # Alterando só o desconto do cliente1 (vira atributo de instância)
    cliente1.desconto_padrao = 0.20  # 20% apenas para João

    print("\nApós mudar só o João:")
    cliente1.aplicar_desconto()  # João usa 20%
    cliente2.aplicar_desconto()  # Maria continua usando 10%
 
def contador_exc():
    class Contador:
        '''
        Classe que representa um contador.
        A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
        '''
    #A classe Contador tem um método de instância incrementar que aumenta o valor do contador e um método __str__ para fornecer uma representação em string da instância.
        contador_global = 0

        def __init__(self):
            self.valor = 0

        def __str__(self):
            return f'Contador: {self.valor}'

        def incrementar(self):
            self.valor += 1

        @classmethod
        def zerar_contador_global(cls):
            cls.contador_global = 0
            return 'Contador global foi zerado.'
        
    c1 = Contador()
    c2 = Contador()

    c1.incrementar()
    print(c1)  # Contador: 1
    print(c2)  # Contador: 0

    Contador.contador_global = 10
    print(Contador.contador_global)  # 10

    Contador.zerar_contador_global()
    print(Contador.contador_global)  # 0

def exemplo_classe_livro():    
    class Livro:
        def __init__(self, titulo='', autor='', paginas=0):
            self.titulo = titulo
            self.autor = autor
            self.paginas = paginas

        def __str__(self):
            return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

        @property
        def titulo_autor(self):
            return f'{self.titulo} por {self.autor}'

        def aumentar_paginas(self, quantidade):
            self.paginas += quantidade
            
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1178)
    livro2 = Livro("Dom Casmurro", "Machado de Assis", 256)
    livro3 = Livro("Clean Code", "Robert C. Martin", 464)

    print(livro1)
    print(livro2)
    Livro.aumentar_paginas(livro1,50)
    livro2.aumentar_paginas(200)
    print(livro1)
    print(livro2)
    print(livro3.titulo_autor)

def exercicio_property_incremento_classe():
# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
    class Pessoa:
        def __init__(self, nome='', idade=0, profissao=''):
            self.nome = nome
            self.idade = idade
            self.profissao = profissao
            
        def __str__(self):
            return f'{self.nome}, {self.idade} anos, {self.profissao}'  
        
        @property
        def saudacao(self):
            if self.profissao:
                return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
            else:
                return f'Olá, sou {self.nome}!'
        
        def aniversario(self):
            self.idade += 1
            
    # Criando 3 instâncias da classe Pessoa
    pessoa1 = Pessoa(nome='Alice', profissao='Engenheira', idade=25 )
    pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
    pessoa3 = Pessoa(nome='Jaque', idade=22)

    # Imprimindo informações iniciais
    print("Informações Iniciais:")
    print(pessoa1)
    print(pessoa2)
    print(pessoa3)
    print()

    # Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
    pessoa1.aniversario()
    pessoa3.aniversario()

    # Imprimindo informações após aniversário
    print("Informações após aniversário:")
    print(pessoa1)
    print(pessoa3)
    print()

    # Utilizando o método de classe saudacao para exibir mensagens personalizadas
    print(pessoa1.saudacao)
    print(pessoa2.saudacao)
    print(pessoa3.saudacao)

def exercicio_classe_completo_conta_bancaria():
# 1 Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
# 2 Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
# 3 Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
# 4 Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
# 5 Crie uma instância da classe e imprima o valor da propriedade titular.
# 6 Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
# 7 Crie um método de classe para a conta ClienteBanco.
    class ContaBancaria:
        pass
