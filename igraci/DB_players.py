import sqlite3

class Database:
    def __init__(self, db_name="club.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table_players()

    def create_table_players(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            birth_year INTEGER,
            position TEXT,
            jersey_number INTEGER
        )''')
        self.conn.commit()

    def add_player(self, first_name, last_name, birth_year='', position='', jersey_number=0):
        self.c.execute("INSERT INTO players (first_name, last_name, birth_year, position, jersey_number) VALUES (?, ?, ?, ?, ?)",
                       (first_name, last_name, birth_year, position, jersey_number))
        self.conn.commit()

    def get_players(self):
        self.c.execute("SELECT * FROM players")
        return self.c.fetchall()

    def delete_player(self, player_id):
        self.c.execute("DELETE FROM players WHERE id=?", (player_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
