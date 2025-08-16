from Modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
        
    def formatar_para_cardapio(self) -> str:
        return f'Nome: {self._nome} | Preço: R${self._preco} | Tamanho: {self.tamanho}'