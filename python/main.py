from random import choice
from functools import reduce
data = []
errorMessage = '\033[31mValor inválido.\033[0;0m'
print('\033[34mVERSÃO: 1.4.0\033[0;0m')
while(True):
    print('\n[0] - SAIR')
    print('[1] - CADASTRAR')
    print('[2] - SORTEAR') if len(data) > 1 else print('')
    choose = input('DIGITE SUA ESCOLHA: ')
    while(['0', '1', '2'].count(choose) == 0):
        print(errorMessage)
        choose = input('DIGITE SUA ESCOLHA: ')
    choose = int(choose)
    match(choose):
        case 0:
            break
        case 1:
            while(True):
                name = str(input('\nDigite o nome do cliente: '))
                test = name.replace(' ', '') 
                while(not test.isalpha()):
                    print(errorMessage)
                    name = str(input('\nDigite o nome do cliente: '))
                    test = name.replace(' ', '') 
                cpf = str(input('Digite o CPF do cliente: '))
                cpf = cpf.replace('.', '')
                cpf = cpf.replace('-', '')
                while(len(cpf) < 11 or len(cpf) >  11 or cpf.isalpha()):
                    print('\033[33mO CPF precisa ter 11 dígitos.\033[0;0m')
                    cpf = str(input('Digite o CPF do cliente: '))
                    cpf = cpf.replace('.', '')
                    cpf = cpf.replace('-', '')
                value = input('Digite o valor da compra do cliente: ')
                while(value.isalpha() or float(value) <= 0):
                    print(errorMessage)
                    value = input('Digite o valor da compra do cliente: ')
                data.append({
                    "name": name,
                    "cpf": cpf,
                    "value": float(value)
                })
                contin = str(input('\nDESEJA CONTINUAR? [s/n] '))
                while(['S', 'N'].count(contin.upper()) == 0):
                    print(errorMessage)
                    contin = str(input('\nDESEJA CONTINUAR? [s/n] '))
                if contin.upper() == 'N':
                    break
        case 2:
            sort = choice(data)
            print(f'\nParabéns {sort["name"].upper()}, CPF: {sort["cpf"]}, você foi o sorteado por ter feito uma compra no valor de R$ {sort["value"]:.2f}')
            bigger = reduce(lambda el, item: item if el["value"] < item["value"] else el, data, data[0])
            print(f'\nCliente com maior valor de compra:'
                  f'\nNOME: {bigger["name"]}'
                  f'\nCPF: {bigger["cpf"]}'
                  f'\nVALOR: {bigger["value"]:.2f}')
