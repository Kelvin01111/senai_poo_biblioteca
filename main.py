from entidades.livro_didatico import LivroDidatico
from entidades.livro_ficcao import LivroFiccao
from entidades.livro_nao_ficcao import LivronaoFiccao


if __name__ == '__main__':
    livro_didatico = LivroDidatico("Código Limpo","Robert C. Martin","464","Eng. Software","Não especificado","Ensino Superior")
    livro_ficcao = LivroFiccao("As Duas Torres","J.R.R. Tolkien","352","Fantasia Épica","Alta Fantasia")
    livro_nao_ficcao = LivronaoFiccao("The Pragmatic Programmer: Your Journey to Mastery","Andrew Hunt e David Thomas","352","Desenvolvimento de Software","Eficiência na Programação")



livro_didatico.informar_detalhes()
print()
livro_ficcao.informar_detalhes()
print()
livro_nao_ficcao.informar_detalhes()
print()