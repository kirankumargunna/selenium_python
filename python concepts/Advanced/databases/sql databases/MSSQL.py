import pyodbc

# Connect to MSSQL server
def connect_to_mssql():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"  # Ensure the correct ODBC driver is installed
            "SERVER=COGNINE-L135\ADMINUSER;"  # Replace with your server name or IP
            "DATABASE=master;"  # Default database
            "UID=sa;"  # Replace with your MSSQL username
            "PWD=ReportingUser;"  # Replace with your MSSQL password
        )
        conn.autocommit = True  # Enable autocommit for CREATE DATABASE
        print("Connected to MSSQL Server successfully!")
        return conn
    except pyodbc.Error as e:
        print(f"Error: {e}")
        return None

# Main function
def main():
    conn = connect_to_mssql()
    if conn is None:
        return
    cursor = conn.cursor()

    # Create and use database
    try:
        cursor.execute("CREATE DATABASE test_db")
        print("Database created.")
    except pyodbc.Error as e:
        print(f"Error: {e}")

    try:
        cursor.execute("USE test_db")
        print("Switched to database test_db.")
    except pyodbc.Error as e:
        print(f"Error: {e}")

    # Create table
    try:
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' AND xtype='U')
        CREATE TABLE users (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name NVARCHAR(255) NOT NULL,
            email NVARCHAR(255) UNIQUE,
            age INT,
            created_at DATETIME DEFAULT GETDATE()
        )
        """)
        print("Table created or already exists.")
    except pyodbc.Error as e:
        print(f"Error: {e}")

    # Insert data
    try:
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                       ("Alice", "alice@example.com", 25))
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                       ("Bob", "bob@example.com", 30))
        conn.commit()
        print("Data inserted.")
    except pyodbc.Error as e:
        print(f"Error: {e}")

    # Query data
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("Retrieved data:")
        for row in rows:
            print(row)
    except pyodbc.Error as e:
        print(f"Error: {e}")

    # Drop table
    try:
        cursor.execute("DROP TABLE users")
        print("Table dropped.")
    except pyodbc.Error as e:
        print(f"Error: {e}")

    # Close connection
    cursor.close()
    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()


