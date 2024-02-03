class Livro:
    def __init__(self,id: int, titulo: str, autor: str) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = "Disponível"


class Membro:
    def __init__(self, membroId: int, nome: str) -> None:
        self.id = membroId
        self.nome = nome
        self.historico = []

    def attHistorico(self, livro: Livro):
        self.historico.append(livro)


class Biblioteca:
    def __init__(self) -> None:
        self.catalogo = [
            Livro(id=1, titulo="1984", autor="George Orwell"),
            Livro(id=2, titulo="Cem Anos de Solidão", autor="Gabriel García Márquez"),
            Livro(id=3, titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien"),
            Livro(id=4, titulo="Crime e Castigo", autor="Fiódor Dostoiévski"),
            Livro(id=5, titulo="Orgulho e Preconceito", autor="Jane Austen"),
            Livro(id=6, titulo="O Grande Gatsby", autor="F. Scott Fitzgerald"),
            Livro(id=7, titulo="O Pequeno Príncipe", autor="Antoine de Saint-Exupéry"),
            Livro(id=8, titulo="Dom Quixote", autor="Miguel de Cervantes"),
            Livro(id=9, titulo="A Revolução dos Bichos", autor="George Orwell"),
            Livro(id=10, titulo="O Apanhador no Campo de Centeio", autor="J.D. Salinger"),
        ]
        self.registroMembros = []
        self.historicoDeDevolucao = []

    def emprestimo(self, livro: Livro):
        for book in self.catalogo:
            if(book == livro):
                book.status = "Indiponível"

    def devolucao(self, livro: Livro, quemDevolveu: str):
        for book in self.catalogo:
            if(book == livro):
                book.status = "Disponível"
                self.historicoDeDevolucao.append({"quemDevolveu": quemDevolveu, "livro": livro})


    def pesquisaDeLivros(self, busca: str):
        if(busca.isdecimal()):
            for livro in self.catalogo:
                if(livro.id == int(busca)):
                    return livro

        livrosPorTitulo = []
        for livro in self.catalogo:
            if(busca.lower() in livro.titulo.lower()):
                livrosPorTitulo.append(livro)
        
        if(len(livrosPorTitulo) > 0):
            return livrosPorTitulo
        
        livrosPorAutor = []
        for livro in self.catalogo:
            if(busca.lower() in livro.autor.lower()):
                livrosPorAutor.append(livro)
        
        if(len(livrosPorAutor) > 0):
            return livrosPorAutor
        
        return False

    def adicionarLivro(self, livro: Livro) -> None:
        self.catalogo.append(livro)

    def adicionarMembro(self, membro: Membro) -> None:
        self.registroMembros.append(membro)

    def pesquisaPorTitulo(self, titulo: str):
        for livro in self.catalogo:
            if(livro.titulo.lower() == titulo.lower()):
                return livro
        
        return False