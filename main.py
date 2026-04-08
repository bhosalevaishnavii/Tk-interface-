import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x450")

frame = tk.Frame(root)
frame.pack(pady=20)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task")

title = tk.Label(frame, text="Task Manager", font=("Arial", 18))
title.pack()

entry = tk.Entry(frame, width=30)
entry.pack(pady=10)

tk.Button(frame, text="Add Task", command=add_task).pack(pady=5)
tk.Button(frame, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(frame, width=35, height=10)
listbox.pack(pady=10)

root.mainloop()
