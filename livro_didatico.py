from entidades.livro import Livro

class LivroDidatico(Livro):
    def __init__(self, titulo, autor, num_paginas, disciplina, ano_escolar, nivel_ensino):
        super().__init__(titulo, autor, num_paginas)
        self.__disciplina = disciplina
        self.__ano_escolar = ano_escolar
        self.__nivel_ensino = nivel_ensino

    def informar_detalhes(self):
        super().informar_detalhes()
        print(f"Disciplina: {self.__disciplina}")
        print(f"Ano escolar: {self.__ano_escolar}")
        print(f"Nível de Ensino{self.__nivel_ensino}")