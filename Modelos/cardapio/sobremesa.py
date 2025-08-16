from Modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        pass    
    
    def formatar_para_cardapio(self) -> str:
        return f'Nome: {self._nome} | Preço: R${self._preco} | Tipo: {self.tipo} |  Tamanho: {self.tamanho} | Descricao: {self.descricao}'    
    