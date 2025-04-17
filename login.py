from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import errorcode
import os
from main import Face_Recognition_System
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Bhanu@123",
    "database": "facialrecognition"
}

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")
        
        # Variables
        self.username_var = StringVar()
        self.password_var = StringVar()
        
        # Background Image
        img = Image.open(r"images/Login.jpg")  
        img = img.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Header Image with Faces
        header_img = Image.open(r"images/login_header.jpg")  
        header_img = header_img.resize((650, 180), Image.LANCZOS)
        self.header_photo = ImageTk.PhotoImage(header_img)
        
        header_label = Label(self.root, image=self.header_photo)
        header_label.place(x=0, y=0, width=650, height=140)


         #Second heade image 
        img1=Image.open(r"images/Faceimage.jpg")
        img1=img1.resize((650,180),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=650,y=0,width=650,height=140)
        
        #Third header image 
        img2=Image.open(r"images/Worldimage.jpg")
        img2=img2.resize((650,180),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1300,y=0,width=600,height=140)

        
        # Title
        title = Label(self.root, text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM", 
                     font=("times new roman", 35, "bold"), bg="white", fg="red")
        title.place(x=0, y=130, width=1920, height=45)
        
        # Login Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=200, width=700, height=500)
        

        # Get Started Label
        get_started = Label(frame, text="Get Started", font=("times new roman", 25, "bold"), fg="white", bg="black")
        get_started.place(x=0, y=120, relwidth=1)

        # Profile icon
        profile_img = Image.open(r"images/login_profile_icon.jpeg")  
        profile_img = profile_img.resize((100, 100), Image.LANCZOS)
        self.profile_photo = ImageTk.PhotoImage(profile_img)
        profile_label = Label(frame, image=self.profile_photo, bg="black")
        profile_label.place(x=300, y=10, width=100, height=100)


        # Username/Email Label
        email_label = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="black")
        email_label.place(x=150, y=220)
        self.txtuser = ttk.Entry(frame, textvariable=self.username_var, font=("times new roman", 15))
        self.txtuser.place(x=150, y=250, width=400)
        
        # Password Label
        pass_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        pass_label.place(x=150, y=290)
        self.txtpass = ttk.Entry(frame, textvariable=self.password_var, show="*", font=("times new roman", 15))
        self.txtpass.place(x=150, y=320, width=400)
        
        # Login Button
        login_btn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), 
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        login_btn.place(x=150, y=370, width=400, height=35)

        # Register and Forgot Password Links
        register_btn = Button(frame, text="New User Register", command=self.register_window, 
                            font=("times new roman", 12), borderwidth=0, fg="white", bg="black", 
                            activeforeground="white", activebackground="black")
        register_btn.place(x=150, y=420)

        forgot_btn = Button(frame, text="Forgot Password", command=self.forgot_password_window,
                          font=("times new roman", 12), borderwidth=0, fg="white", bg="black",
                          activeforeground="white", activebackground="black")
        forgot_btn.place(x=450, y=420)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def connect_db(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            return conn
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                messagebox.showerror("Error", "Database access denied. Check credentials.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                messagebox.showerror("Error", "Database does not exist")
            else:
                messagebox.showerror("Error", f"Database connection failed: {err}")
            return None

    def login(self):
        if self.username_var.get() == "" or self.password_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = self.connect_db()
            if conn is None:
                return
            try:
                cur = conn.cursor()
                
                # Add login attempt tracking
                cur.execute("SELECT login_attempts, last_attempt FROM register WHERE email=%s", 
                           (self.username_var.get(),))
                attempt_row = cur.fetchone()
                
                if attempt_row and attempt_row[0] >= 3:  # Max 3 attempts
                    last_attempt = attempt_row[1]
                    if (datetime.now() - last_attempt).total_seconds() < 300:  # 5 minutes lockout
                        messagebox.showerror("Error", "Account locked. Try again in 5 minutes")
                        return
                
                cur.execute("SELECT * FROM register WHERE email=%s AND password=%s",
                           (self.username_var.get(), self.password_var.get()))
                row = cur.fetchone()
                
                if row is None:
                    # Update failed attempts
                    cur.execute("UPDATE register SET login_attempts = login_attempts + 1, last_attempt = NOW() WHERE email=%s",
                              (self.username_var.get(),))
                    conn.commit()
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    # Reset attempts on successful login
                    cur.execute("UPDATE register SET login_attempts = 0 WHERE email=%s",
                              (self.username_var.get(),))
                    conn.commit()
                    
                    open_main = messagebox.askyesno("Access", "Access only admin")
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
                    
                conn.close()
                
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")
            
    def forgot_password_window(self):
        if self.username_var.get() == "":
            messagebox.showerror("Error", "Please enter email to reset password")
        else:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cur = conn.cursor()
                cur.execute("select * from register where email=%s", (self.username_var.get(),))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Please enter valid username")
                else:
                    conn.close()
                    self.root2 = Toplevel()
                    self.root2.title("Reset Password")
                    self.root2.geometry("340x450+610+170")
                    
                    # Add security question verification
                    l = Label(self.root2, text="Reset Password", font=("times new roman", 20, "bold"))
                    l.place(x=0, y=10, relwidth=1)
                    
                    # Security Question
                    security_q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"))
                    security_q.place(x=50, y=80)
                    
                    # Replace Entry with Combobox for security questions
                    self.security_q_combo = ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly")
                    self.security_q_combo["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Mother Name")
                    self.security_q_combo.place(x=50, y=110, width=250)
                    self.security_q_combo.current(0)
                    
                    # Security Answer
                    security_a = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"))
                    security_a.place(x=50, y=150)
                    self.security_a_entry = ttk.Entry(self.root2, font=("times new roman", 15))
                    self.security_a_entry.place(x=50, y=180, width=250)
                    
                    # New Password
                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"))
                    new_password.place(x=50, y=220)
                    self.new_password_entry = ttk.Entry(self.root2, font=("times new roman", 15), show="*")
                    self.new_password_entry.place(x=50, y=250, width=250)
                    
                    # Reset Button
                    reset_btn = Button(self.root2, text="Reset", command=self.reset_password,
                                     font=("times new roman", 15, "bold"), fg="white", bg="green")
                    reset_btn.place(x=100, y=300, width=150)
                    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")
            
    def reset_password(self):
        if self.security_q_combo.get() == "Select" or self.security_a_entry.get() == "" or self.new_password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cur = conn.cursor()
                
                # Verify security question and answer
                cur.execute("SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s",
                          (self.username_var.get(), self.security_q_combo.get(), self.security_a_entry.get()))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid security question or answer", parent=self.root2)
                else:
                    # Update password
                    cur.execute("UPDATE register SET password=%s WHERE email=%s",
                              (self.new_password_entry.get(), self.username_var.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Password reset successful", parent=self.root2)
                    self.root2.destroy()
                    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root2)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # First header image  
        img = Image.open(r"images/Backgroundimage.jpg")
        img = img.resize((650, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=650, height=140)
        
        # Second header image 
        img1 = Image.open(r"images/Faceimage.jpg")
        img1 = img1.resize((650, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=650, y=0, width=650, height=140)
        
        # Third header image 
        img2 = Image.open(r"images/Worldimage.jpg")
        img2 = img2.resize((650, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1300, y=0, width=600, height=140)

        # Background image 
        bg1 = Image.open(r"images/0899623a-1944-45cf-882e-2cf4a3c99cf6.jpg")
        bg1 = bg1.resize((1920, 1080), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1920, height=1080)

        # Title section
        title_lbl = Label(bg_img, text="REGISTRATION SYSTEM", 
                         font=("times new roman", 35, "bold"), bg="white", fg="BLACK")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=320, y=55, width=1280, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                              text="Registration Details", font=("times new roman", 20, "bold"))
        left_frame.place(x=10, y=10, width=1260, height=580)

        # Labels and entry fields
        # First name
        fname = Label(left_frame, text="First Name:", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=50)
        self.fname_entry = ttk.Entry(left_frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=50, y=80, width=250)

        # Last name
        l_name = Label(left_frame, text="Last Name:", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=50)
        self.txt_lname = ttk.Entry(left_frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=80, width=250)

        # Contact
        contact = Label(left_frame, text="Contact No:", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=130)
        self.txt_contact = ttk.Entry(left_frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=160, width=250)

        # Email
        email = Label(left_frame, text="Email:", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=130)
        self.txt_email = ttk.Entry(left_frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=160, width=250)

        # Security Question
        security_Q = Label(left_frame, text="Select Security Question:", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=210)
        self.combo_security_Q = ttk.Combobox(left_frame, textvariable=self.var_securityQ, 
                                           font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Mother Name")
        self.combo_security_Q.place(x=50, y=240, width=250)
        self.combo_security_Q.current(0)

        # Security Answer
        security_A = Label(left_frame, text="Security Answer:", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=210)
        self.txt_security = ttk.Entry(left_frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=240, width=250)

        # Password
        pswd = Label(left_frame, text="Password:", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=290)
        self.txt_pswd = ttk.Entry(left_frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=320, width=250)

        # Confirm Password
        confirm_pswd = Label(left_frame, text="Confirm Password:", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=290)
        self.txt_confirm_pswd = ttk.Entry(left_frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=370, y=320, width=250)

        # Buttons Frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=50, y=400, width=570, height=70)

        # Register Button
        register_btn = Button(btn_frame, text="Register", command=self.register_data, 
                            font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                            fg="white", bg="green", activeforeground="white", activebackground="green")
        register_btn.place(x=50, y=10, width=200, height=50)

        # Login Button
        login_btn = Button(btn_frame, text="Login", command=self.return_login,
                          font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                          fg="white", bg="blue", activeforeground="white", activebackground="blue")
        login_btn.place(x=320, y=10, width=200, height=50)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & confirm password must be same")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Bhanu@123",
                    database="facialrecognition"
                )
                cur = conn.cursor()
                cur.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
                row = cur.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    cur.execute("""
                        INSERT INTO register 
                        (fname, lname, contact, email, securityQ, securityA, password, login_attempts, last_attempt) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get(),
                        0,  # initial login_attempts
                        None  # initial last_attempt
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Register Successfully")
                    self.root.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}")

    def return_login(self):
        self.root.destroy()

    def validate_email(self, email):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_password(self, password):
        # Minimum 8 characters, at least one letter and one number
        import re
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        return re.match(pattern, password) is not None

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
