import tkinter as tk
 
from tkinter import ttk

def bmi_calculus(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def userRegister():
    name = name_entry.get()
    age = int(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    bmi = bmi_calculus(weight, height)

    result_label.config(text=f'Name: {name} \n Age: {age} \n Weight: {weight} \n Height: {height} \n BMI: {bmi:.2f}')

root = tk.Tk()
root.title('Interface')
root.geometry('300x300')

# Define font.
fonte = ('Arial', 10)

# Create entry.
name_label = ttk.Label(root, text='Name:', font=fonte)
age_label = ttk.Label(root, text='Age:', font=fonte)
weight_label = ttk.Label(root, text='Weight (kg):', font=fonte)
height_label = ttk.Label(root, text='Height (m):', font=fonte)


name_entry = ttk.Entry(root, font=fonte, width=30)
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry.grid(row=0, column=1, padx=10, pady=5)


age_entry = ttk.Entry(root, font=fonte, width=30)
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry.grid(row=1, column=1, padx=10, pady=5)

weight_entry = ttk.Entry(root, font=fonte, width=30)
weight_label.grid(row=2, column=0, padx=10, pady=5)
weight_entry.grid(row=2, column=1, padx=10, pady=5)

height_entry = ttk.Entry(root, font=fonte, width=30)
height_label.grid(row=3, column=0, padx=10, pady=5)
height_entry.grid(row=3, column=1, padx=10, pady=5)

button = ttk.Button(root, text='Calcular IMC', command=userRegister)
button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

result_label = ttk.Label(root, text='')
result_label.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
