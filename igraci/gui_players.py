import tkinter as tk
from tkinter import messagebox, ttk
from DB_players import Database  # Import Database class

# Create database object
db = Database()

# Function to add a player
def add_player():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    birth_year = entry_birth_year.get()
    position = entry_position.get()
    jersey_number = entry_jersey_number.get()

    if first_name and last_name:
        db.add_player(first_name, last_name, birth_year, position, jersey_number)  # Call method from DB class
        display_players()
        entry_first_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_birth_year.delete(0, tk.END)
        entry_position.delete(0, tk.END)
        entry_jersey_number.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "First name and last name are required!")

# Function to delete a player
def delete_player():
    selected = player_list.curselection()  # Get selected row index
    if selected:
        index = selected[0]  # Get index in Listbox
        player_id = players_map.get(index)  # Retrieve actual ID from dictionary

        if player_id:
            db.delete_player(player_id)  # Delete player from database
            display_players()  # Refresh Listbox
            messagebox.showinfo("Success", "Player deleted!")
    else:
        messagebox.showwarning("Error", "Please select a player to delete.")

players_map = {}  # Dictionary to store player IDs

def display_players():
    player_list.delete(0, tk.END)
    players = db.get_players()
    players_map.clear()  # Clear dictionary before adding new data

    for index, player in enumerate(players):
        players_map[index] = player[0]  # Store ID with row index in Listbox
        player_list.insert(tk.END, player[1:])  # Add everything except ID

# Create main window
root = tk.Tk()
root.title("Player Database")
root.geometry("400x400")

# Input frame
frame = ttk.LabelFrame(root, text="Add Player", padding=10)
frame.pack(pady=10, padx=10, fill="both")

ttk.Label(frame, text="First Name").grid(row=0, column=0)
entry_first_name = ttk.Entry(frame)
entry_first_name.grid(row=0, column=1)

ttk.Label(frame, text="Last Name").grid(row=1, column=0)
entry_last_name = ttk.Entry(frame)
entry_last_name.grid(row=1, column=1)

ttk.Label(frame, text="Birth Year").grid(row=2, column=0)
entry_birth_year = ttk.Entry(frame)
entry_birth_year.grid(row=2, column=1)

ttk.Label(frame, text="Position").grid(row=3, column=0)
entry_position = ttk.Entry(frame)
entry_position.grid(row=3, column=1)

ttk.Label(frame, text="Jersey Number").grid(row=4, column=0)
entry_jersey_number = ttk.Entry(frame)
entry_jersey_number.grid(row=4, column=1)

# Buttons
ttk.Button(root, text="Add Player", command=add_player).pack(pady=5)
ttk.Button(root, text="Delete Player", command=delete_player).pack()

# Player list
player_list = tk.Listbox(root, width=50)
player_list.pack(pady=10)

# Display existing players
display_players()

# Run application
root.mainloop()
