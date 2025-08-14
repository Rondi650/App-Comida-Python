from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')


restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('Rondi',8)
restaurante_praca.receber_avaliacao('Samara',5)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()