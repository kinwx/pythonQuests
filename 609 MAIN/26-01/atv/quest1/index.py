from tkinter import *
from functools import reduce

window = Tk()
window.title("Média de Notas")
window.geometry("300x300")

class ResponseConfigure:
    def __init__(self, label, fg = "", bg = "") -> None:
        self.label = label
        self.background = bg
        self.color = fg


def calcule():
    notas = [float(inputNota1.get()), float(inputNota2.get()), float(inputNota3.get())]
    media = list(map(lambda total: total / len(notas), [reduce(lambda total, note: total + note, notas, 0)]))[0]
    print(notas, media)
    res = ResponseConfigure(label="Aprovado", bg="green") if media >= 7 else ResponseConfigure(label="Reprovado", bg="red")
    res = ResponseConfigure(label="Aprovado com Distinção", bg="blue") if media == 10 else res

    invalidValue = False
    for nota in notas:
        if nota > 10 or nota < 0:
            invalidValue = True
            break
    
    res = ResponseConfigure(label="Valores inválidos. Média não calculada", bg="gray") if invalidValue else res
    response.configure(text=f"{res.label}", bg=f"{res.background}")


labelNota1 = Label(text="Digite a 1° nota:")
labelNota2 = Label(text="Digite a 2° nota:")
labelNota3 = Label(text="Digite a 3° nota:")

response = Label(text="")

inputNota1 = Entry()
inputNota2 = Entry()
inputNota3 = Entry()

button = Button(window, text="Calcular", command=calcule, width=16)

labelNota1.pack()
inputNota1.pack()
labelNota2.pack()
inputNota2.pack()
labelNota3.pack()
inputNota3.pack()
button.pack(pady=10)

response.pack()

window.mainloop()
