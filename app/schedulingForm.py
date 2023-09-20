import datetime
from sqlalchemy import DateTime
from ttkbootstrap import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
from tkinter import messagebox
from infra.entities.Requesters import Requesters
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
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
        requester = self.requester_name_combobox.get()
        classroom= self.classroom_name_combobox.get()
        selected_date = self.date.entry.get().replace("/","-")
        selected_time = self.time_combo.get()
        
        print("Requester:", requester)
        print("Classroom:", classroom)
        print("Selected Date:", selected_date)
        print("Selected Time:", selected_time)
        
        try:
            date_time = datetime.strptime(f"{selected_date} {selected_time}:00", "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Invalid date and time format. Please use YYYY-MM-DD HH:MM:SS")
            return

        if not requester or not classroom or not selected_date or not selected_time:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        # Call the repository to insert the scheduling
        
        selected_requester = self.requester_name_combobox.get()
        selected_requester_id = int(selected_requester.split(' - ')[0])  # Obtém o ID

        selected_classroom = self.classroom_name_combobox.get()
        selected_classroom_id = int(selected_classroom.split(' - ')[0])
        
        if self.id:
            success = SchedulingRepository.update(self.id,selected_requester_id, selected_classroom_id, date_time)
        else:
            success = SchedulingRepository.insert(selected_requester_id, selected_classroom_id, date_time)
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
            requesters = RequesterRepository.gets()
            requester_names = [f"{requester.id} - {requester.name}" for requester in requesters]
            self.requester_name_combobox = ttk.Combobox(self.schedule_form_frame, values=requester_names, width=width, font=font)
            self.requester_name_combobox.insert(0, schedule.Schedulings.requester)
            self.requester_name_combobox.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Classroom ID:").pack(anchor="w")
            classrooms = ClassRoomsRepository.gets()
            classroom_names = [f"{classroom[0].id} - {classroom[0].name}" for classroom in classrooms]
            self.classroom_name_combobox = ttk.Combobox(self.schedule_form_frame, values=classroom_names, width=width, font=font)
            self.classroom_name_combobox.insert(0, schedule.Schedulings.classRoom)
            self.classroom_name_combobox.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Enter Date:").pack(anchor="w")
            self.date = ttk.DateEntry(self.schedule_form_frame, dateformat='%Y/%m/%d', firstweekday=6, width=width)
            self.date.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Time:").pack(anchor="w")
            self.time_combo = ttk.Combobox(self.schedule_form_frame, values=['7:30', '8:20', '9:20', '10:10', '11:10', '12:00', '13:30', '14:20', '15:20', '16:10', '17:10', '18:00', '19:30', '20:20', '21:20', '22:10'], width=width, font=font)
            self.time_combo.pack(anchor="w")
        else:
            ttk.Label(self.schedule_form_frame, text="Requester ID:").pack(anchor="w")
            requester_names = [f"{requester.id} - {requester.name}" for requester in Requesters]
            self.requester_name_combobox = ttk.Combobox(self.schedule_form_frame, values=requester_names, width=width, font=font)
            self.requester_name_combobox.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Classroom ID:").pack(anchor="w")
            classroom_names = [f"{classroom[0].id} - {classroom[0].name}" for classroom in classrooms]
            self.classroom_name_combobox = ttk.Combobox(self.schedule_form_frame, values=classroom_names, width=width, font=font)
            self.classroom_name_combobox.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Enter Date:").pack(anchor="w")
            self.date = ttk.DateEntry(self.schedule_form_frame, dateformat='%Y/%m/%d', firstweekday=6, width=width)
            self.date.pack(anchor="w")
            
            ttk.Label(self.schedule_form_frame, text="Time:").pack(anchor="w")
            self.time_combo = ttk.Combobox(self.schedule_form_frame, values=['7:30', '8:20', '9:20', '10:10', '11:10', '12:00', '13:30', '14:20', '15:20', '16:10', '17:10', '18:00', '19:30', '20:20', '21:20', '22:10'], width=width, font=font)
            self.time_combo.pack(anchor="w")
        
        self.requester_name_combobox.config(state='readonly')
        self.classroom_name_combobox.config(state='readonly')
        self.time_combo.config(state='readonly')
        
        schedule_button = ttk.Button(self.schedule_form_frame, text="Schedule", style="Outline.TButton", command=self.register_schedule)
        schedule_button.pack(anchor="w")
