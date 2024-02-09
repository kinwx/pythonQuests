class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, genero: str) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero
        self.sobrenome= "Silva"

    def info(self):
        print(f"Nome: {self.nome}"
              f"\nSobrenome: {self.sobrenome}"
              f"\nIdade: {self.idade}"
              f"\nPeso: {self.peso}"
              f"\nGenêro: {self.genero}")
        
user = Pessoa("Lopes", 29, 87.8, "M")
user.info()
