import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
from tkinter import messagebox
from infra.repository.SchedulingRepository import SchedulingRepository
from infra.repository.RequesterRepository import RequesterRepository
from infra.entities.ERequester import ERequester


from infra.repository.UsersRepository import UsersRepository

# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ScheduleForm:
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
        
        self.schedule_form_frame = ttk.Frame(self.main_content)
        self.schedule_form_frame.pack(padx=10, pady=10, fill=ttk.BOTH, expand=True)

        self.create_schedule_form()

    def register_schedule(self):
        requester_id = int(self.requester_id_entry.get())
        classroom_id = int(self.classroom_id_entry.get())
        selected_date = self.date.entry.get().replace("/","-")
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
        
        ttk.Label(self.schedule_form_frame, text="Enter Date:").grid(row=2, column=0, padx=5, pady=5)
        self.date = ttk.DateEntry(self.schedule_form_frame, dateformat='%Y/%m/%d', firstweekday=6)
        self.date.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.schedule_form_frame, text="Time:").grid(row=3, column=0, padx=5, pady=5)
        self.time_combo = ttk.Combobox(self.schedule_form_frame, values=['7:30', '8:20', '9:20', '10:10', '11:10', '12:00', '13:30', '14:20', '15:20', '16:10', '17:10', '18:00', '19:30', '20:20', '21:20', '22:10'])
        self.time_combo.grid(row=3, column=1, padx=5, pady=5)
        
        schedule_button = ttk.Button(self.schedule_form_frame, text="Schedule", style="Outline.TButton", command=self.register_schedule)
        schedule_button.grid(row=4, column=0, columnspan=2, pady=10)