import tkinter as tk
from tkinter import *

def salvar_nome(): #Função para salvar o nome
    global nome_salvo #Cria uma variavel global chamada nome_salvo
    nome_salvo = eNome.get() #nome_salvo da get em o nome que foi colocado
    window.destroy() #Destroi a primeira janela
    salvo() #Chama a função salva

def salvo(): #Função para ver o nome salvo
    newWindow = Tk() #Cria uma nova janela
    newWindow.geometry('200x100') #Define o tamanho da nova janela
    newWindow.title('Informações Salvas') #Título da nova janela

    lNomeSalvo = Label(newWindow, text='Nome: ' + nome_salvo) #Mostra o nome que foi registrado
    lNomeSalvo.pack() #Posiciona a Label

    newWindow.mainloop() #Roda a aplicação sem fechar ela instantaneamente

window = Tk() #Primeira janela
window.geometry('200x100') #Define o tamanho da janela
window.title('Informações') #Título da janela


lNome = Label(window, text='Nome') #Label escrito nome
lNome.pack() #Posiciona a Label

eNome = Entry(window, bd=5) #Caixa do input
eNome.pack()#Posiciona a caixa do input

btnSalvar = Button(window, text="Salvar", command=salvar_nome) #Botão para salvar o nome e mandar para proxima tela
btnSalvar.pack() #Posiciona o botão

window.mainloop() #Roda a aplicação sem fechar ela instantaneamente