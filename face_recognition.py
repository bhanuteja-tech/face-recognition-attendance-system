import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import threading
from time import strftime
from datetime import datetime
import csv
import os
import messagebox

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lb1 = tk.Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="BLACK")
        title_lb1.place(x=0, y=0, width=1920, height=55)

        # Left Image
        self.img_top = Image.open(r"images/face_recog_left.jpg")  
        self.img_top = self.img_top.resize((920, 900), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(self.img_top)
        self.f_lb1 = tk.Label(self.root, image=self.photoimg_top)
        self.f_lb1.place(x=0, y=55, width=920, height=900)

        # Right Image
        self.img_bottom = Image.open(r"images/face_recog _right.jpg") 
        self.img_bottom = self.img_bottom.resize((990, 900), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(self.img_bottom)
        self.f_lb2 = tk.Label(self.root, image=self.photoimg_bottom)
        self.f_lb2.place(x=920, y=55, width=990, height=900)

        # Button
        std_b1_1 = tk.Button(self.f_lb2, text="FACE RECOGNITION", cursor="hand2", command=self.face_recog, font=("times new roman", 30, "bold"), bg="red", fg="white")
        std_b1_1.place(x=250, y=750, width=500, height=50)

    def mark_attendance(self, student_id, name, roll, dep, year):
        try:
            # Save to database
            conn = mysql.connector.connect(host="localhost", user="root", password="Bhanu@123", database="facialrecognition")
            cursor = conn.cursor()
            
            # Get current date and time
            now = datetime.now()
            date = now.strftime('%Y-%m-%d')
            time = now.strftime('%H:%M:%S')
            
            # Check if attendance already marked for today
            cursor.execute("SELECT * FROM attendance WHERE Student_ID=%s AND Date=%s", (student_id, date))
            if cursor.fetchone() is None:
                # Insert attendance record
                cursor.execute("INSERT INTO attendance (Student_ID, Name, Roll, Department, Year, Date, Time) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                             (student_id, name, roll, dep, year, date, time))
                conn.commit()

                # Save to CSV file using csv module
                # Get the absolute path to the CSV file
                csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.csv")
                
                # Check if file exists, if not create it with headers
                if not os.path.exists(csv_path):
                    with open(csv_path, "w", newline="\n") as f:
                        writer = csv.writer(f)
                        writer.writerow(["Roll No", "Name", "Department", "Year", "Date", "Time"])
                
                # Append the attendance record
                with open(csv_path, "a", newline="\n") as f:
                    writer = csv.writer(f)
                    writer.writerow([roll, name, dep, year, date, time])
                
                print(f"Attendance marked and saved to CSV: {csv_path}")
                return True
            return False
        except Exception as e:
            print(f"Error marking attendance: {str(e)}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            # Convert to grayscale
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Apply preprocessing for better recognition
            # 1. Histogram equalization for better contrast
            gray_image = cv2.equalizeHist(gray_image)
            
            # 2. Gaussian blur to reduce noise
            gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
            
            # 3. Apply adaptive thresholding
            gray_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            
            # 4. Detect faces with more robust parameters
            features = classifier.detectMultiScale(
                gray_image,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            
            coord = []
            
            for (x, y, w, h) in features:
                # Add padding around face for better recognition
                padding = 20
                y1 = max(0, y - padding)
                y2 = min(gray_image.shape[0], y + h + padding)
                x1 = max(0, x - padding)
                x2 = min(gray_image.shape[1], x + w + padding)
                
                # Extract face ROI with padding
                face_roi = gray_image[y1:y2, x1:x2]
                
                # Resize to standard size
                face_roi = cv2.resize(face_roi, (200, 200))
                
                # Apply additional preprocessing to ROI
                face_roi = cv2.equalizeHist(face_roi)
                
                # Predict with confidence threshold
                id, predict = clf.predict(face_roi)
                confidence = int(100 * (1 - predict / 300))
                
                print(f"Predicted ID: {id}, Confidence: {confidence}%")
                
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Bhanu@123",
                        database="facialrecognition"
                    )
                    cur = conn.cursor()
                    
                    # Get student details
                    cur.execute("SELECT Name, Roll, Dep, Year FROM student WHERE Student_ID=%s", (str(id),))
                    result = cur.fetchone()
                    
                    if result:
                        name, roll, dep, year = result
                        
                        # Adjust confidence threshold based on lighting conditions
                        if confidence > 50:  # Lowered threshold for better recognition
                            if self.mark_attendance(str(id), name, roll, dep, year):
                                # Draw rectangle around face
                                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                                
                                # Display student details with better formatting
                                cv2.putText(img, f"Name: {name}", (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                                cv2.putText(img, f"Roll: {roll}", (x, y-35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                                cv2.putText(img, f"Dept: {dep}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                                cv2.putText(img, f"Year: {year}", (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                                cv2.putText(img, f"Confidence: {confidence}%", (x, y+h+50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        else:
                            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                            cv2.putText(img, f"Unknown (Confidence: {confidence}%)", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                        cv2.putText(img, "Student not found in database", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    
                    conn.close()
                except Exception as e:
                    print(f"Database error: {str(e)}")
                    cv2.putText(img, "DB Error", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                
                coord = [x, y, w, h]
            
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face", clf)
            return img
        
        # Use a more robust face cascade classifier
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Check if classifier file exists
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Classifier file not found! Please train the model first.")
            return
            
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        video_cap.set(3, 640)  # Set width
        video_cap.set(4, 480)  # Set height
        
        print("Starting face recognition...")
        
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
                
            # Resize for consistent processing
            img = cv2.resize(img, (640, 480))
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)
            
            if cv2.waitKey(1) == ord('q'):
                break
        
        video_cap.release()
        cv2.destroyAllWindows()
            
                    
                
        


















        
if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition(root)
    root.mainloop()