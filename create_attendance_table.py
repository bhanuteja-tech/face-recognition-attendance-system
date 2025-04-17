import mysql.connector

def create_attendance_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bhanu@123",
            database="facialrecognition"
        )
        cursor = conn.cursor()
        
        # Create attendance table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Student_ID VARCHAR(50),
                Name VARCHAR(100),
                Roll VARCHAR(50),
                Department VARCHAR(50),
                Year VARCHAR(50),
                Date DATE,
                Time TIME
            )
        """)
        
        conn.commit()
        print("Attendance table created successfully!")
        
    except Exception as e:
        print(f"Error creating attendance table: {str(e)}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_attendance_table() 