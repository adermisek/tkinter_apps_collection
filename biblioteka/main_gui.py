import tkinter as tk
from tkinter import ttk, messagebox
import gui_posudba
import gui_users
import gui_knjige
from db import Database

db = Database()

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Biblioteka")
        self.geometry("600x500")
        self.db = db

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.books_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.books_frame, text="Knjige")

        self.users_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.users_frame, text="Korisnici")

        self.posudba_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.posudba_frame, text="Posudba")

        self.create_books_tab()
        self.create_users_tab()
        self.create_posudba_tab()

    ### --- TAB KNJIGE --- ###
    def create_books_tab(self):
        frame = tk.Frame(self.books_frame)
        frame.pack(pady=10)

        tk.Label(frame, text="Naslov").grid(row=0, column=0)
        self.entry_naslov = tk.Entry(frame)
        self.entry_naslov.grid(row=0, column=1)

        tk.Label(frame, text="Autor").grid(row=1, column=0)
        self.entry_autor = tk.Entry(frame)
        self.entry_autor.grid(row=1, column=1)

        tk.Button(self.books_frame, text="Dodaj knjigu", command=self.dodaj_knjigu).pack()
        tk.Button(self.books_frame, text="Obriši knjigu", command=self.obrisi_knjigu).pack()

        self.lista_knjiga = tk.Listbox(self.books_frame, width=50)
        self.lista_knjiga.pack()
        self.osvjezi_knjige()

    def dodaj_knjigu(self):
        naslov = self.entry_naslov.get()
        autor = self.entry_autor.get()

        if naslov and autor:
            self.db.dodaj_knjigu(naslov, autor)
            self.osvjezi_knjige()
        else:
            messagebox.showwarning("Greška", "Popunite sva polja!")

    def obrisi_knjigu(self):
        selected = self.lista_knjiga.curselection()
        if selected:
            knjiga_id = self.lista_knjiga.get(selected[0])[0]
            db.obrisi_knjigu(knjiga_id)
            self.osvjezi_knjige()
            self.osvjezi_posudbe()

    def osvjezi_knjige(self):
        self.lista_knjiga.delete(0, tk.END)
        for knjiga in db.dohvati_knjige():
            self.lista_knjiga.insert(tk.END, knjiga)

    ### --- TAB KORISNICI --- ###
    def create_users_tab(self):
        frame = tk.Frame(self.users_frame)
        frame.pack(pady=10)

        tk.Label(frame, text="Ime").grid(row=0, column=0)
        self.entry_ime = tk.Entry(frame)
        self.entry_ime.grid(row=0, column=1)

        tk.Label(frame, text="Prezime").grid(row=1, column=0)
        self.entry_prezime = tk.Entry(frame)
        self.entry_prezime.grid(row=1, column=1)

        tk.Button(self.users_frame, text="Dodaj korisnika", command=self.dodaj_korisnika).pack()
        tk.Button(self.users_frame, text="Obriši korisnika", command=self.obrisi_korisnika).pack()

        self.lista_korisnika = tk.Listbox(self.users_frame, width=50)
        self.lista_korisnika.pack()
        self.osvjezi_korisnike()

    def dodaj_korisnika(self):
        ime = self.entry_ime.get()
        prezime = self.entry_prezime.get()

        if ime and prezime:
            clanska_iskaznica = self.db.dodaj_korisnika(ime, prezime)
            messagebox.showinfo("Korisnik dodat", f"Korisnik {ime} {prezime} dodat s članskom iskaznicom {clanska_iskaznica}.")
            self.osvjezi_korisnike()
        else:
            messagebox.showwarning("Greška", "Popunite sva polja!")

    def obrisi_korisnika(self):
        selected = self.lista_korisnika.curselection()
        if selected:
            korisnik_id = self.lista_korisnika.get(selected[0])[0]
            db.obrisi_korisnika(korisnik_id)
            self.osvjezi_korisnike()
            self.osvjezi_posudbe()

    def osvjezi_korisnike(self):
        self.lista_korisnika.delete(0, tk.END)
        for korisnik in db.dohvati_korisnike():
            self.lista_korisnika.insert(tk.END, korisnik)


        ### --- TAB POSUDBA --- ###
    def create_posudba_tab(self):
        frame = tk.Frame(self.posudba_frame)
        frame.pack(pady=10)

        tk.Label(frame, text="Članska iskaznica").grid(row=0, column=0)
        self.entry_clanska_posudba = tk.Entry(frame)
        self.entry_clanska_posudba.grid(row=0, column=1)

        tk.Label(frame, text="ID Knjige").grid(row=1, column=0)
        self.entry_knjiga_id = tk.Entry(frame)
        self.entry_knjiga_id.grid(row=1, column=1)

        tk.Label(frame, text="Datum posudbe").grid(row=2, column=0)
        self.entry_datum_posudbe = tk.Entry(frame)
        self.entry_datum_posudbe.grid(row=2, column=1)

        tk.Button(self.posudba_frame, text="Dodaj posudbu", command=self.dodaj_posudbu).pack()
        tk.Button(self.posudba_frame, text="Obriši posudbu", command=self.obrisi_posudbu).pack()

        self.lista_posudbi = tk.Listbox(self.posudba_frame, width=50)
        self.lista_posudbi.pack()
        self.osvjezi_posudbe()

    def dodaj_posudbu(self):
        clanska = self.entry_clanska_posudba.get()
        knjiga_id = self.entry_knjiga_id.get()
        datum = self.entry_datum_posudbe.get()

        if clanska and knjiga_id and datum:
            self.db.dodaj_posudbu(clanska, knjiga_id, datum)
            self.osvjezi_posudbe()
        else:
            messagebox.showwarning("Greška", "Popunite sva polja!")

    def obrisi_posudbu(self):
        selected = self.lista_posudbi.curselection()
        if selected:
            posudba_id = self.lista_posudbi.get(selected[0])[0]
            db.obrisi_posudbu(posudba_id)
            self.osvjezi_posudbe()

    def osvjezi_posudbe(self):
        self.lista_posudbi.delete(0, tk.END)
        for posudba in db.dohvati_posudbe():
            self.lista_posudbi.insert(tk.END, posudba)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
