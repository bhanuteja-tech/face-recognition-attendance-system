import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Bhanu@123",
    "database": "facialrecognition"
}

def create_register_table():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Drop existing table if it exists
        cursor.execute("DROP TABLE IF EXISTS register")
        
        # Create register table with all required columns
        cursor.execute("""
            CREATE TABLE register (
                fname VARCHAR(45),
                lname VARCHAR(45),
                contact VARCHAR(45),
                email VARCHAR(45) PRIMARY KEY,
                securityQ VARCHAR(45),
                securityA VARCHAR(45),
                password VARCHAR(45),
                login_attempts INT DEFAULT 0,
                last_attempt DATETIME
            )
        """)
        
        conn.commit()
        print("Register table created successfully!")
        
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_register_table()