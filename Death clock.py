import datetime
import tkinter as tk

def calculate_death_date():

    age = int(age_entry.get())

    gender = gender_var.get()

    life_expectancy = calculate_life_expectancy(age, gender) 

    today = datetime.date.today()

    death_date = today + datetime.timedelta(days=(life_expectancy * 365))

    result_label.config(text=f"Estimated death date: {death_date.strftime('%Y-%m-%d')}") 

root = tk.Tk()

age_entry = tk.Entry(root)

gender_var = tk.StringVar(value="Male")  

calculate_button = tk.Button(root, text="Calculate", command=calculate_death_date)

result_label = tk.Label(root, text="")
root.mainloop() 