from classes import *
from random import randint


biblioteca = Biblioteca()
menssagemDeErro = "Valor Inválido"
contadorDeIdsLivro = 11
contadorDeIdsMembro = 1

while(True):
    print('== OPÇÕES =='
          '\n[0] - SAIR'
          '\n[1] - ADICIONAR LIVRO'
          '\n[2] - ADICIONAR MEMBRO'
          '\n[3] - PESQUISAR LIVRO'
          '\n[4] - PEGAR LIVRO EMPRESTADO'
          '\n[5] - DEVOLVER LIVRO'
          )
    escolha = str(input("DIGITE SUA ESCOLHA: ")).strip()
    while(['0', '1', '2', '3', '4', '5'].count(escolha) == 0):
        print(menssagemDeErro)
        escolha = str(input("DIGITE SUA ESCOLHA: ")).strip()

    match(escolha):
        case "0":
            break
        case "1":
            titulo = str(input("DIGITE O TITULO DO LIVRO: ")).strip()
            while(not titulo):
                print(menssagemDeErro)
                titulo = str(input("DIGITE O TITULO DO LIVRO: ")).strip()
            
            autor = str(input("DIGITE O AUTOR DO LIVRO: ")).strip()
            while(not autor or autor.isdecimal()):
                print(menssagemDeErro)
                autor = str(input("DIGITE O AUTOR DO LIVRO: ")).strip()
            
            biblioteca.adicionarLivro(Livro(id=contadorDeIdsLivro, titulo=titulo, autor=autor))
            contadorDeIdsLivro += 1

        case "2":
            nome = str(input("DIGITE O NOME DO MEMBRO: ")).strip()
            while(not nome or nome.isdecimal()):
                print(menssagemDeErro)
                nome = str(input("DIGITE O NOME DO MEMBRO: ")).strip()
            
            biblioteca.adicionarMembro(Membro(numeroMembro=contadorDeIdsMembro, nome=nome))
            contadorDeIdsMembro += 1

        case "3":
            while(True):
                pesquisa = str(input("BUSCA: ")).strip()
                while(not pesquisa):
                    print(menssagemDeErro)
                    pesquisa = str(input("BUSCA: ")).strip()

                retorno = biblioteca.pesquisaDeLivros(pesquisa)
                if(pesquisa.isdecimal()):
                    print(f'\nID: {retorno.id}'
                        f'\nTITULO: {retorno.titulo}'
                        f'\nAUTOR: {retorno.autor}'
                        f'\nSTATUS: {retorno.statusEmprestimo}'
                        )
                    break
                else:
                    if(not retorno):
                        print("\nBUSCA NÃO ENCONTRADA")
                        continue

                    for livro in retorno:
                        print(f'\nID: {livro.id}'
                        f'\nTITULO: {livro.titulo}'
                        f'\nAUTOR: {livro.autor}'
                        f'\nSTATUS: {livro.statusEmprestimo}'
                        )
                    break


        case "4":
            while(True):
                pesquisa = str(input("BUSCAR LIVRO: ")).strip()
                while(not pesquisa):
                    print(menssagemDeErro)
                    pesquisa = str(input("BUSCAR LIVRO: ")).strip()

                retorno = biblioteca.pesquisaDeLivros(pesquisa)
                data: object = {
                    "livro": "",
                    "membro": ""
                }
                if(pesquisa.isdecimal()):
                    data["livro"] = retorno.titulo
                else:
                    if(not retorno):
                        print("\nBUSCA NÃO ENCONTRADA")
                        continue

                    if(retorno[0].statusEmprestimo == "Indiponível"):
                        print("\nO LIVRO EM QUESTÃO ESTÁ INDISPONÍVEL")
                        cont = str(input("DESEJA PROCURAR OUTRO? [s/n] "))
                        while(["s", "n"].count(cont) == 0):
                            print(menssagemDeErro)
                            cont = str(input("DESEJA PROCURAR OUTRO? [s/n] "))

                        match(cont):
                            case "s":
                                continue
                            case "n":
                                break

                    data["livro"] = retorno[0].titulo
                
                while(True):
                    membroNome = str(input("QUEM ESTÁ SOLICITANDO O LIVRO: "))
                    while(not membroNome or membroNome.isdecimal()):
                        print(menssagemDeErro)
                        membroNome = str(input("QUEM ESTÁ SOLICITANDO O LIVRO: "))
                    
                    for member in biblioteca.registroMembros:
                        if(membroNome == member.nome):
                            data["membro"] = member.nome
                            member.attHistorico(data["livro"])
                    
                    if(len(data["membro"]) == 0):
                        print("USUÁRIO NÃO ENCONTRADO!")
                        continue

                    break

                biblioteca.emprestimo(data["livro"])
                tituloLivro = data["livro"]
                membroNome = data["membro"]

                print(f"\nO LIVRO {tituloLivro} FOI EMPRESTADO PARA {membroNome}!")
                break
        
        case "5":
            livroNome = str(input("\nDIGITE O NOME DO LIVRO: "))
            while(not livroNome):
                print(menssagemDeErro)
                livroNome = str(input("DIGITE O NOME DO LIVRO: "))
            
            encontrado = biblioteca.pesquisaDeLivros(livroNome)
            if(encontrado[0].statusEmprestimo == "Disponível"):
                print("ESTE LIVRO NEM FOI ALUGADO.")
                continue

            who = str(input("QUEM ESTÁ DEVOLVENDO O LIVRO: "))
            while(not who or who.isdecimal()):
                print(menssagemDeErro)
                who = str(input("QUEM ESTÁ DEVOLVENDO O LIVRO: "))

            biblioteca.devolucao(encontrado[0], who)


            
