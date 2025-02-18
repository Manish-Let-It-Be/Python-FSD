import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('user_db.db')
cursor = conn.cursor()

# Query the User table
cursor.execute("SELECT * FROM User")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()