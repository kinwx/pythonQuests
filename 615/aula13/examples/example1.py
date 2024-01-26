# ASSOCIAÇÃO
class Autor:
    def __init__(self, nome: str, idade: int, nacionalidade: str) -> None:
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo: str, autor: Autor, genero: str, qtde_pag: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qtde_pag =  qtde_pag

autor1 = Autor(nome="joazin", idade=52, nacionalidade="Brasileiro")
livro1 = Livro(titulo="Historias do joao", autor=autor1, genero="Drama", qtde_pag=122)

print(livro1.titulo)
print(livro1.autor.nacionalidade)