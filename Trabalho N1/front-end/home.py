import tkinter as tk
from tkinter import ttk

# exemplo de professor
class Home():
    def __init__(self, master): #customizar a janela
        self.janela = master
        self.janela.title('Banco de Brasil')
        self.janela.geometry('400x400')
        #self.janela.maxsize(400)
        #self.janela.resizable(width=True,height=True)
        #Menu
        mnu_barra = tk.Menu(self.janela) #Barra
        mnu_arquivo = tk.Menu(mnu_barra, tearoff=0) #Item
        mnu_barra.add_cascade(label='Contas', menu=mnu_arquivo)
        mnu_arquivo.add_command(label='Novo Arquivo...') #SubItens
        mnu_arquivo.add_command(label='Sair', command=self.janela.destroy)
        self.janela.config(menu=mnu_barra)
        mnu_editar = tk.Menu(mnu_barra, tearoff=0)
        mnu_barra.add_cascade(label='Editar', menu=mnu_editar)
        mnu_editar.add_command(label='Copiar')
        mnu_editar.add_command(label='Colar')
        mnu_editar.add_command(label='Recortar')
        mnu_editar.add_separator()
        mnu_pesquisar = tk.Menu(mnu_editar, tearoff=0)
        mnu_editar.add_cascade(label='Pesquisar', menu=mnu_pesquisar)
        mnu_pesquisar.add_command(label='Arquivo')
        mnu_pesquisar.add_command(label='Caracter')
        mnu_pesquisar.add_command(label='Palavra')



app = tk.Tk()
janelaPrincipal = Home(app)
app.mainloop()