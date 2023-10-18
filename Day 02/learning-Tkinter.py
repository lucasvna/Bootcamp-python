# Graphic library tkinter. tk referencies the objects and classes from Tkinter module.
import tkinter as tk

# Theme tkinter, Widget packs 
from tkinter import ttk

# Creates a window
root = tk.Tk()
root.title('Interface')

# Define o tamanho da janela
root.geometry('300x300')

# Cria os widgets
root.configure(bg='blue')

nome_label = ttk.Label(root, text='Primeira interface', font=('Arial', 12, 'bold'), foreground='green')
nome_label.pack(padx=80, pady=20)

root.mainloop()
