import sqlite3

class Database:
    def __init__(self, db_name="biblioteka.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.conn.commit()
        self.create_tables()

  

    def create_tables(self):
        """ Kreiranje tablica ako ne postoje, s ON DELETE CASCADE """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS knjige (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naslov TEXT NOT NULL,
                autor TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS korisnici (
                clanska_iskaznica INTEGER PRIMARY KEY AUTOINCREMENT,
                ime TEXT NOT NULL,
                prezime TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS posudbe (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                clanska_iskaznica INTEGER NOT NULL,
                knjiga_id INTEGER NOT NULL,
                datum_posudbe TEXT NOT NULL,
                FOREIGN KEY (clanska_iskaznica) REFERENCES korisnici(clanska_iskaznica) ON DELETE CASCADE,
                FOREIGN KEY (knjiga_id) REFERENCES knjige(id) ON DELETE CASCADE
            )
        """)

        self.conn.commit()

    ### --- KNJIGE --- ###
    def dodaj_knjigu(self, naslov, autor):
        """ Dodavanje nove knjige """
        self.cursor.execute("INSERT INTO knjige (naslov, autor) VALUES (?, ?)", (naslov, autor))
        self.conn.commit()
        return True

    def dohvati_knjige(self):
        """ Dohvati sve knjige """
        self.cursor.execute("SELECT * FROM knjige")
        return self.cursor.fetchall()

    def obrisi_knjigu(self, knjiga_id):
        """ Brisanje knjige po ID-u """
        self.cursor.execute("DELETE FROM knjige WHERE id = ?", (knjiga_id,))
        if self.cursor.rowcount == 0:
            print("Greška: Knjiga s tim ID-em ne postoji!")
            return False
        self.conn.commit()
        return True

    ### --- KORISNICI --- ###
    def dodaj_korisnika(self, ime, prezime):
        """ Dodavanje korisnika - članski broj se automatski generira """
        self.cursor.execute("INSERT INTO korisnici (ime, prezime) VALUES (?, ?)", (ime, prezime))
        self.conn.commit()
        return self.cursor.lastrowid  # Vraća generirani broj članske iskaznice

    def dohvati_korisnike(self):
        """ Dohvati sve korisnike """
        self.cursor.execute("SELECT * FROM korisnici")
        return self.cursor.fetchall()

    def obrisi_korisnika(self, clanska_iskaznica):
        """ Brisanje korisnika (i automatski svih njegovih posudbi) """
        self.cursor.execute("DELETE FROM korisnici WHERE clanska_iskaznica = ?", (clanska_iskaznica,))
        print(self.cursor.execute("SELECT * FROM posudbe").fetchall())
        if self.cursor.rowcount == 0:
            print("Greška: Korisnik s tom članskom iskaznicom ne postoji!")
            return False
        self.conn.commit()
        return True

    ### --- POSUDBE --- ###
    def dodaj_posudbu(self, clanska_iskaznica, knjiga_id, datum_posudbe):
        """ Dodavanje posudbe ako korisnik i knjiga postoje """
        # Provjera postoji li korisnik
        self.cursor.execute("SELECT clanska_iskaznica FROM korisnici WHERE clanska_iskaznica = ?", (clanska_iskaznica,))
        korisnik = self.cursor.fetchone()
        if not korisnik:
            print("Greška: Korisnik s tom članskom iskaznicom ne postoji!")
            return False

        # Provjera postoji li knjiga
        self.cursor.execute("SELECT id FROM knjige WHERE id = ?", (knjiga_id,))
        knjiga = self.cursor.fetchone()
        if not knjiga:
            print("Greška: Knjiga s tim ID-em ne postoji!")
            return False

        # Dodaj posudbu
        self.cursor.execute(
            "INSERT INTO posudbe (clanska_iskaznica, knjiga_id, datum_posudbe) VALUES (?, ?, ?)",
            (clanska_iskaznica, knjiga_id, datum_posudbe)
        )
        self.conn.commit()
        return True

    def dohvati_posudbe(self):
        """ Dohvati sve posudbe """
        self.cursor.execute("SELECT * FROM posudbe")
        return self.cursor.fetchall()

    def obrisi_posudbu(self, posudba_id):
        """ Brisanje posudbe po ID-u """
        self.cursor.execute("DELETE FROM posudbe WHERE id = ?", (posudba_id,))
        
        if self.cursor.rowcount == 0:
            print("Greška: Posudba s tim ID-em ne postoji!")
            return False
        self.conn.commit()
        return True

    def close(self):
        """ Zatvori konekciju s bazom podataka """
        self.conn.close()
