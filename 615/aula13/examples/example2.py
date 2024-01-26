# ENCAPSULAMENTO
class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def getNome(self):
        return self.__nome
    def setNome(self, func):
        self.__nome = func(self.__nome)
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    def setIdade(self, valor):
        self.__idade = valor
        return self.__idade
    
    def getAltura(self):
        return self.__altura
    def setAltura(self, valor):
        self.__altura = valor
        return self.__altura

    def info(self):
        return {
            "nome": self.getNome(),
            "idade": self.getIdade(),
            "altura": self.getAltura(),
        }

pessoa1 = Pessoa(nome="Maria", idade=25, altura=1.62)
# print(pessoa1.info())
pessoa1.__nome = "Joaquim"

print(pessoa1.getNome())

pessoa1.setNome(lambda prev: prev + "Gomes")

print(pessoa1.getNome())

# print(pessoa1.info())