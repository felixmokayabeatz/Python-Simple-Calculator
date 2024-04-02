#felixmokayabeatz

import tkinter as tk
from tkinter import ttk

def on_click(button_value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(button_value))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def switch_theme():
    current_theme = theme_var.get()
    new_theme = 'dark' if current_theme == 'light' else 'light'
    
    if new_theme == 'dark':
        set_dark_theme()
    else:
        set_light_theme()
    
    theme_var.set(new_theme)

def set_dark_theme():
    root.configure(bg='#2E2E2E')
    entry.configure(bg='#2E2E2E', fg='white')
    theme_button.configure(bg='#2E2E2E', fg='white')

def set_light_theme():
    root.configure(bg='SystemButtonFace')
    entry.configure(bg='SystemButtonFace', fg='black')
    theme_button.configure(bg='SystemButtonFace', fg='black')

def clear_entry():
    entry.delete(0, tk.END)
    
def on_key(event):
    if event.char and event.keysym not in ['Return', 'BackSpace']:
        key = event.char
        on_click(key)
    elif event.keysym == 'Return':  # Enter key on numpad
        calculate()
    elif event.keysym == 'BackSpace':  # Backspace key
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])








root = tk.Tk()
root.title("Felix")

# Entry widget for display
entry = tk.Entry(root, width=50, font=('Arial', 15))
entry.grid(row=0, column=0, columnspan=4)

# Buttons


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0


for button in buttons:
    tk.Button(root, text=button, width=6, height=3,
              command=lambda btn=button: on_click(btn) if btn != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Theme toggle button
theme_var = tk.StringVar(value='light')
theme_button = tk.Button(root, text="Toggle Theme", command=switch_theme)
theme_button.grid(row=row_val, column=col_val, columnspan=4)

clear_button = tk.Button(root, text= "Clear" , command = clear_entry)
clear_button.grid(row=row_val, column=col_val)
col_val += 1


# Set initial light theme
set_light_theme()

# Run the Tkinter event loop
root.bind("<Key>", on_key)

root.mainloop()
