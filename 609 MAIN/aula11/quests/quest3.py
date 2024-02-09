class Calculadora:
    def __init__(self) -> None:
        ...
    
    def somar(self, n1: float, n2: float) -> float:
        return n1 + n2
    
    def subtrair(self, n1: float, n2: float) -> float:
        return n1 - n2
    
    def mult(self, n1: float, n2: float) -> float:
        return n1 * n2
    
    def dividir(self, n1: float, n2: float) -> float | False:
        return False if n2 == 0 else n1 / n2
    

calculadora = Calculadora()

while(True):
    print("== OPÇÕES =="
          "\n[0] - SAIR"
          "\n[1] - SOMAR"
          "\n[2] - SUBTRAIR"
          "\n[3] - MULTIPLICAR"
          "\n[4] - DIVIDIR")
    res = str(input("DIGITE SUA ESCOLHA: "))
    while(['0', '1', '2', '3', '4'].count(res) == 0):
        print("VALOR INVÁLIDO.")
        res = str(input("DIGITE SUA ESCOLHA: "))

    n1 = str(input("DIGITE O PRIMEIRO NÚMERO: "))
    while(not n1.isdecimal()):
        print("VALOR INVÁLIDO.")
        n1 = str(input("DIGITE O PRIMEIRO NÚMERO: "))

    n2 = str(input("DIGITE O SEGUNDO NÚMERO: "))
    while(not n2.isdecimal()):
        print("VALOR INVÁLIDO.")
        n2 = str(input("DIGITE O SEGUNDO NÚMERO: "))
    
    match(res):
        case '0':
            break
        case '1':
            print(f"{n1} + {n2} = {calculadora.somar(float(n1), float(n2))}")
        case '2':
            print(f"{n1} - {n2} = {calculadora.subtrair(float(n1), float(n2))}")
        case '3':
            print(f"{n1} x {n2} = {calculadora.mult(float(n1), float(n2))}")
        case '4':
            result = calculadora.dividir(float(n1), float(n2))

            print(f"{n1} / {n2} = {result}") if result else print("NÃO É POSSÍVEL DIVIDIR POR 0")
