import tkinter as tk


def display_greeting(entry=None, greeting_label=None):
    name = entry.get()
    greeting_label.config(text=f"Hello {name}")


def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)


def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="dark olive green")


root = tk.Tk()
root.title("Your Task list")
root.configure(background="navajo white")

text1 = tk.Label(root, text="Your new task:", bg="navajo white", fg="black")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="orange1")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add task", bg="navajo white", fg="orange1", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Remove task", bg="navajo white", fg="orange1", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as done", bg="navajo white", fg="dark olive green", command=mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text="Task list:", bg="navajo white", fg="black")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="LightPink1", fg="black")
task_listBox.pack(pady=10)

root.mainloop()
