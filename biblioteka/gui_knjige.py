import tkinter as tk
from tkinter import messagebox
from db import Database

db = Database()

class KnjigeApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Upravljanje knjigama")
        self.geometry("400x400")

        tk.Label(self, text="Naslov").grid(row=0, column=0)
        self.entry_naslov = tk.Entry(self)
        self.entry_naslov.grid(row=0, column=1)

        tk.Label(self, text="Autor").grid(row=1, column=0)
        self.entry_autor = tk.Entry(self)
        self.entry_autor.grid(row=1, column=1)

        tk.Button(self, text="Dodaj knjigu", command=self.dodaj_knjigu).grid(row=2, column=0, columnspan=2)
        tk.Button(self, text="Obriši knjigu", command=self.obrisi_knjigu).grid(row=3, column=0, columnspan=2)

        self.lista_knjiga = tk.Listbox(self, width=50)
        self.lista_knjiga.grid(row=4, column=0, columnspan=2)
        self.osvjezi_knjige()

    def dodaj_knjigu(self):
        naslov = self.entry_naslov.get()
        autor = self.entry_autor.get()
        if naslov and autor:
            db.dodaj_knjigu(naslov, autor)
            self.osvjezi_knjige()
        else:
            messagebox.showerror("Greška", "Unesite sve podatke!")

    def obrisi_knjigu(self):
        selected = self.lista_knjiga.curselection()
        if selected:
            knjiga_id = self.lista_knjiga.get(selected[0])[0]
            db.obrisi_knjigu(knjiga_id)
            self.osvjezi_knjige()

    def osvjezi_knjige(self):
        self.lista_knjiga.delete(0, tk.END)
        for knjiga in db.dohvati_knjige():
            self.lista_knjiga.insert(tk.END, knjiga)
