from classes import ContaCorrente, ContaPoupanca
from random import randint

# TERMINAL CORES
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
amarelo = '\033[33m'
ciano = '\033[36m'

stopColor = '\033[0;0m'

# MENSSAGEM DE ERROR
menssagemDeError = vermelho + 'VALOR INVÁLIDO.' + stopColor
# BANCO - DATA
bancoDeContas = []

while True:
    # MENU DE OPÇÕES
    print(f'{azul}\n== OPÇÕES =={stopColor}'
          '\n[0] - SAIR'
          '\n[1] - CRIAR CONTA'
          '\n[2] - ENTRAR NA CONTA')
    
    # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
    escolha = input('DIGITE SUA ESCOLHA: ')
    while(['1', '2', '0'].count(escolha) == 0):
        print(menssagemDeError)
        escolha = input('DIGITE SUA ESCOLHA: ')

    # OPÇÕES E SUAS RESPECTIVAS AÇÕES
    escolha = int(escolha)
    match(escolha):
        # SAIR
        case 0:
            break

        # CADASTRAR
        case 1:
            # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
            titular = input('DIGITE SEU NOME: ')
            test = titular.replace(' ', '')
            while(not test.isalpha()):
                print(menssagemDeError)
                titular = input('DIGITE SEU NOME: ')
                test = titular.replace(' ', '')
            
            # GERANDO NÚMERO DE CONTA ALEATÓRIO
            conta = randint(1000, 9999) * 11
            # SALDO INCIAL: 0
            saldo = 0

            # OPÇÃO DE TIPO DE CONTA
            print('\n[1] - CONTA CORRENTE'
                  '\n[2] - CONTA POUPANÇA')
            
            # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
            tipoDeConta = input('DIGITE SUA ESCOLHA: ')
            while(['1', '2'].count(tipoDeConta) == 0):
                print(menssagemDeError)
                tipoDeConta = input('DIGITE SUA ESCOLHA: ')

            # CRIAR DIFERENTES TIPOS DE CONTA
            match(tipoDeConta):
                case '1':
                    bancoDeContas.append(ContaCorrente(conta, titular, saldo))
                case '2':
                    bancoDeContas.append(ContaPoupanca(conta, titular, saldo))

            # RESPOSTA AO USUÁRIO
            print(verde + '\nConta criada com sucesso!' + stopColor)
        
        # ENTRAR NA CONTA
        case 2:
            # CASO NÃO HAJA CONTAS
            if(len(bancoDeContas) == 0):
                print(amarelo + '\nNÃO HÁ CONTAS CADASTRADAS.' + stopColor)
                continue

            # EXIBIÇÃO DE CONTAS CADASTRADAS NO BANCO
            for conta in bancoDeContas:
                dados = conta.resumo()
                print(f'{ciano}\n=========== x ==========={stopColor}'
                      f'\nCONTA: {dados["conta"]}'
                      f'\nTITULAR: {dados["titular"]}')
                
            # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
            numeroDaConta = input('\nDIGITE O NÚMERO DA CONTA PARA ENTRAR: ')
            while(not numeroDaConta.isdecimal() and numeroDaConta != ''):
                print(menssagemDeError)
                numeroDaConta = input('DIGITE O NÚMERO DA CONTA PARA ENTRAR: ')
            
            # CASO NÃO SEJA DIGITADO NADA, VOLTAR AO MENU ANTERIOR
            if(numeroDaConta == ''):
                continue

            # PROCURANDO CONTA NO BANCO
            contaSelecionada = list(filter(lambda account: account.conta == int(numeroDaConta), bancoDeContas))

            # PEDIR DADOS NOVAMENTE CASO CONTA NÃO SEJA ENCONTRADA
            while(len(contaSelecionada) == 0):

                # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
                print(amarelo + 'CONTA NÃO ENCONTRADA.' + stopColor)
                numeroDaConta = input('\nDIGITE O NÚMERO DA CONTA PARA ENTRAR: ')
                while(not numeroDaConta.isdecimal() and numeroDaConta != ''):
                    print(menssagemDeError)
                    numeroDaConta = input('DIGITE O NÚMERO DA CONTA PARA ENTRAR: ')

                # CASO NÃO SEJA DIGITADO NADA, NÃO PROCURE CONTA, SAIA DO LOOP
                if(numeroDaConta == ''):
                    break

                # PROCURANDO CONTA NO BANCO
                contaSelecionada = list(filter(lambda account: account.conta == int(numeroDaConta), bancoDeContas))

            # CASO NÃO SEJA DIGITADO NADA, VOLTAR AO MENU ANTERIOR
            if(numeroDaConta == ''):
                continue
            
            # TRANFORMANDO EM UMA VARIÁVEL O VALOR INCIAL DE UMA LISTA
            [ contaSelecionada ] = contaSelecionada

            # ENTROU NA CONTA
            while(True):
                # MENSAGEM DE BOAS-VINDAS
                print(f'{ciano}\nBEM VINDO(A) {contaSelecionada.titular.upper()}{stopColor}')

                # OPÇÕES DA CONTA
                match(contaSelecionada.tipo):
                    # CONTA CORRENTE - OPÇÕES
                    case 'Conta Corrente':
                        print(f'{azul}\n== OPÇÕES =={stopColor}'
                            '\n[0] - SAIR'
                            '\n[1] - SACAR'
                            '\n[2] - DEPOSITAR'
                            '\n[3] - EXIBIR SALDO'
                            '\n[4] - EXIBIR RESUMO'
                            )
                        
                        # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
                        escolhaDoUsuario = input('DIGITE SUA ESCOLHA: ')
                        while(['0', '1', '2', '3', '4'].count(escolhaDoUsuario) == 0):
                            print(menssagemDeError)
                            escolhaDoUsuario = input('DIGITE SUA ESCOLHA: ')

                    # CONTA POUPANÇA - OPÇÕES
                    case 'Conta Poupança':
                        print(f'{azul}\n== OPÇÕES =={stopColor}'
                            '\n[0] - SAIR'
                            '\n[1] - SACAR'
                            '\n[2] - DEPOSITAR'
                            '\n[3] - EXIBIR SALDO'
                            '\n[4] - EXIBIR RESUMO'
                            '\n[5] - PASSAR UM MÊS'
                            )
                        
                        # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
                        escolhaDoUsuario = input('DIGITE SUA ESCOLHA: ')
                        while(['0', '1', '2', '3', '4', '5'].count(escolhaDoUsuario) == 0):
                            print(menssagemDeError)
                            escolhaDoUsuario = input('DIGITE SUA ESCOLHA: ')
                
                # ESCOLHAS
                escolhaDoUsuario = int(escolhaDoUsuario)
                match(escolhaDoUsuario):
                    # SAIR
                    case 0:
                        break

                    # SACAR
                    case 1:
                        # ENTRADA E TRATAMENTO DE VALORES
                        qntRequirida = input('DIGITE O VALOR DE SAQUE: ').replace(',', '.')
                        testQnt = qntRequirida.replace('.', '')
                        somente1ponto = 0
                        qntNumerosDepoisVirg = 0
                        
                        # TESTE PARA SABER SE É UM NÚMERO FLUTUANTE VÁLIDO
                        for numero in qntRequirida:
                            if(numero == '.'):
                                somente1ponto += 1
                            if(somente1ponto > 0):
                                qntNumerosDepoisVirg += 1
                        
                        # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
                        while(not testQnt.isdecimal() or somente1ponto > 1 or qntNumerosDepoisVirg > 2):
                            print(menssagemDeError) if qntNumerosDepoisVirg < 2 else print(f'{amarelo}A quantidade de máxima de dígitos depois da vírgula é 2.{stopColor}'
                                                                                           f'\n{amarelo}Caso esteja querendo colocar valores acima de 999, não coloque ponto.{stopColor}')
                            qntRequirida = input('DIGITE O VALOR DE SAQUE: ').replace(',', '.')
                            testQnt = qntRequirida.replace('.', '')
                            somente1ponto = 0
                            qntNumerosDepoisVirg = 0
                            for numero in qntRequirida:
                                if(somente1ponto > 0):
                                    qntNumerosDepoisVirg += 1
                                if(numero == '.'):
                                    somente1ponto += 1
                        

                        # UTILIZANDO MÉTODO DE SAQUE DA CLASSE
                        qntRequirida = float(qntRequirida)
                        res = contaSelecionada.saque(qntRequirida)
                        print('\n' + res["menssagem"])
                        
                    # DEPOSITAR
                    case 2:
                        # ENTRADA E TRATAMENTO DE VALORES
                        qntDeposito = input('DIGITE O VALOR DE DEPÓSITO: ').replace(',', '.')
                        testQnt = qntDeposito.replace('.', '')
                        somente1ponto = 0
                        qntNumerosDepoisVirg = 0

                        # TESTE PARA SABER SE É UM NÚMERO FLUTUANTE VÁLIDO
                        for numero in qntDeposito:
                            if(somente1ponto > 0):
                                qntNumerosDepoisVirg += 1
                            if(numero == '.'):
                                somente1ponto += 1
                        
                        # FILTRO PARA INSERÇÃO DE DADOS CORRETAMENTE
                        while(not testQnt.isdecimal() or somente1ponto > 1 or qntNumerosDepoisVirg > 2):
                            print(menssagemDeError) if qntNumerosDepoisVirg < 2 else print(f'{amarelo}A quantidade de máxima de dígitos depois da vírgula é 2.{stopColor}'
                                                                                           f'\n{amarelo}Caso esteja querendo colocar valores acima de 999, não coloque ponto.{stopColor}')
                            qntDeposito = input('DIGITE O VALOR DE DEPÓSITO: ').replace(',', '.')
                            testQnt = qntDeposito.replace('.', '')
                            somente1ponto = 0
                            qntNumerosDepoisVirg = 0
                            for numero in qntDeposito:
                                if(somente1ponto > 0):
                                    qntNumerosDepoisVirg += 1
                                if(numero == '.'):
                                    somente1ponto += 1
                        
                        # UTILIZANDO MÉTODO DE DEPÓSITO DA CLASSE
                        qntDeposito = float(qntDeposito)
                        res = contaSelecionada.depositar(qntDeposito)
                        print('\n' + res["menssagem"])
                    
                    # EXIBIR SALDO
                    case 3:
                        # UITLIZANDO MÉTODO DE EXIBIR SALDO DA CLASSE
                        res = contaSelecionada.exibirSaldo()
                        print('\n' + res["menssagem"])

                    # RESUMO
                    case 4:
                        # UTILIZANDO MÉTODO DE RESUMO DA CLASSE
                        res = contaSelecionada.resumo()
                        print(f'{azul}\nTIPO:{stopColor} {res["tipo"]}'
                            f'{azul}\nCONTA:{stopColor} {res["conta"]}'
                            f'{azul}\nTITULAR:{stopColor} {res["titular"]}'
                            f'{azul}\nSALDO:{stopColor} {res["saldo"]}'
                            )
                        
                    # CALCULAR JUROS
                    case 5:
                        # UTILIZANDO MÉTODO DE CALCULAR JUROS DE CONTA DO TIPO POUPANÇA
                        res = contaSelecionada.calcularAdicicionarJuros()
                        print('\n' + res["menssagem"])
