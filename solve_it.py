import tkinter as tk
import random

# Initial values for statistics
correct_answers = 0
total_attempts = 0
current_solution = 0  # Stores the correct result of the expression

def generate_expression():
    """Generates a new mathematical expression and sets it in the label."""
    global current_solution, total_attempts
    
    operator = random.choice(["+", "-", "*"])  # Randomly chooses an operator
    
    if operator in ["+", "-"]:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
    else:  # If it's multiplication (*), use numbers from 1 to 20
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 20)
    
    current_solution = eval(f"{number1} {operator} {number2}")  # Calculates the correct solution
    label_expression.config(text=f"{number1} {operator} {number2}")  # Sets the expression in the label
    
    entry_solution.delete(0, tk.END)  # Clears the previous input
    global total_attempts
    total_attempts += 1  # Increases the total number of expressions
    update_statistics()  # Updates the statistics display

def check_solution():
    """Checks if the user's input is correct."""
    global correct_answers
    
    try:
        input_value = int(entry_solution.get())  # Gets the number from the Entry field
        if input_value == current_solution:
            correct_answers += 1  # Increases the number of correct answers
            label_result.config(text="✅ Correct!", fg="green")
        else:
            label_result.config(text=f"❌ Incorrect! Correct: {current_solution}", fg="red")
    except ValueError:
        label_result.config(text="⚠ Enter a number!", fg="orange")
    
    update_statistics()  # Updates the statistics
    generate_expression()  # Automatically generates a new expression

def update_statistics():
    """Updates the label that displays statistics (correct / total)."""
    label_statistics.config(text=f"{correct_answers} / {total_attempts}")

def close_application():
    """Closes the Tkinter window."""
    root.destroy()

# Creating the Tkinter window
root = tk.Tk()
root.title("Math Quiz")
root.geometry("400x250")

frame = tk.Frame(root)
frame.pack(pady=20)

# Label for displaying the expression
label_expression = tk.Label(frame, text="Click 'Generate'", font=("Arial", 20))
label_expression.grid(row=0, column=0, padx=10)

# Entry field for entering the solution
entry_solution = tk.Entry(frame, font=("Arial", 16), width=5)
entry_solution.grid(row=0, column=1, padx=10)

# Button to check the solution
button_check = tk.Button(frame, text="Check", font=("Arial", 14), command=check_solution)
button_check.grid(row=0, column=2, padx=10)

# Label for displaying the result (correct/incorrect)
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=5)

# Label for statistics (number of correct / total expressions)
label_statistics = tk.Label(root, text="0 / 0", font=("Arial", 14))
label_statistics.pack()

# Button to end the game
button_end = tk.Button(root, text="End", font=("Arial", 14), command=close_application)
button_end.pack(pady=10)

# Generates the first expression when the program starts
generate_expression()

# Running the Tkinter application
root.mainloop()
import tkinter as tk
import random

# Initial values for statistics
correct_answers = 0
total_attempts = 0
current_solution = 0  # Stores the correct result of the expression

def generate_expression():
    """Generates a new mathematical expression and sets it in the label."""
    global current_solution, total_attempts
    
    operator = random.choice(["+", "-", "*"])  # Randomly chooses an operator
    
    if operator in ["+", "-"]:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
    else:  # If it's multiplication (*), use numbers from 1 to 20
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 20)
    
    current_solution = eval(f"{number1} {operator} {number2}")  # Calculates the correct solution
    label_expression.config(text=f"{number1} {operator} {number2}")  # Sets the expression in the label
    
    entry_solution.delete(0, tk.END)  # Clears the previous input
    global total_attempts
    total_attempts += 1  # Increases the total number of expressions
    update_statistics()  # Updates the statistics display

def check_solution():
    """Checks if the user's input is correct."""
    global correct_answers
    
    try:
        input_value = int(entry_solution.get())  # Gets the number from the Entry field
        if input_value == current_solution:
            correct_answers += 1  # Increases the number of correct answers
            label_result.config(text="✅ Correct!", fg="green")
        else:
            label_result.config(text=f"❌ Incorrect! Correct: {current_solution}", fg="red")
    except ValueError:
        label_result.config(text="⚠ Enter a number!", fg="orange")
    
    update_statistics()  # Updates the statistics
    generate_expression()  # Automatically generates a new expression

def update_statistics():
    """Updates the label that displays statistics (correct / total)."""
    label_statistics.config(text=f"{correct_answers} / {total_attempts}")

def close_application():
    """Closes the Tkinter window."""
    root.destroy()

# Creating the Tkinter window
root = tk.Tk()
root.title("Math Quiz")
root.geometry("400x250")

frame = tk.Frame(root)
frame.pack(pady=20)

# Label for displaying the expression
label_expression = tk.Label(frame, text="Click 'Generate'", font=("Arial", 20))
label_expression.grid(row=0, column=0, padx=10)

# Entry field for entering the solution
entry_solution = tk.Entry(frame, font=("Arial", 16), width=5)
entry_solution.grid(row=0, column=1, padx=10)

# Button to check the solution
button_check = tk.Button(frame, text="Check", font=("Arial", 14), command=check_solution)
button_check.grid(row=0, column=2, padx=10)

# Label for displaying the result (correct/incorrect)
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=5)

# Label for statistics (number of correct / total expressions)
label_statistics = tk.Label(root, text="0 / 0", font=("Arial", 14))
label_statistics.pack()

# Button to end the game
button_end = tk.Button(root, text="End", font=("Arial", 14), command=close_application)
button_end.pack(pady=10)

# Generates the first expression when the program starts
generate_expression()

# Running the Tkinter application
root.mainloop()
