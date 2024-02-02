from tkinter import *

janela = Tk()
janela.title("Aprendendo cores")
janela.geometry("200x200")
# janela.configure(bg="#7dde92")

def mostar_altura():
    altura = float(altura_input.get())
    resposta.configure(
        text=f"Sual altura é {altura}", fg="orange",
        font=("Arial", 16, "bold")
    )

altura = Label(text="Digite sua altura", fg="#140b19", bg="#735e96")
altura.pack()

altura_input = Entry()
altura_input.pack()

botao = Button(janela, text="Enviar", command=mostar_altura,bg="#ff47be", fg="#01161e")
botao.pack()

resposta = Label(text="")
resposta.pack()

janela.mainloop()