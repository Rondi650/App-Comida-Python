from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()