from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato

# instanciado restaurantes
restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

# incluido notas para teste
restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('Rondi',8)
restaurante_praca.receber_avaliacao('Samara',5)

# instanciando bebidas
bebida_suco = Bebida('Suco de Melancia',5.0,'Grande')
prato_paozinho = Prato('Paozinho',2.0,'O melhor pao da cidade')





def main():
    Restaurante.listar_restaurantes()
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()