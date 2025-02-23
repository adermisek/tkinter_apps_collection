import tkinter as tk
from tkinter import messagebox
from db import Database

db = Database()

class UsersApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Upravljanje korisnicima")
        self.geometry("500x400")

        self.create_widgets()
        self.refresh_users()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="Ime").grid(row=0, column=0)
        self.entry_ime = tk.Entry(frame)
        self.entry_ime.grid(row=0, column=1)

        tk.Label(frame, text="Prezime").grid(row=1, column=0)
        self.entry_prezime = tk.Entry(frame)
        self.entry_prezime.grid(row=1, column=1)

        tk.Button(self, text="Dodaj korisnika", command=self.add_user).pack()
        tk.Button(self, text="Obriši korisnika", command=self.delete_user).pack()

        self.lista_korisnika = tk.Listbox(self, width=50)
        self.lista_korisnika.pack()

    def add_user(self):
        ime = self.entry_ime.get()
        prezime = self.entry_prezime.get()

        if ime and prezime:
            clanska_iskaznica = db.dodaj_korisnika(ime, prezime)
            messagebox.showinfo("Korisnik dodat", f"Korisnik {ime} {prezime} dodat s članskom iskaznicom {clanska_iskaznica}.")
            self.refresh_users()
        else:
            messagebox.showwarning("Greška", "Popunite sva polja!")

    def delete_user(self):
        selected = self.lista_korisnika.curselection()
        if selected:
            korisnik_id = self.lista_korisnika.get(selected[0]).split()[0]
            db.obrisi_korisnika(korisnik_id)
            self.refresh_users()

    def refresh_users(self):
        self.lista_korisnika.delete(0, tk.END)
        for korisnik in db.dohvati_korisnike():
            self.lista_korisnika.insert(tk.END, korisnik)

