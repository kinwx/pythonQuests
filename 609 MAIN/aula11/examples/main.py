class Moto:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas: float) -> None:
        self.cilindradas = cilindradas
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.velocidade_atual = 0

    def buzinar(self):
        return f"A moto {self.modelo} está buzinando, sai da frente."
    
    def acelerar(self):
        self.velocidade_atual += 20
        return f"A mot está acelerando."
    
    def freiar(self):
        self.velocidade_atual -= 10
        return "A moto está freiando"
    
    def dar_grau(self):
        return "A moto está dando grau 😎👍"


moto1 = Moto(
    marca="Honda",
    modelo="Bros",
    ano=2016,
    cor="Preto",
    cilindradas=160
)
moto2 = Moto(
    marca="Yamaha",
    modelo="Factor",
    ano=2019,
    cor="Vermelha",
    cilindradas=149.7
)

print(moto1.modelo)
print(moto2.modelo)

print(moto1.buzinar())