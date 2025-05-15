import random
from tkinter import *

class Employee:
    def __init__(self):
     self.employees = [
         "Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", 
       "Ago James", "Michell Taiwo", "Abraham Jones" ,  "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"
       ]
    
    self.tasks = [
        "Loading", "Transporting", "Reveiwing Orders", "Customer Service", "Delivering Items"
        ]
    self.attendance = {}

    def check_employee(self, name):
        return name in self.employees
    
    def take_attendance(self, name):
     self.attendance[name] = "Present"     
     return f"{name} marked present for today."

    
    def assign_task(self, name):
        task = random.choice(self.tasks)
        return f"{name}'s task for today: {task}"
    
    def refuse_access(self):
        return "Sorry, you're not an employee. Access denied."


class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Attendance System")
        self.employee = Employee()
        
        
        self.label = Label(root, text="Enter your name:")
        self.label.pack()
        
        self.entry = Entry(root, width=30)
        self.entry.pack()
        
        self.button = Button(root, text="Submit", command=self.process_employee)
        self.button.pack()
        
        self.result = Label(root, text="", wraplength=300)
        self.result.pack()

    def process_employee(self):
        name = self.entry.get()
        if self.employee.check_employee(name):
            attendance_msg = self.employee.take_attendance(name)
            task_msg = self.employee.assign_task(name)
            self.result.config(text=f"{attendance_msg}\n{task_msg}")
        else:
            self.result.config(text=self.employee.refuse_access())