import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        self.priority = priority
        self.completed = False

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

  
        self.create_widgets()

    def create_widgets(self):
      
        tk.Label(self.master, text="Description:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.master, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.master, text="Priority:").grid(row=2, column=0, sticky=tk.E)

  
        self.description_entry = tk.Entry(self.master)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5)
        self.due_date_entry = tk.Entry(self.master)
        self.due_date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.priority_entry = tk.Entry(self.master)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5)

       
        tk.Button(self.master, text="Add Task", command=self.add_task).grid(row=3, column=0, columnspan=2, pady=10)


        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.grid(row=4, column=0, columnspan=2, pady=10)
        self.populate_task_listbox()

        
        tk.Button(self.master, text="Mark as Completed", command=self.mark_as_completed).grid(row=5, column=0, pady=5)
        tk.Button(self.master, text="Remove Task", command=self.remove_task).grid(row=5, column=1, pady=5)

        tk.Button(self.master, text="Delete All Tasks", command=self.delete_all_tasks).grid(row=6, column=0, columnspan=2, pady=10)

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if description and due_date and priority:
            task = Task(description, due_date, priority)
            self.tasks.append(task)
            self.populate_task_listbox()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Incomplete Information", "Please provide all task details.")

    def populate_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = 'Done' if task.completed else 'Not Done'
            self.task_listbox.insert(tk.END, f"{index}. {task.description} (Due Date: {task.due_date}, Priority: {task.priority}) - {status}")

    def clear_entry_fields(self):
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()

        if selected_index:
            task_index = selected_index[0]
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index].completed = True
                self.populate_task_listbox()
            else:
                messagebox.showwarning("Invalid Task Index", "Please select a valid task.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()

        if selected_index:
            task_index = selected_index[0]
            if 0 <= task_index < len(self.tasks):
                del self.tasks[task_index]
                self.populate_task_listbox()
            else:
                messagebox.showwarning("Invalid Task Index", "Please select a valid task.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")

    def delete_all_tasks(self):
        confirmed = messagebox.askyesno("Delete All Tasks", "Are you sure you want to delete all tasks?")
        if confirmed:
            self.tasks = []
            self.populate_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

