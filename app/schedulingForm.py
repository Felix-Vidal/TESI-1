from ttkbootstrap import *
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from infra.repository.SchedulingRepository import SchedulingRepository
from infra.repository.RequesterRepository import RequesterRepository
from infra.entities.ERequester import ERequester
from tkcalendar import DateEntry


from infra.repository.UsersRepository import UsersRepository

# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ScheduleForm:
    
    def __init__(self, root):

        self.root = root
        # Configuração da janela principal
        self.root.title("SGAS")
        
        # Criação do estilo usando ttkbootstrap
        self.style = Style()
        self.style.configure("Outline.TButton", padding=(10, 5), width=15)
        self.style.configure("Outline.TMenubutton", padding=(10, 5), width=15)
        
        # Criação da barra lateral
        self.sidebar = ttk.Frame(root, style="TFrame")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Título na barra lateral
        self.title_label = ttk.Label(self.sidebar, text="SGAS",font="-size 24 -weight bold",  style="TLabel", padding=(10, 20, 10, 5))
        self.title_label.pack(fill=tk.X)
        
        # self.btn_voltar = ttk.Button(self.sidebar, text="Voltar", style="Outline.TButton")
        # self.btn_voltar.pack(pady=(5)) #por algum motivo n aparece embaixo dos menubutton
        
        # Menubuttons na barra lateral com estilo "OUTLINE"
        self.btn_user = ttk.Menubutton(self.sidebar, text="Usuarios", style="Outline.TMenubutton")
        self.btn_user.pack(pady=(10, 5))
        self.user_menu = tk.Menu(self.btn_user, tearoff=0)
        self.user_menu.add_command(label="Cadastrar")
        self.user_menu.add_command(label="Listar")
        self.btn_user["menu"] = self.user_menu
        
        self.btn_room = ttk.Menubutton(self.sidebar, text="Salas", style="Outline.TMenubutton")
        self.btn_room.pack(pady=5)
        self.room_menu = tk.Menu(self.btn_room, tearoff=0)
        self.room_menu.add_command(label="Cadastrar")
        self.room_menu.add_command(label="Listar")
        self.btn_room["menu"] = self.room_menu
        
        self.btn_block = ttk.Menubutton(self.sidebar, text="Blocos", style="Outline.TMenubutton")
        self.btn_block.pack(pady=5)
        self.block_menu = tk.Menu(self.btn_block, tearoff=0)
        self.block_menu.add_command(label="Cadastrar")
        self.block_menu.add_command(label="Listar")
        self.btn_block["menu"] = self.block_menu
        
        self.btn_request = ttk.Menubutton(self.sidebar, text="Solicitantes", style="Outline.TMenubutton")
        self.btn_request.pack(pady=5)
        self.request_menu = tk.Menu(self.btn_request, tearoff=0)
        self.request_menu.add_command(label="Cadastrar")
        self.request_menu.add_command(label="Listar")
        self.btn_request["menu"] = self.request_menu
        
        self.main_content = ttk.Frame(root)
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.schedule_form_frame = ttk.Frame(self.main_content)
        self.schedule_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.create_schedule_form()

    def register_schedule(self):
        requester_id = int(self.requester_id_entry.get())
        classroom_id = int(self.classroom_id_entry.get())
        selected_date = self.date_entry.get_date()
        selected_time = self.time_combo.get()
        
        try:
            date_time = datetime.strptime(f"{selected_date} {selected_time}:00", "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Invalid date and time format. Please use YYYY-MM-DD HH:MM:SS")
            return

        # Call the repository to insert the scheduling
        success = SchedulingRepository.insert(requester_id, classroom_id, date_time)
        
        if success:
            messagebox.showinfo("Success", "Scheduling successful.")
        else:
            messagebox.showerror("Error", "Time slot already taken for this classroom.")


    def create_schedule_form(self):
        ttk.Label(self.schedule_form_frame, text="Requester ID:").grid(row=0, column=0, padx=5, pady=5)
        self.requester_id_entry = ttk.Entry(self.schedule_form_frame)
        self.requester_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.schedule_form_frame, text="Classroom ID:").grid(row=1, column=0, padx=5, pady=5)
        self.classroom_id_entry = ttk.Entry(self.schedule_form_frame)
        self.classroom_id_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.schedule_form_frame, text="Enter Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.schedule_form_frame)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.schedule_form_frame, text="Time:").grid(row=3, column=0, padx=5, pady=5)
        self.time_combo = ttk.Combobox(self.schedule_form_frame, values=['7:30', '8:20', '9:20', '10:10', '11:10', '12:00', '13:30', '14:20', '15:20', '16:10', '17:10', '18:00', '19:30', '20:20', '21:20', '22:10'])
        self.time_combo.grid(row=3, column=1, padx=5, pady=5)
        
        schedule_button = ttk.Button(self.schedule_form_frame, text="Schedule", style="Outline.TButton", command=self.register_schedule)
        schedule_button.grid(row=4, column=0, columnspan=2, pady=10)