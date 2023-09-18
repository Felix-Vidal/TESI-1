import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
from login import Login
from datetime import datetime
import time
def clean_screen(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Init:
    def __init__(self, root):
        self.root = root

        self.root.title("SGAS")
        
        # Calculate screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 1300
        window_height = 600

        # Calculate x and y coordinates to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"1300x600+{x}+{y}")

        self.frameMain = ttk.Frame(self.root)
        self.frameMain.pack(expand=True, fill="both", pady=(150,0))
        font = ("", 20)
        self.logo_path = "img/init.png"
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((170, 170)) 
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.lbl_logo = ttk.Label(self.frameMain, image=self.logo_tk)
        self.lbl_logo.pack()

        self.lbl_title = ttk.Label(self.frameMain, text="Sistema de Gerenciamento de Agendamento de Salas", font=font)
        self.lbl_title.pack(pady=(50,25))

        button = tk.Button(self.frameMain, text="Login", command=self.open_login, width=30)
        button.pack()


    def open_login(self):
        clean_screen(self.root)
        TelaPrincipal = Login(self.root)


root = ttk.Window(themename="cyborg")
TelaPricipal = Init(root)
root.mainloop()
