import mysql.connector

if __name__ == '__main__':
#User, password, host, database : required for making the connection
    connection=mysql.connector.connect(
        user="root",
        password="manish",
        database="demo_user",
        host="localhost"
    )

#print(connection)

# for pointing the database we need to create a cursor object

cursor=connection.cursor()

# fetching all fields from user_dat table

query="select * from user_data"

cursor.execute(query)

# accessing the data from cusor object

results=cursor.fetchall()  # this method is returning all the rows from the cursor

for data in results:
    print(data)
