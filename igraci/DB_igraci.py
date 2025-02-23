import sqlite3

class Database:
    def __init__(self, db_name="klub.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table_igraci()

    def create_table_igraci(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS igraci (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ime TEXT,
            prezime TEXT,
            godina_rodjenja INTEGER,
            pozicija TEXT,
            broj_dresa INTEGER
        )''')
        self.conn.commit()

    def dodaj_igraca(self, ime, prezime, godina_rodjenja='', pozicija='', broj_dresa=0):
        self.c.execute("INSERT INTO igraci (ime, prezime, godina_rodjenja, pozicija,broj_dresa) VALUES (?, ?, ?, ?,?)",
                  (ime, prezime, godina_rodjenja, pozicija,broj_dresa))
        self.conn.commit()

    def dohvati_igrace(self):
        self.c.execute("SELECT * FROM igraci")
        return self.c.fetchall()

    def obrisi_igraca(self, igrac_id):
        self.c.execute("DELETE FROM igraci WHERE id=?", (igrac_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
