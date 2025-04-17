import csv

def create_attendance_csv():
    try:
        # Create attendance.csv with headers if it doesn't exist
        with open("attendance.csv", "w", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll No", "Name", "Department", "Year", "Date", "Time"])
        print("Attendance CSV file created successfully!")
    except Exception as e:
        print(f"Error creating attendance CSV file: {str(e)}")

if __name__ == "__main__":
    create_attendance_csv() 