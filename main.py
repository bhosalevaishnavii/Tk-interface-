import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x450")
root.configure(bg="#f0f0f0")  # background color

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task")

# Title
title = tk.Label(root, text="Task Manager", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Entry
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", bg="#4CAF50", fg="white", width=15, command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", bg="#f44336", fg="white", width=15, command=delete_task)
delete_btn.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=35, height=12, font=("Arial", 11))
listbox.pack(pady=15)

root.mainloop()
