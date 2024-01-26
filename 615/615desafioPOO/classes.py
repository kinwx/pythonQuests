vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
stopColor = '\033[0;0m'

class Conta:
    def __init__(self, conta: int, titular: str, saldo: float, tipo: str) -> None:
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.tipo = tipo

    def saque(self, qnt: float) -> dict:
        if(qnt <= self.saldo and qnt != 0):
            self.saldo = round(self.saldo - qnt, 2)
            return {
                "menssagem": verde + "Saque efetuado com sucesso!" + stopColor,
                "valor": qnt,
                "saldo": self.saldo,
            }
        return {
            "menssagem": vermelho + "Saldo insuficiente para saque." + stopColor,
            "valor": 0
        }

    def depositar(self, qnt: float) ->  dict:
        if(qnt == 0):
            return {
                "menssagem": f"{vermelho}Quantia inválida.{stopColor}"
            }
        
        self.saldo += qnt
        return {
            "menssagem": f"{verde}Valor depositado! Saldo atual: $ {self.saldo:.2f}{stopColor}"
        }

    def exibirSaldo(self) -> dict:
        return {
            "menssagem": f'{verde if self.saldo > 0 else vermelho}Saldo atual: $ {self.saldo:.2f}{stopColor}',
            "saldo": self.saldo
        }
    
    def resumo(self):
        return {
            "tipo": self.tipo,
            "conta": self.conta,
            "titular": self.titular,
            "saldo": self.saldo,
        }
    

class ContaCorrente(Conta):
    def __init__(self, conta: int, titular: str, saldo: float) -> None:
        super().__init__(conta, titular, saldo, "Conta Corrente")
        self.taxaDeManutenção = 1.98 # taxa de manutenção $ 1,98
        self.limiteDeChequeEspecial = 500 # limite para saque $ 500,00

    def saque(self, qnt: float) -> dict:
        if(qnt > self.limiteDeChequeEspecial):
            return {
                "menssagem": f"{amarelo}Valor de saque é maior do que o permitido. Valor máximo: {self.limiteDeChequeEspecial:.2f}{stopColor}",
                "valor": 0
            }

        return super().saque(qnt)
    

class ContaPoupanca(Conta):
    def __init__(self, conta: int, titular: str, saldo: float) -> None:
        super().__init__(conta, titular, saldo, "Conta Poupança")
        self.taxaDeJuros = 0.028 # taxa de juros 2,8%

    def calcularAdicicionarJuros(self) -> None:
        if(self.saldo == 0):
            return {
                "menssagem": amarelo + "Não foi possível calcular e adicinar juros. Saldo insuficiente." + stopColor,
                "juros": self.saldo
            }

        juros = self.saldo * self.taxaDeJuros
        self.saldo = self.saldo + round(juros, 2)
        return {
            "menssagem": verde + "Valor de juros adicionado." + stopColor,
            "juros": self.saldo * self.taxaDeJuros
        }
