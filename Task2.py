import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        destroy_label()
        body_mass = float(entry_weight.get())
        height = float(entry_height.get())

        if body_mass > 0 and height > 0:
            BMI = body_mass / height**2
            if BMI < 18.5:
                display_label(f"Your BMI is {BMI} \nYou are underweight", "blue")
            elif 18.5 <= BMI < 24.9:
                display_label(f"Your BMI is {BMI}\nYou are normal weight", "green")
            elif 25 <= BMI <= 29.9:
                display_label(f"Your BMI is {BMI}\nYou are overweight", "orange")
            else:
                display_label(f"Your BMI is {BMI}\nYou are obese", "red")

            

        elif body_mass <= 0 or height <= 0:
            messagebox.showerror("Error", "Invalid values. Please enter positive values for weight and height.")

    except ValueError:
        messagebox.showerror("Error", "Invalid entry. Please enter numeric values for weight and height.")

def display_label(text, color):
    global L1_exists
    if L1_exists:
        L1.config(text=text, fg=color)
    else:
        create_label(text, color)

def create_label(text, color):
    global L1_exists
    global L1
    L1 = tk.Label(root, text=text, font=("Arial", 12, "bold"),fg=color)
    L1.pack()
    L1_exists = True

def destroy_label():
    global L1_exists
    if L1_exists:
        L1.destroy()
        L1_exists = False

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")


font_label = ("Arial", 12)
font_entry = ("Arial", 12)
font_button = ("Arial", 12, "bold")


label_weight = tk.Label(root, text="Enter your body weight in KG:", font=font_label)
label_weight.pack(pady=5)

entry_weight = tk.Entry(root, font=font_entry)
entry_weight.pack(pady=5)

label_height = tk.Label(root, text="Enter your height in Meters:", font=font_label)
label_height.pack(pady=5)

entry_height = tk.Entry(root, font=font_entry)
entry_height.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=font_button)
calculate_button.pack(pady=10)


L1 = None
L1_exists = False

root.mainloop()
