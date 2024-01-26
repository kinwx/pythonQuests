class Tarefa:
    def __init__(self, tarefa: str, descricao: str) -> None:
        self.tarefa = tarefa
        self.descricao = descricao

class Projeto:
    def __init__(self, projeto: str, descricao: str) -> None:
        self.projeto = projeto
        self.descricao = descricao
        self.bancoDeTarefas = []

    def adicionarTarefas(self, tarefa: Tarefa) -> None:
        self.bancoDeTarefas.append(tarefa)


menssagemDeError = "VALOR INVÁLIDO."
bancoDeTarefas = []
bancoDeProjetos = []

while(True):
    print(f'\n=== OPÇÕES ==='
          f'\n[0] - SAIR'
          f'\n[1] - ADICIONAR PROJETO'
          f'\n[2] - ADICIONAR TAREFA'
          f'\n[3] - VER PROJETOS'
          f'\n[4] - VER TAREFAS'
          )
    
    res = input("DIGITE SUA ESCOLHA: ").strip()
    while(['1', '2', '0', '3', '4'].count(res) == 0):
        print(menssagemDeError)
        res = input("DIGITE SUA ESCOLHA: ").strip()
    
    match(res):
        case '0':
            break
        case '1':
            projetoNome = input("\nDIGITE O NOME DO PROJETO: ").strip().upper()
            while(not projetoNome):
                print(menssagemDeError)
                projetoNome = input("\nDIGITE O NOME DO PROJETO: ").strip().upper()

            descricaoProjeto = input("\nDIGITE A DESCRIÇÃO DO PROJETO: ").strip()
            while(not descricaoProjeto):
                print(menssagemDeError)
                descricaoProjeto = input("\nDIGITE A DESCRIÇÃO DO PROJETO: ").strip()

            projeto = Projeto(projeto=projetoNome, descricao=descricaoProjeto)    

            while(True):
                tarefaLabel = input("\nDIGITE SUA TAREFA: ").strip().upper()
                while(not tarefaLabel):
                    print(menssagemDeError)
                    tarefaLabel = input("\nDIGITE SUA TAREFA: ").strip().upper()

                descricaoTarefa = input("\nDIGITE A DESCRIÇÃO DA TAREFA: ").strip()
                while(not descricaoTarefa):
                    print(menssagemDeError)
                    descricaoTarefa = input("\nDIGITE A DESCRIÇÃO DA TAREFA: ").strip()

                tarefa = Tarefa(tarefa=tarefaLabel, descricao=descricaoTarefa)
                projeto.adicionarTarefas(tarefa)

                cont = input("DESEJA ADICIONAR OUTRA? [s/n] ")
                while(['s','n'].count(cont) == 0):
                    print(menssagemDeError)
                    cont = input("DESEJA ADICIONAR OUTRA? [s/n] ")
                
                if cont == 'n':
                    break

            bancoDeProjetos.append(projeto)

        case '2':
            tarefa = input("\nDIGITE SUA TAREFA: ").strip().upper()
            while(not tarefa):
                print(menssagemDeError)
                tarefa = input("\nDIGITE SUA TAREFA: ").strip().upper()

            descricao = input("\nDIGITE A DESCRIÇÃO DA TAREFA: ").strip()
            while(not descricao):
                print(menssagemDeError)
                descricao = input("\nDIGITE A DESCRIÇÃO DA TAREFA: ").strip()

            bancoDeTarefas.append(Tarefa(tarefa=tarefa, descricao=descricao))
        
        case '3':
            if len(bancoDeProjetos)==0:
                print('LISTA VAZIA')
            else:
                for proj in bancoDeProjetos:
                    print(f'\nPROJETO: {proj.projeto}'
                        f'\nDESCRIÇÃO: {proj.descricao}')
                    for tf in proj.bancoDeTarefas:
                        print(f'\nTAREFA: {tf.tarefa}'
                            f'\nDESCRIÇÃO: {tf.descricao}')
                    
        case '4':
            if len(bancoDeTarefas)==0:
                print('LISTA VAZIA')
            else:
                for tf in bancoDeTarefas:
                    print(f'\nTAREFA: {tf.tarefa}'
                        f'\nDESCRIÇÃO: {tf.descricao}')
