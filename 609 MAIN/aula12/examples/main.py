class Veiculo:
    def __init__(self, marca: str, modelo: str, cor: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def ligar(self):
        return f"O veículo ligou."
        
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int, qtde_portas: int) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.qtde_portas = qtde_portas
    
    def ligar_o_ar(self):
        return "O carro ligou o ar-condicionado."

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int, cilindradas: float) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.cilindradas = cilindradas

class Bicicleta(Veiculo):
    def __init__(self, marca: str, cor: str, ano: int, marchas: bool) -> None:
        super().__init__(marca, cor, ano)
        self.marchas = marchas

carro1 = Carro("Fiat", "Palio", "Azul", 2004, 4)
moto1 = Moto("Honda", "500x", "Vermelho", 2021, 500)
bicicleta = Bicicleta("Caloi", "Cinza", 2019, True)

print(carro1.ligar())
print(carro1.ligar_o_ar())
print(moto1.cilindradas)
print(bicicleta.ligar())