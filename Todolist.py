import tkinter as tk

from tkinter import messagebox

import json

import os


TODO_FILE = "todo_list.json"


def load_todos():

    if os.path.exists(TODO_FILE):

        with open(TODO_FILE, "r") as file:

            return json.load(file)

    return []


def save_todos(todos):

    with open(TODO_FILE, "w") as file:

        json.dump(todos, file, indent=4)


def add_task():

    task = entry_task.get()

    if task:

        todos.append({"task": task, "completed": False})

        save_todos(todos)

        update_task_list()

        entry_task.delete(0, tk.END)

    else:

        messagebox.showwarning("Input Error", "Please enter a task.")


def update_task_list():

    listbox_tasks.delete(0, tk.END)

    for i, todo in enumerate(todos):

        status = "Done" if todo["completed"] else "Not Done"

        listbox_tasks.insert(tk.END, f"{i+1}. {todo['task']} [{status}]")


def mark_task_complete():

    selected_task = listbox_tasks.curselection()

    if selected_task:

        index = selected_task[0]

        todos[index]["completed"] = True

        save_todos(todos)

        update_task_list()

    else:

        messagebox.showwarning("Selection Error", "Please select a task.")


def delete_task():

    selected_task = listbox_tasks.curselection()

    if selected_task:

        index = selected_task[0]

        todos.pop(index)

        save_todos(todos)

        update_task_list()

    else:

        messagebox.showwarning("Selection Error", "Please select a task.")


def update_task():

    selected_task = listbox_tasks.curselection()

    if selected_task:

        index = selected_task[0]

        new_task = entry_task.get()

        if new_task:

            todos[index]["task"] = new_task

            save_todos(todos)

            update_task_list()

            entry_task.delete(0, tk.END)

        else:

            messagebox.showwarning("Input Error", "Please enter a task.")

    else:

        messagebox.showwarning("Selection Error", "Please select a task.")


app = tk.Tk()

app.title("To-Do List Application")


todos = load_todos()


frame_tasks = tk.Frame(app)

frame_tasks.pack(pady=10)


listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10)

listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)


scrollbar_tasks = tk.Scrollbar(frame_tasks)

scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)


listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

scrollbar_tasks.config(command=listbox_tasks.yview)


entry_task = tk.Entry(app, width=50)

entry_task.pack(pady=10)


frame_buttons = tk.Frame(app)

frame_buttons.pack(pady=10)


button_add = tk.Button(frame_buttons, text="Add Task", command=add_task)

button_add.pack(side=tk.LEFT, padx=5)


button_update = tk.Button(frame_buttons, text="Update Task", command=update_task)

button_update.pack(side=tk.LEFT, padx=5)


button_complete = tk.Button(frame_buttons, text="Complete Task", command=mark_task_complete)

button_complete.pack(side=tk.LEFT, padx=5)


button_delete = tk.Button(frame_buttons, text="Delete Task", command=delete_task)

button_delete.pack(side=tk.LEFT, padx=5)


update_task_list()


app.mainloop()

