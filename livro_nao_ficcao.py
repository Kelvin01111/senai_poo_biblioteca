
from entidades.livro import Livro

class LivronaoFiccao(Livro):


    def __init__(self,titulo, autor, num_paginas, tema, topico):
        super().__init__(titulo, autor, num_paginas)
        self.__tema = tema
        self.__topico = topico

    def informar_detalhes(self):
        super().informar_detalhes()
        print(f"Tema: {self.__tema}")
        print(f"Tópico: {self.__topico}")


