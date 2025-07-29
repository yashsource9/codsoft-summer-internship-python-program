import tkinter as tk
from tkinter import messagebox
import os

# Functions
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Save Success", "Tasks saved successfully.")

def load_tasks():
    if os.path.exists("tasks.txt"):
        listbox_tasks.delete(0, tk.END)
        with open("tasks.txt", "r") as file:
            for task in file:
                listbox_tasks.insert(tk.END, task.strip())
    else:
        messagebox.showwarning("Load Error", "No saved tasks found.")

# GUI Window
window = tk.Tk()
window.title("My To-Do List")
window.geometry("400x400")

# Title Label
title = tk.Label(window, text="My To-Do List", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Entry Box
entry_task = tk.Entry(window, width=40)
entry_task.pack()

# Buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

btn_add = tk.Button(btn_frame, text="Add Task", width=15, command=add_task)
btn_add.pack(pady=2)

btn_delete = tk.Button(btn_frame, text="Delete Task", width=15, command=delete_task)
btn_delete.pack(pady=2)

btn_save = tk.Button(btn_frame, text="Save Tasks", width=15, command=save_tasks)
btn_save.pack(pady=2)

btn_load = tk.Button(btn_frame, text="Load Tasks", width=15, command=load_tasks)
btn_load.pack(pady=2)

# Task Listbox
listbox_tasks = tk.Listbox(window, width=50, height=10)
listbox_tasks.pack(pady=10)

# Start GUI loop
window.mainloop()
