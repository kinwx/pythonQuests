# Sistema de Gerenciamento de Contas Bancárias em Python

Crie um sistema de gerenciamento de contas bancárias
em Python usando herança e polimorfismo. O sistema
deve incluir as seguintes classes:

### Classe Conta:

- A classe base "Conta" deve ter atributos para o número da conta, o titular da conta e o saldo.

- Ela deve incluir métodos para depósitos, saques e exibição do saldo
atual.

### Classe ContaCorrente:

- A classe "ContaCorrente "herda de "Conta" e inclui atributos específicos, como taxa de 
manutenção e limite de cheque especial.

- Deve sobrescrever o método de saque para
considerar o limite de cheque especial, se
necessário.

### Classe ContaPoupanca:

- A classe "ContaPoupanca "também herda de "Conta" 
e inclui atributos específicos, como taxa de juros.

- Ela deve ter um método para calcular e adicionar juros ao
saldo. 

## Polimorfismo:

- Crie um método chamado resumo que pode ser chamado
em qualquer objeto de conta (ContaCorrente ou
ContaPoupanca).

*Esse método resumo irá exibir um resumo das
informações da conta, incluindo o tipo de conta
(corrente ou poupança), o número da conta, o
titular da conta e o saldo atual.*

## Teste de Funcionalidade:

Crie um programa principal que demonstre o uso dessas
classes. Crie instâncias de contas
correntes e poupanças, realize depósitos,
saques, adicione juros e chame o método
resumo para cada conta.