class Cachorro:
    def __init__(self, nome: str, raca: str, idade: int) -> None:
        self.nome = nome
        self.raca = raca
        self.idade = idade


dog1 = Cachorro(nome="Fusca", raca="Peduro", idade=12)
dog2 = Cachorro(nome="Junin", raca="Caramelo", idade=6)

print(dog1.nome)

print(dog2.raca)
print(dog2.idade)
