
#felixmokayabeatz is coding 

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

import tkinter as tk
from tkinter import ttk  # Import themed widgets

def enforce_min_size(event):
    if login_window.winfo_width() < 600 or login_window.winfo_height() < 200:
        login_window.geometry("600x200")

def on_entry_click(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, "end")

def on_focusout(event):
    if username_entry.get() == '':
        username_entry.insert(0, 'Username')

def on_pass_click(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, "end")
        password_entry.config(show='*')

def on_pass_focusout(event):
    if password_entry.get() == '':
        password_entry.config(show='')
        password_entry.insert(0, 'Password')

def login():
    entered_username = username.get()
    entered_password = password.get()

    if entered_username == entered_password:
        root.deiconify()
        login_window.withdraw()
    else:
        login_status.config(text="Invalid credentials. Use any Username same as Password.")

def update_screen(value):
    current = screen.get()

    if value == 'C':
        screen.set("")
    elif value == '=':
        try:
            result = eval(current)
            screen.set(str(result))
        except:
            screen.set("Error")
    else:
        screen.set(current + value)

def toggle_theme():
    global is_dark
    if is_dark:
        root.config(bg='#F0F0F0')
        entry.config(style='Light.TEntry')
        for row in buttons:
            for button in row:
                button.config(style='Light.TButton')
        theme_button.config(text="Dark Theme")
        is_dark = False
    else:
        root.config(bg='#303030')
        entry.config(style='Dark.TEntry')
        for row in buttons:
            for button in row:
                button.config(style='Dark.TButton')
        theme_button.config(text="Light Theme")
        is_dark = True

root = tk.Tk()
root.title("Felix Mokaya")
is_dark = False

s = ttk.Style()
s.theme_use('clam')

s.configure('Light.TButton', background='#55C5FF', foreground='black', font=('Arial', 12))
s.map('Light.TButton', background=[('active', 'white')])

s.configure('Dark.TButton', background='#292929', foreground='white', font=('Arial', 12))
s.map('Dark.TButton', background=[('active', '#757575')])

s.configure('Light.TEntry', fieldbackground='#EEEEEE', foreground='grey', font=('Arial', 15))
s.configure('Dark.TEntry', fieldbackground='#111', foreground='white', font=('Arial', 15))

login_window = tk.Toplevel(root)
login_window.title("Secure Login")

login_status = ttk.Label(login_window, text="Login\nPassword same as Username", font=('Arial', 14))
login_status.pack(pady=10)

login_window.geometry("600x200")
login_window.resizable(False, False)
login_window.bind("<Configure>", enforce_min_size)
login_window.geometry("600x200")

username = tk.StringVar()
password = tk.StringVar()

username_entry = ttk.Entry(login_window, textvariable=username, width=20)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', on_entry_click)
username_entry.bind('<FocusOut>', on_focusout)
username_entry.pack(pady=10)

password_entry = ttk.Entry(login_window, textvariable=password, show='', width=20)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', on_pass_click)
password_entry.bind('<FocusOut>', on_pass_focusout)
password_entry.pack()

login_button = ttk.Button(login_window, text="Login", command=login)
login_button.pack()

root.withdraw()
root.title("Calculator")

screen = tk.StringVar()
entry = ttk.Entry(root, textvariable=screen, justify='right', style='Light.TEntry')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
entry.config(font=('Arial', 20))

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

buttons = []
for i in range(4):
    row = []
    for j in range(4):
        if i * 4 + j < len(button_texts):
            button_text = button_texts[i * 4 + j]
            button = ttk.Button(root, text=button_text, command=lambda x=button_text: update_screen(x), style='Light.TButton', width=5, padding=5)
            button.grid(row=i + 1, column=j, padx=5, pady=5, sticky='nsew')
            row.append(button)
            root.rowconfigure(i + 1, weight=1)
            root.columnconfigure(j, weight=1)
    buttons.append(row)

theme_button = ttk.Button(root, text="Dark Theme", command=toggle_theme)
theme_button.grid(row=5, columnspan=4, sticky='ew')

root.mainloop()

