import tkinter as tk

def calculate():
    price_amount = float(entry_amount.get())
    percentage_increase = float(entry_percentage.get())
    result.set(round(price_amount * (1 + percentage_increase / 100), 2))

    label_after_increase_amount.config(fg="red", font=("Arial", 14, "bold"))

root = tk.Tk()
root.title("Price Increase Calculator")
result = tk.DoubleVar()
frame = tk.Frame(root)
frame.grid(rows=3, columns=2)

label_amount = tk.Label(frame, text='Price Amount')
label_amount.grid(row=0, column=0)

entry_amount = tk.Entry(frame)
entry_amount.grid(row=0, column=1)

label_percentage = tk.Label(frame, text='Percentage Increase')
label_percentage.grid(row=1, column=0)

entry_percentage = tk.Entry(frame)
entry_percentage.grid(row=1, column=1)

label_after_increase = tk.Label(frame, text='Price After Increase')
label_after_increase.grid(row=2, column=0)

label_after_increase_amount = tk.Label(frame, textvariable=result)
label_after_increase_amount.grid(row=2, column=1)

calculate_btn = tk.Button(frame, text="Calculate", command=calculate)
calculate_btn.grid(row=3, columnspan=2)

root.mainloop()
