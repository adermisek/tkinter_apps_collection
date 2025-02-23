import tkinter as tk
from tkinter import ttk, messagebox
from db import Database

db = Database()

class PosudbaApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Upravljanje posudbama")
        self.geometry("500x400")

        self.create_widgets()
        self.refresh_loans()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="Članska iskaznica").grid(row=0, column=0)
        self.entry_clanska = tk.Entry(frame)
        self.entry_clanska.grid(row=0, column=1)

        tk.Label(frame, text="ID Knjige").grid(row=1, column=0)
        self.entry_knjiga_id = tk.Entry(frame)
        self.entry_knjiga_id.grid(row=1, column=1)

        tk.Label(frame, text="Datum posudbe (YYYY-MM-DD)").grid(row=2, column=0)  # Novo polje
        self.entry_datum = tk.Entry(frame)
        self.entry_datum.grid(row=2, column=1)

        tk.Button(self, text="Dodaj posudbu", command=self.add_loan).pack()
        tk.Button(self, text="Obriši posudbu", command=self.delete_loan).pack()

        self.lista_posudbi = tk.Listbox(self, width=50)
        self.lista_posudbi.pack()

    def add_loan(self):
        clanska = self.entry_clanska.get()
        knjiga_id = self.entry_knjiga_id.get()
        datum = self.entry_datum.get()

        if clanska and knjiga_id and datum:
            db.dodaj_posudbu(clanska, knjiga_id, datum)
            self.refresh_loans()
        else:
            messagebox.showwarning("Greška", "Popunite sva polja!")

    def delete_loan(self):
        selected = self.lista_posudbi.curselection()
        if selected:
            posudba_id = self.lista_posudbi.get(selected[0]).split()[0]
            db.obrisi_posudbu(posudba_id)
            self.refresh_loans()

    def refresh_loans(self):
        self.lista_posudbi.delete(0, tk.END)
        for posudba in db.dohvati_posudbe():
            self.lista_posudbi.insert(tk.END, posudba)

