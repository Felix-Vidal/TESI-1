import ttkbootstrap as tkk
from tkinter import messagebox

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Home:
    
    def __init__(self, root):

        self.root = root
        # Configuração da janela principal
        self.root.title("sem title")
        


   
        
        
        
    