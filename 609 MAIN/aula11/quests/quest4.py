class Fatura:
    def __init__(self, item: str, preco: float, quantidade: int) -> None:
        self.item = item
        self.preco = preco
        self.quantidade = quantidade
        self.total = 0

    def calcular_total(self) -> float:
        self.total = self.preco * self.quantidade
        return self.total
    
biscoito = Fatura(item="Oreo", preco=1.19, quantidade=4)
print("R$", biscoito.calcular_total())