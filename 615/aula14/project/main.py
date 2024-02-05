from classes import *

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
amarelo = '\033[33m'
ciano = '\033[36m'

stopColor = '\033[0;0m'

biblioteca = Biblioteca()
menssagemDeErro = vermelho + "VALOR INVÁLIDO." + stopColor
contadorDeIdsLivro = 11
contadorDeIdsMembro = 1

while(True):
    print(f'\n{azul}== OPÇÕES =={stopColor}'
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
            testAutor = autor.replace(" ", "")
            while(not testAutor or not testAutor.isalpha()):
                print(menssagemDeErro)
                autor = str(input("DIGITE O AUTOR DO LIVRO: ")).strip()
                testAutor = autor.replace(" ", "")
            
            biblioteca.adicionarLivro(Livro(id=contadorDeIdsLivro, titulo=titulo, autor=autor))
            contadorDeIdsLivro += 1
            print(f"\n{verde}O LIVRO{stopColor} {titulo}{verde}, DE AUTOR{stopColor} {autor} {verde}FOI ADICIONADO AO CATÁLOGO.{stopColor}")

        case "2":
            nome = str(input("DIGITE O NOME DO MEMBRO: ")).strip()
            testNome = nome.replace(" ", "")
            while(not nome or nome.isdecimal() or not nome.isalpha()):
                print(menssagemDeErro)
                nome = str(input("DIGITE O NOME DO MEMBRO: ")).strip()
            
            biblioteca.adicionarMembro(Membro(membroId=contadorDeIdsMembro, nome=nome))
            contadorDeIdsMembro += 1
            print(f"\n{verde}O MEMBRO{stopColor} {nome} {verde}FOI ADICIONADO AO REGISTRO.{stopColor}")

        case "3":
            while(True):
                print(f"\n{ciano}PESQUISE POR [ID | TITULO | AUTOR]{stopColor}")
                pesquisa = str(input("BUSCA INTELIGENTE: ")).strip()
                while(not pesquisa):
                    print(menssagemDeErro)
                    pesquisa = str(input("BUSCA INTELIGENTE: ")).strip()

                retorno = biblioteca.pesquisaDeLivros(pesquisa)
                if(not retorno):
                    print(f"\n{vermelho}BUSCA NÃO ENCONTRADA{stopColor}")
                    continue
                
                if(type(retorno) == Livro):
                    print(f'\n{azul}ID:{stopColor} {retorno.id}'
                        f'\n{azul}TITULO:{stopColor} {retorno.titulo}'
                        f'\n{azul}AUTOR:{stopColor} {retorno.autor}'
                        f'\n{azul}STATUS:{stopColor} {retorno.status}'
                        )
                    break
                else:
                    for livro in retorno:
                        print(f'\n{azul}ID:{stopColor} {livro.id}'
                        f'\n{azul}TITULO:{stopColor} {livro.titulo}'
                        f'\n{azul}AUTOR:{stopColor} {livro.autor}'
                        f'\n{azul}STATUS:{stopColor} {livro.status}'
                        )
                    break

        case "4":
            if(len(biblioteca.registroMembros) == 0):
                print(f"{amarelo}NÃO HÁ NENHUM MEBRO ADICIONADO AO REGISTRO PARA EMPRESTAR.{stopColor}")
                continue

            while(True):
                pesquisa = str(input("BUSCAR LIVRO: ")).strip()
                while(not pesquisa):
                    print(menssagemDeErro)
                    pesquisa = str(input("BUSCAR LIVRO: ")).strip()

                retorno = biblioteca.pesquisaDeLivros(pesquisa)
                if(not retorno):
                    print(f"\n{vermelho}BUSCA NÃO ENCONTRADA{stopColor}")
                    continue
                
                data: dict = {
                    "livro": "",
                    "membro": ""
                }
                if(type(retorno) == Livro):
                    print(f'{ciano}== LIVRO =={stopColor}'
                        f'\n{azul}ID:{stopColor} {retorno.id}'
                        f'\n{azul}TITULO:{stopColor} {retorno.titulo}'
                        f'\n{azul}AUTOR:{stopColor} {retorno.autor}'
                        f'\n{azul}STATUS:{stopColor} {retorno.status}'
                        )
                    if(retorno.status == "Indiponível"):
                        print(f"\n{amarelo}O LIVRO EM QUESTÃO ESTÁ INDISPONÍVEL{stopColor}")
                        cont = str(input(f"DESEJA PROCURAR OUTRO? {ciano}[s/n]{stopColor} ")).strip().lower()
                        while(["s", "n"].count(cont) == 0):
                            print(menssagemDeErro)
                            cont = str(input(f"DESEJA PROCURAR OUTRO? {ciano}[s/n]{stopColor} "))

                        match(cont):
                            case "s":
                                continue
                            case "n":
                                break
                    
                    data["livro"] = retorno
                else:
                    if(len(retorno) > 1):
                        print(f"{amarelo}DIGITE O TÍTULO COMPLETO DO LIVRO POR FAVOR.{stopColor}")
                        continue
                    
                    print(f'{ciano}== LIVRO =={stopColor}'
                        f'\n{azul}ID:{stopColor} {retorno[0].id}'
                        f'\n{azul}TITULO:{stopColor} {retorno[0].titulo}'
                        f'\n{azul}AUTOR:{stopColor} {retorno[0].autor}'
                        f'\n{azul}STATUS:{stopColor} {retorno[0].status}'
                        )
                    if(retorno[0].status == "Indiponível"):
                        print(f"{amarelo}\nO LIVRO EM QUESTÃO ESTÁ INDISPONÍVEL{stopColor}")
                        cont = str(input(f"DESEJA PROCURAR OUTRO? {ciano}[s/n]{stopColor} ")).strip().lower()
                        while(["s", "n"].count(cont) == 0):
                            print(menssagemDeErro)
                            cont = str(input(f"DESEJA PROCURAR OUTRO? {ciano}[s/n]{stopColor} ")).strip().lower()

                        match(cont):
                            case "s":
                                continue
                            case "n":
                                break

                    data["livro"] = retorno[0]
                
                while(True):
                    membroNome = str(input("\nQUEM ESTÁ SOLICITANDO O LIVRO: ")).strip()
                    while(not membroNome or membroNome.isdecimal() or not membroNome.isalpha()):
                        print(menssagemDeErro)
                        membroNome = str(input("QUEM ESTÁ SOLICITANDO O LIVRO: ")).strip()
                    
                    for member in biblioteca.registroMembros:
                        if(membroNome.lower() == member.nome.lower()):
                            data["membro"] = member.nome
                            member.attHistorico(data["livro"])
                    
                    if(len(data["membro"]) == 0):
                        print(f"{vermelho}USUÁRIO NÃO ENCONTRADO!{stopColor}")
                        continue

                    break

                biblioteca.emprestimo(data["livro"])
                tituloLivro = data["livro"].titulo
                membroNome = data["membro"]

                print(f"\n{verde}O LIVRO{stopColor} {tituloLivro} {verde}FOI EMPRESTADO PARA{stopColor} {membroNome}!")
                break
        
        case "5":
            livroNome = str(input("\nDIGITE O TÍTULO DO LIVRO: ")).strip()
            while(not livroNome):
                print(menssagemDeErro)
                livroNome = str(input("DIGITE O TÍTULO DO LIVRO: ")).strip()
            
            encontrado = biblioteca.pesquisaPorTitulo(livroNome)
            if(not encontrado):
                print(f"{vermelho}LIVRO NÃO ENCONTRADO.{stopColor}")
                continue
            
            if(encontrado.status == "Disponível"):
                print(f"{amarelo}ESTE LIVRO NEM FOI ALUGADO.{stopColor}")
                continue

            who = str(input("QUEM ESTÁ DEVOLVENDO O LIVRO: ")).strip()
            while(not who or who.isdecimal() or not who.isalpha()):
                print(menssagemDeErro)
                who = str(input("QUEM ESTÁ DEVOLVENDO O LIVRO: ")).strip()

            biblioteca.devolucao(encontrado, who)
            print(f"{verde}O LIVRO{stopColor} {encontrado.titulo} {verde}FOI DEVOLVIDO.{stopColor}")
