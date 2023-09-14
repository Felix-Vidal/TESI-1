import ttkbootstrap as ttk
from tkinter import messagebox
from app.home import Home
from infra.repository.UsersRepository import UsersRepository

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Login:
    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        
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
        self.frameMain.pack(expand=True, fill="both", pady=150)

        font = ("", 16)
        width = 30 

        self.label_username = ttk.Label(self.frameMain, text="Username:", font=font)
        self.label_username.pack()

        self.entry_username = ttk.Entry(self.frameMain, width=width, font=font)
        self.entry_username.pack(pady=10)
        self.entry_username.focus()

        self.label_password = ttk.Label(self.frameMain, text="Password:", font=font)
        self.label_password.pack()

        self.entry_password = ttk.Entry(self.frameMain, show="*", width=width, font=font)  # Aumente o valor de width conforme desejado
        self.entry_password.pack()

        self.button_login = ttk.Button(self.frameMain, text="Login", command=self.login)
        self.button_login.pack(pady=5)

    def login(self):

        username = self.entry_username.get()
        password = self.entry_password.get()
        user = UsersRepository.getUserName(username)


        # Simulando um processo de autenticação simples
        if username == user.userName and password == user.password:
            self.open_home()
        else:
            messagebox.showerror("Login", "Credenciais inválidas.")

    def open_home(self):
        limpar_tela(self.root)
        TelaPricipal = Home(self.root)


root = ttk.Window(themename="cyborg")
TelaPricipal = Login(root)
root.mainloop()