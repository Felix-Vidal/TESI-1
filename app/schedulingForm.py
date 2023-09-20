import datetime
from ttkbootstrap import *
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
    
    def __init__(self, root, main_content, id = None):

        self.root = root
        self.main_content = main_content
        self.id = id
        self.schedule_form_frame = ttk.Frame(self.main_content)
        self.schedule_form_frame.pack()

        self.create_schedule_form()

    def register_schedule(self):
        requester = int(self.requester_id_entry.get())
        classroom= int(self.classroom_id_entry.get())
        selected_date = self.date.entry.get().replace("/","-")
        selected_time = self.time_combo.get()
        
        try:
            date_time = datetime.strptime(f"{selected_date} {selected_time}:00", "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Invalid date and time format. Please use YYYY-MM-DD HH:MM:SS")
            return

        if not requester or not classroom or not selected_date or not selected_time:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        # Call the repository to insert the scheduling
        if self.id:
            success = SchedulingRepository.update(self.id,requester, classroom, date_time)
        else:
            success = SchedulingRepository.insert(requester, classroom, date_time)
        if success:
            messagebox.showinfo("Success", "Scheduling successful.")
            print("Requester ID:", requester)
            print("Classroom ID:", classroom)
            print("Date:", selected_date)
            print("Time:", selected_time)
        else:
            messagebox.showerror("Error", "Time slot already taken for this classroom.")


    def create_schedule_form(self):
        
        width = 50
        font = ("", 16)
        self.schedule_form_frame = ttk.Frame(self.main_content)
        self.schedule_form_frame.pack(padx=(200,0), pady=40, fill=tk.BOTH, expand=True)
        if self.id:
            schedule = SchedulingRepository.get(self.id)
            
            ttk.Label(self.schedule_form_frame, text="Requester ID:").pack(anchor="w")
            self.requester_id_entry = ttk.Entry(self.schedule_form_frame, width=width, font=font)
            self.requester_id_entry.insert(0, schedule.requester)
            self.requester_id_entry.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Classroom ID:").pack(anchor="w")
            self.classroom_id_entry = ttk.Entry(self.schedule_form_frame, width=width, font=font)
            self.classroom_id_entry.insert(0, schedule.classRoom)
            self.classroom_id_entry.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Enter Date:").pack(anchor="w")
            self.date = ttk.DateEntry(self.schedule_form_frame, dateformat='%Y/%m/%d', firstweekday=6, width=width, font=font)
            self.date.insert(0, schedule.dateTime)
            self.date.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Time:").pack(anchor="w")
            self.time_combo = ttk.Combobox(self.schedule_form_frame, values=['7:30', '8:20', '9:20', '10:10', '11:10', '12:00', '13:30', '14:20', '15:20', '16:10', '17:10', '18:00', '19:30', '20:20', '21:20', '22:10'], width=width, font=font)
            self.time_combo.insert(0, schedule.dateTime)
            self.time_combo.pack(anchor="w")
        else:
            ttk.Label(self.schedule_form_frame, text="Requester ID:").pack(anchor="w")
            self.requester_id_entry = ttk.Entry(self.schedule_form_frame, width=width, font=font)
            self.requester_id_entry.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Classroom ID:").pack(anchor="w")
            self.classroom_id_entry = ttk.Entry(self.schedule_form_frame, width=width, font=font)
            self.classroom_id_entry.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Enter Date:").pack(anchor="w")
            self.date = ttk.DateEntry(self.schedule_form_frame, dateformat='%Y/%m/%d', firstweekday=6, width=width)
            self.date.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Time:").pack(anchor="w")
            self.time_combo = ttk.Combobox(self.schedule_form_frame, values=['7:30', '8:20', '9:20', '10:10', '11:10', '12:00', '13:30', '14:20', '15:20', '16:10', '17:10', '18:00', '19:30', '20:20', '21:20', '22:10'], width=width, font=font)
            self.time_combo.pack(anchor="w")
        
        schedule_button = ttk.Button(self.schedule_form_frame, text="Schedule", style="Outline.TButton", command=self.register_schedule)
        schedule_button.pack(anchor="w")
