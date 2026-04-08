import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

tasks = []

# Function to add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

# Function to delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

# UI Elements
title = tk.Label(root, text="Task Manager", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

root.mainloop()
