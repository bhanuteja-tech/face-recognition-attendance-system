from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import csv
from tkinter import messagebox
from datetime import datetime
import os
from tkinter import filedialog


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance Management System")

        # Global variable for storing CSV data
        self.mydata = []

        # ==================== Variables ====================
        self.var_atten_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # Background image 
        img = Image.open(r"images/0899623a-1944-45cf-882e-2cf4a3c99cf6.jpg")
        img = img.resize((1920, 1080), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        # Title
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1880, height=1000)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=930, height=960)

        # Left Frame Image
        img_left = Image.open(r"images/face_recog_left.jpg")
        img_left = img_left.resize((920, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=915, height=130)

        # Left Frame Entry Fields
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=135, width=915, height=780)

        # Labels and Entry fields
        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceId_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=22, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        roll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_roll, width=22, font=("times new roman", 13, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_name, width=22, font=("times new roman", 13, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_dep, width=22, font=("times new roman", 13, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_time, width=22, font=("times new roman", 13, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_date, width=22, font=("times new roman", 13, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        self.attendance_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance, font=("times new roman", 13, "bold"), state="readonly", width=20)
        self.attendance_combo["values"] = ("Status", "Present", "Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=910, height=35)

        # Import Button
        import_btn = Button(btn_frame, text="Import CSV", command=self.import_csv, width=21, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, padx=2)

        # Export Button
        export_btn = Button(btn_frame, text="Export CSV", command=self.export_csv, width=21, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, padx=2)

        # Update Button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=21, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=2)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=21, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=2)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=950, y=10, width=920, height=960)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=900, height=900)

        # Scroll Bars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Create Treeview
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), 
                                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Configure Treeview Columns
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        # Set Column Widths
        self.AttendanceReportTable.column("id", width=120)
        self.AttendanceReportTable.column("roll", width=120)
        self.AttendanceReportTable.column("name", width=120)
        self.AttendanceReportTable.column("department", width=120)
        self.AttendanceReportTable.column("time", width=120)
        self.AttendanceReportTable.column("date", width=120)
        self.AttendanceReportTable.column("attendance", width=120)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetch_data(self):
        # Clear existing data
        for item in self.AttendanceReportTable.get_children():
            self.AttendanceReportTable.delete(item)
        
        # Populate with current data
        for i in self.mydata:
            self.AttendanceReportTable.insert("", END, values=i)

    def get_cursor(self, event=""):
        try:
            cursor_row = self.AttendanceReportTable.focus()
            content = self.AttendanceReportTable.item(cursor_row)
            rows = content['values']
            
            if rows:  # Check if any row is selected
                # Clear previous values
                self.var_atten_id.set("")
                self.var_roll.set("")
                self.var_name.set("")
                self.var_dep.set("")
                self.var_time.set("")
                self.var_date.set("")
                self.var_attendance.set("Status")
                
                # Set new values
                if len(rows) >= 1:
                    self.var_atten_id.set(rows[0])
                if len(rows) >= 2:
                    self.var_roll.set(rows[1])
                if len(rows) >= 3:
                    self.var_name.set(rows[2])
                if len(rows) >= 4:
                    self.var_dep.set(rows[3])
                if len(rows) >= 5:
                    self.var_time.set(rows[4])
                if len(rows) >= 6:
                    self.var_date.set(rows[5])
                if len(rows) >= 7:
                    self.var_attendance.set(rows[6])
                    
        except Exception as es:
            print(f"Error in get_cursor: {str(es)}")  # For debugging
            pass

    def import_csv(self):
        try:
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", 
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            
            if fln:  # Check if a file was selected
                with open(fln) as myfile:
                    csvread = csv.reader(myfile, delimiter=",")
                    self.mydata = list(csvread)  # Convert to list to store all rows
                    self.fetch_data()  # Update the display
                    messagebox.showinfo("Success", "Data imported successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def export_csv(self):
        try:
            if len(self.mydata) < 1:
                messagebox.showerror("Error", "No Data found to export", parent=self.root)
                return
            
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", 
                filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)
            
            if fln:  # Check if a filename was selected
                if not fln.endswith('.csv'):
                    fln = fln + '.csv'
                    
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in self.mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Success", "Data exported successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def update_data(self):
        selected_item = self.AttendanceReportTable.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return

        try:
            idx = self.AttendanceReportTable.index(selected_item[0])
            
            # Update the data in mydata list
            self.mydata[idx] = [
                self.var_atten_id.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_dep.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attendance.get()
            ]
            
            # Refresh the display
            self.fetch_data()
            messagebox.showinfo("Success", "Record Updated Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Status")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()



