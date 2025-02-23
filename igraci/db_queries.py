import sqlite3

# Connect to or create a database located in the same folder as the program
conn = sqlite3.connect('club.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM players")
print(cursor.fetchall())

# Update Luka Modrić's jersey number to 7
sql_update = "UPDATE players SET jersey_number = 7 WHERE first_name = 'Luka' AND last_name = 'Modrić'"
cursor.execute(sql_update)
conn.commit()

# Delete players whose first name starts with "D"
sql_delete = "DELETE FROM players WHERE first_name LIKE 'D%'"
cursor.execute(sql_delete)
conn.commit()

cursor.execute("SELECT * FROM players")
print(cursor.fetchall())

# Function to search for a player's position by last name
def search_by_position(last_name):
    cursor.execute("SELECT position FROM players WHERE last_name = ?", (last_name,))
    result = cursor.fetchone()
    return result[0] if result else None

player_last_name = "Messi"
position = search_by_position(player_last_name)

if position:
    print(f"Player {player_last_name} plays as: {position}")
else:
    print(f"Player {player_last_name} was not found in the database.")

# Function to search for players by jersey number
def search_by_jersey_number(jersey_number):
    cursor.execute("SELECT last_name FROM players WHERE jersey_number = ?", (jersey_number,))
    result = cursor.fetchall()
    return result if result else None

jersey_num = 10
players_with_number = search_by_jersey_number(jersey_num)

if players_with_number:
    print(f"Players with jersey number {jersey_num}: {', '.join(p[0] for p in players_with_number)}")
else:
    print(f"No players found with jersey number {jersey_num}.")

conn.close()
