# Importing required libraries
import mysql.connector
from mysql.connector import Error

# Establish connection to the MySQL server
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="sa",  # Replace with your MySQL username
            password="ReportingUser"  # Replace with your MySQL password
        )
        if conn.is_connected():
            print("Connected to MySQL Server successfully!")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# Create a database
def create_database(cursor, db_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database `{db_name}` created or already exists.")
    except Error as e:
        print(f"Error: {e}")

# Use a specific database
def use_database(cursor, db_name):
    try:
        cursor.execute(f"USE {db_name}")
        print(f"Using database `{db_name}`.")
    except Error as e:
        print(f"Error: {e}")

# Create a table
def create_table(cursor):
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE,
            age INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        print("Table `users` created or already exists.")
    except Error as e:
        print(f"Error: {e}")

# Insert data into the table
def insert_data(cursor, conn):
    try:
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", 
                       ("Alice", "alice@example.com", 25))
        users = [
            ("Bob", "bob@example.com", 30),
            ("Charlie", "charlie@example.com", 35)
        ]
        cursor.executemany("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", users)
        conn.commit()
        print("Data inserted into table.")
    except Error as e:
        print(f"Error: {e}")

# Query data from the table
def query_data(cursor):
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("Retrieved data:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

# Update data in the table
def update_data(cursor, conn):
    try:
        cursor.execute("UPDATE users SET age = %s WHERE name = %s", (26, "Alice"))
        conn.commit()
        print("Data updated successfully.")
    except Error as e:
        print(f"Error: {e}")

# Delete data from the table
def delete_data(cursor, conn):
    try:
        cursor.execute("DELETE FROM users WHERE name = %s", ("Charlie",))
        conn.commit()
        print("Data deleted successfully.")
    except Error as e:
        print(f"Error: {e}")

# Drop the table
def drop_table(cursor):
    try:
        cursor.execute("DROP TABLE IF EXISTS users")
        print("Table `users` dropped.")
    except Error as e:
        print(f"Error: {e}")

# Main function to execute all operations
def main():
    # Step 1: Connect to MySQL server
    conn = connect_to_mysql()
    if conn is None:
        return
    cursor = conn.cursor()

    # Step 2: Create and use a database
    create_database(cursor, "test_db")
    use_database(cursor, "test_db")

    # Step 3: Create a table
    create_table(cursor)

    # Step 4: Insert data
    insert_data(cursor, conn)

    # Step 5: Query data
    query_data(cursor)

    # Step 6: Update data
    update_data(cursor, conn)
    query_data(cursor)

    # # Step 7: Delete data
    # delete_data(cursor, conn)
    # query_data(cursor)

    # # Step 8: Drop the table
    # drop_table(cursor)

    # Step 9: Close the connection
    cursor.close()
    conn.close()
    print("Database connection closed.")

# Run the main function
if __name__ == "__main__":
    main()
