from tkinter import *
from datetime import datetime

box = Tk()
box.title("Maior de Idade")
box.geometry("250x250")

def calcular_idade():
    nome = nome_input.get()
    ano = int(ano_input.get())
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade >= 18:
        print(f"{nome} já pode ser preso")
    else:
        print(f"{nome} não pode ser preso")


nome_label = Label(text="Digite seu nome: ")
nome_label.pack()

nome_input = Entry()
nome_input.pack()



ano_label = Label(text="Digite sua ano de nascimento: ")
ano_label.pack()

ano_input = Entry()
ano_input.pack()


botao = Button(box, text="Calcular idade", command=calcular_idade)
botao.pack()

box.mainloop()