from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato
from Modelos.cardapio.sobremesa import Sobremesa

# instanciado restaurantes
restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

# incluido notas para teste
restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('Rondi',8)
restaurante_praca.receber_avaliacao('Samara',5)

# instanciando comidas
bebida_suco = Bebida('Suco de Melancia',5.0,'Grande')
prato_paozinho = Prato('Paozinho',2.0,'O melhor pao da cidade')
sobremesa1 = Sobremesa('Petit Gateau', 18.0, 'Doce', 'Individual', 'Bolo de chocolate com sorvete')
sobremesa2 = Sobremesa('Torta de Limão', 12.0, 'Torta', 'Fatia', 'Torta cremosa com cobertura de limão')

# aplicar desconto
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

# adicionado itens ao cardapio
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_mexicano.adicionar_no_cardapio(sobremesa1)
restaurante_japones.adicionar_no_cardapio(sobremesa2)

def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio()
    restaurante_japones.exibir_cardapio()
    restaurante_mexicano.exibir_cardapio()

if __name__ == '__main__':
    main()
    