import tkinter as tk

def click_button(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(char))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Primitiv Kalkulyator")

entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20,
              command=lambda b=button: click_button(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(window, text="C", padx=20, pady=20, command=clear_entry).grid(row=5, column=0)

window.mainloop()
