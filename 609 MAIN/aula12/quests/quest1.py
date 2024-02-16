class Animal:
    def __init__(self, nome: str, raca: str, cor: str, peso: float) -> None:
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.peso = peso

    def comer(self, nome_comida):
        return f"O animal {self.nome} comeu a comida {nome_comida}"
    
    def dormir(self):
        return f"O animal {self.nome} está dormindo"
    

class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, cor: str, peso: float, pedigre: bool) -> None:
        super().__init__(nome, raca, cor, peso)
        self.pedigre = pedigre

    def pegar_bolinha(self):
        return f"O cachorro {self.nome} pegou a bolinha"
    

class Papagaio(Animal):
    def __init__(self, nome: str, raca: str, cor: str, peso: float, asa_cortada: bool) -> None:
        super().__init__(nome, raca, cor, peso)
        self.asa_cortada = asa_cortada

    def voar(self):
        if(self.asa_cortada):
            return "O papagaio está voando"

        return "O papagaio está com suas asas cortadas"


cachorro1 = Cachorro("Max", "Vira-Lata", "Caramelo", 48.7, False)
papagaio1 = Papagaio("Zé", "Papagaio-verdadeiro", "Verde", 0.800, False)
porco1 = Animal("Rosalina", "Bacurin", "Rosa", 30)


print(cachorro1.pegar_bolinha())
print(papagaio1.voar())
print(porco1.comer("Maçã"))
print(porco1.dormir())