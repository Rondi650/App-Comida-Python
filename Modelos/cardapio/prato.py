from Modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
        
    def formatar_para_cardapio(self) -> str:
        return f'Nome: {self._nome} | Preço: R${self._preco} | Descrição: {self.descricao}'