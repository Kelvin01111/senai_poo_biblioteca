from entidades.livro import Livro


class LivroFiccao(Livro):

    def __init__(self,titulo, autor, num_paginas, genero, subgenero):
        super().__init__(titulo, autor, num_paginas)
        self.__genero = genero
        self.__subgenero = subgenero

    def informar_detalhes(self):
        super().informar_detalhes()
        print(f"Genero: {self.__genero}")
        print(f"Subgênero: {self.__subgenero}")

