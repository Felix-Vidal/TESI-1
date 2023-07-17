import tkinter as tk
from component_login import Login
        

if __name__ == "__app__":
    root = tk.Tk()
    TelaPricipal = Login(root)
    root.mainloop()