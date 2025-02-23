import tkinter as tk
from tkinter import messagebox
from DB_igraci import Database  # Uvoz klase Database

# Kreiranje objekta baze
db = Database()

# Funkcija za dodavanje igrača
def dodaj_igraca():
    ime = entry_ime.get()
    prezime = entry_prezime.get()
    godina_rodjenja = entry_godina.get()
    pozicija = entry_pozicija.get()
    broj_dresa = entry_broj_dresa.get()

    if ime and prezime:
        db.dodaj_igraca(ime, prezime, godina_rodjenja, pozicija,broj_dresa)  # Poziv metode iz DB klase
        prikazi_igrace()
        entry_ime.delete(0, tk.END)
        entry_prezime.delete(0, tk.END)
        entry_godina.delete(0, tk.END)
        entry_pozicija.delete(0, tk.END)
        entry_broj_dresa.delete(0, tk.END)
    else:
        messagebox.showerror("Greška", "Ime i prezime su obavezni!")

# Funkcija za brisanje igrača
def obrisi_igraca():
    odabrano = lista_igraca.curselection()  # Dohvaćamo indeks odabranog reda
    if odabrano:
        index = odabrano[0]  # Dohvaćamo indeks u Listboxu
        igrac_id = igraci_map.get(index)  # Dohvaćamo stvarni ID iz dictionarya

        if igrac_id:
            db.obrisi_igraca(igrac_id)  # Brišemo igrača iz baze
            prikazi_igrace()  # Osvježavamo Listbox
            messagebox.showinfo("Uspjeh", "Igrač obrisan!")
    else:
        messagebox.showwarning("Greška", "Molimo odaberite igrača za brisanje.")

igraci_map = {}  # Dictionary za spremanje ID-a

def prikazi_igrace():
    lista_igraca.delete(0, tk.END)
    igraci = db.dohvati_igrace()
    igraci_map.clear()  # Očisti dictionary prije dodavanja novih podataka

    for index, igrac in enumerate(igraci):
        igraci_map[index] = igrac[0]  # Pohranjujemo ID uz redni broj u Listboxu
        lista_igraca.insert(tk.END, igrac[1:])  # Dodajemo sve osim ID-a


# Kreiranje glavnog prozora
root = tk.Tk()
root.title("Baza igrača")
root.geometry("400x400")

# Okvir za unos
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Ime").grid(row=0, column=0)
entry_ime = tk.Entry(frame)
entry_ime.grid(row=0, column=1)

tk.Label(frame, text="Prezime").grid(row=1, column=0)
entry_prezime = tk.Entry(frame)
entry_prezime.grid(row=1, column=1)

tk.Label(frame, text="Godina").grid(row=2, column=0)
entry_godina = tk.Entry(frame)
entry_godina.grid(row=2, column=1)

tk.Label(frame, text="Pozicija").grid(row=3, column=0)
entry_pozicija = tk.Entry(frame)
entry_pozicija.grid(row=3, column=1)


tk.Label(frame, text="Broj dresa").grid(row=4, column=0)
entry_broj_dresa = tk.Entry(frame)
entry_broj_dresa.grid(row=4, column=1)
# Dugmad
tk.Button(root, text="Dodaj igrača", command=dodaj_igraca).pack()
tk.Button(root, text="Obriši igrača", command=obrisi_igraca).pack()

# Lista knjiga
lista_igraca = tk.Listbox(root, width=50)
lista_igraca.pack()

# Prikaz trenutnih igraca u bazi
prikazi_igrace()

# Pokretanje aplikacije
root.mainloop()


