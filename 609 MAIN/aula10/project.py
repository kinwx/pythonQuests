from tkinter import *
from data import *
from funcAux import regexInside
import re

window = Tk()
window.title("Cadastro")
window.geometry("400x400")

regex = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#._-])[0-9a-zA-Z$*&@#._-]{8,}$')
emailReg = re.compile(r'^[a-zA-Z0-9._-]+@([a-z]+)(\.[a-z]{2,3})+$')

def registerUser():
    getEmail = inputEmail.get()
    passes = [inputPass.get(), inputPassAgain.get()]
    for clean in [getEmail, *passes]:
        if(not clean):
            return res.configure(text="Preencha todos os campos!")
        
    if(len(set(passes)) != 1):
        return res.configure(text="As senhas não são iguais!", fg="red")

    if(not emailReg.match(getEmail)):
        return res.configure(text="Insira um e-mail válido!")
    
    if(not regex.match(passes[0])):
        return res.configure(text=f"{regexInside(passes[0])}")

    isExist = False
    for user in mainData.dataBase:
        if(user.email == getEmail):
            isExist = True

    return res.configure(text="E-mail já cadastrado!", fg="red") if isExist else res.configure(text="Cadastro efetuado com sucesso!", fg="green")


labelEmail = Label(text="Insira seu e-mail:")
labelPass = Label(text="Insira sua senha:")
labelPassAgain = Label(text="Insira sua senha novamente:")

inputEmail = Entry()
inputPass = Entry(show="*")
inputPassAgain = Entry(show="*")

button = Button(text="Registrar", command=registerUser)

res = Label(text="")

labelEmail.pack()
inputEmail.pack()

labelPass.pack()
inputPass.pack()

labelPassAgain.pack()
inputPassAgain.pack()

button.pack()

res.pack()

window.mainloop()