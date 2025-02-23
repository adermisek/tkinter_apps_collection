import sqlite3

#povezivanje ili kreiranje s bazom podataka koja 
# se nalazi u istoj mapi kao i program
conn = sqlite3.connect('klub.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM igraci")
print(cursor.fetchall())


#ažuriranje broja dresa Luke Modrića na 7
sql_string = "UPDATE igraci SET broj_dresa = 7 WHERE ime = 'Luka' AND prezime = 'Modrić'"
t = cursor.execute(sql_string)
for _t in t:
    print(_t)

#brisanje igrača s imenom na D
sql_string_b_d = "DELETE FROM igraci WHERE ime LIKE 'D%'"
t_b_d = cursor.execute(sql_string_b_d)
for _t in t_b_d:
    print(_t)

cursor.execute("SELECT * FROM igraci")
print(cursor.fetchall())


        
# # Dohvati poziciju za messija
# cursor.execute("SELECT pozicija FROM igraci WHERE prezime = 'Messi'")
# igrac = cursor.fetchone()[0]  # Vraća tuple ili None ako student ne postoji
# print("--",igrac)

def pretrazi_po_poziciji(prezime):
    cursor.execute("SELECT pozicija FROM igraci WHERE prezime = ?", (prezime,))
    rezultat = cursor.fetchone()
    return rezultat[0] if rezultat else None

prezime_igraca = "Messi"
pozicija = pretrazi_po_poziciji(prezime_igraca)

if pozicija:
    print(f"Igrač {prezime_igraca} igra na poziciji: {pozicija}")
else:
    print(f"Igrač {prezime_igraca} nije pronađen u bazi.")




def pretrazi_po_broju(broj_dresa_igraca):
    cursor.execute("SELECT prezime FROM igraci WHERE broj_dresa = ?", (broj_dresa_igraca,))
    rezultat = cursor.fetchall()
    print("REZ:",rezultat)
    return rezultat if rezultat else None

broj_na_dresu = 10
broj = pretrazi_po_broju(broj_na_dresu)

if broj:
    print(f"Igrači s brojem {broj_na_dresu}: {', '.join(b[0] for b in broj)}")                  #mora join ne moze ici generatorski izraz
else:
    print(f"Igrač s brojem {broj_na_dresu} nije pronađen u bazi.")


conn.close()
