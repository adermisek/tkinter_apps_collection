import tkinter as tk

def submit_data():
    global total
    try:
        name = entry_name.get()
        amount = int(entry_amount.get())
        total += amount
        print(f"Hello {name}!")  
        item_list.append(name + ",")
        update_total()
    except ValueError:
        print("Error: Please enter a valid number for the amount.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def end_data():
    try:
        label_total_text.config(text="Total amount:") 
        entry_name.delete(0, tk.END)  
        entry_amount.delete(0, tk.END) 
        
        if item_list:
            item_list[-1] = item_list[-1][:-1]
        
        label_item_list.config(text=item_list)
        label_items.config(text="Items:")
    except Exception as e:
        print(f"Unexpected error: {e}")

def update_total():
    try:
        label_total.config(text=total)
    except Exception as e:
        print(f"Unexpected error: {e}")

root = tk.Tk()
root.title("Data Entry Application")  

item_list = []
total = 0

frame  = tk.Frame(root, bg="red")
frame.grid(row=4, column=2, padx=20, pady=20)

label_name = tk.Label(frame, text="Enter name:", font=("Arial", 12), anchor="w", bg="red")
label_name.grid(row=0, column=0) 

entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

label_amount = tk.Label(frame, text="Enter amount:", font=("Arial", 12), bg="red")
label_amount.grid(row=1, column=0) 

entry_amount = tk.Entry(frame)
entry_amount.grid(row=1, column=1)

submit_button = tk.Button(frame, text="Submit", command=submit_data, font=("Arial", 12, "bold"), fg="green", bg="black")
submit_button.grid(row=2, column=0) 

end_button = tk.Button(frame, text="End", command=end_data, font=("Arial", 12, "bold"), fg="red", bg="black")
end_button.grid(row=2, column=1) 

label_total_text = tk.Label(frame, text="Current balance:", font=("Arial", 12), bg="red")
label_total_text.grid(row=3, column=0) 

label_total = tk.Label(frame, text=total, font=("Arial", 14), bg="red")
label_total.grid(row=3, column=1) 

label_items = tk.Label(frame, text="", bg="red")
label_items.grid(row=4, column=0) 

label_item_list = tk.Label(frame, text="", bg="red")
label_item_list.grid(row=4, column=1)

root.mainloop()
