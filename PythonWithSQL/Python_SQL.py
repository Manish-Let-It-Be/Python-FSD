# import mysql.connector

# if __name__ == '__main__':
# #User, password, host, database : required for making the connection
#     connection=mysql.connector.connect(
#         user="root",
#         password="manish",
#         database="demo_user",
#         host="localhost"
#     )

# #print(connection)

# # for pointing the database we need to create a cursor object

# cursor=connection.cursor()

# # fetching all fields from user_dat table

# query="select * from user_data"

# cursor.execute(query)

# # accessing the data from cusor object

# results=cursor.fetchall()  # this method is returning all the rows from the cursor

# for data in results:
#     print(data)




import mysql.connector

def create_user(cursor, user_name, email, phone):
    query = "INSERT INTO user_data (user_name, email, phone) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_name, email, phone))

def read_users(cursor):
    query = "SELECT * FROM user_data"
    cursor.execute(query)
    results = cursor.fetchall()
    for data in results:
        print(data)

def update_user(cursor, user_id, user_name, email, phone):
    query = "UPDATE user_data SET user_name = %s, email = %s, phone = %s WHERE id = %s"
    cursor.execute(query, (user_name, email, phone, user_id))

def delete_user(cursor, user_id):
    query = "DELETE FROM user_data WHERE id = %s"
    cursor.execute(query, (user_id,))

if __name__ == '__main__':
    connection = mysql.connector.connect(
        user="root",
        password="manish",
        database="demo_user",
        host="localhost"
    )

    cursor = connection.cursor()

    while True:
        print("\nChoose an operation:")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            user_name = input("Enter user name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            create_user(cursor, user_name, email, phone)
            print("User created successfully.")

        elif choice == '2':
            print("Users in the database:")
            read_users(cursor)

        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            user_name = input("Enter new user name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone number: ")
            update_user(cursor, user_id, user_name, email, phone)
            print("User updated successfully.")

        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(cursor, user_id)
            print("User deleted successfully.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

        # Commit changes to the database after each operation
        connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
