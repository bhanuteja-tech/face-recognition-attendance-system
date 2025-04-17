from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import cv2
import mysql.connector
from tkcalendar import DateEntry


class Student:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Management System")


        # ---------------------- variables --------------------

        self.var_Dep = StringVar()
        self.var_course = StringVar()
        self.var_Year = StringVar()
        self.var_Semester = StringVar()
        self.var_std_ID = StringVar()
        self.var_std_name = StringVar()
        self.var_Div = StringVar()
        self.var_Roll = StringVar()
        self.var_Gender = StringVar()
        self.var_DOB = StringVar()
        self.var_Email = StringVar()
        self.var_Mobile = StringVar()
        self.var_Address = StringVar()
        self.var_Teacher = StringVar()


        # first header image  
        img=Image.open(r"images/Backgroundimage.jpg")
        img=img.resize((650,180),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=650,height=140)
        
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


        #backgorund image 
        bg1=Image.open(r"images/0899623a-1944-45cf-882e-2cf4a3c99cf6.jpg")
        bg1=bg1.resize((1920,1080),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1920,height=1080)


        #title section
        title_lb1 = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="BLACK")
        title_lb1.place(x=0,y=0,width=1920,height=40)
        
        
        #Creating a main frame 
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=0,y=50,width=1910,height=1000)

        #left label frame

        Left_frame =LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=5,y=10,width=930,height=800)
        
        
        #Right Frame
        Right_frame =LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=940,y=10,width=960,height=800)


        #Header image 
        img_left=Image.open(r"images/llll.jpg")
        img_left=img_left.resize((920,400),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        # set image as lable
        f_lb1 = Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=920,height=140)


        # ------ courses ------

        #Current course

        current_course_frame =LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        current_course_frame.place(x=5,y=145,width=920,height=150)
        
        #Department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=("times new roman",15,"bold"),state="readonly")
        dep_combo["values"] = ("Select Department","Computer Science","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course

        course_label = Label(current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",15,"bold"),state="readonly",width=20)
        course_combo["values"] = ("Select Course","BTech","BCA","MCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year

        year_label = Label(current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",15,"bold"),state="readonly",width=17)
        year_combo["values"] = ("Select Year","1st Year","2nd Year","3rd Year","4th year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester

        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Semester,font=("times new roman",15,"bold"),state="readonly",width=17)
        semester_combo["values"] = ("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Class Student Information

        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",15,"bold")) 
        class_student_frame.place(x=5,y=300,width=920,height=470)

        #Student_id

        studentid_label = Label(class_student_frame,text="StudentID:",font=("times new roman",15,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        studentid_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_ID,width=20,font=("times new roman",15,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student_name

        studentname_label = Label(class_student_frame,text="Student Name:",font=("times new roman",15,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        studentname_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",15,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

      #---- class divison -----

        class_div_label = Label(class_student_frame,text="Class divison:",font=("times new roman",15,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        class_div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_Div,font=("times new roman",15,"bold"),state="readonly",width=18)
        class_div_combo["values"] = ("Select Class Divison","First","Second","Third")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=0,sticky=W)

      #---- Roll No ----

        roll_no_label = Label(class_student_frame,text="Roll No:",font=("times new roman",15,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_Roll,width=20,font=("times new roman",15,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W) 

      #---- Gender ----

        gender_label = Label(class_student_frame,text="Gender:",font=("times new roman",15,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("times new roman",15,"bold"),state="readonly",width=18)
        gender_combo["values"] = ("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=0,sticky=W)

      # ----- DOB ----

        dob_label = Label(class_student_frame,text="DOB:",font=("times new roman",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        dob_entry = DateEntry(class_student_frame, width=18, textvariable=self.var_DOB, font=("times new roman", 15, "bold"), bg="white", date_pattern="dd/mm/yyyy")
        dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

      #----- Email_ID ----

        email_label = Label(class_student_frame,text="Email ID:",font=("times new roman",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_Email,width=20,font=("times new roman",15,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

      #----- Phone number ----

        phone_label = Label(class_student_frame,text="Mobile No:",font=("times new roman",15,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_Mobile,width=20,font=("times new roman",15,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

      # ---- Address -----
        address_label = Label(class_student_frame,text="Address:",font=("times new roman",15,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_Address,width=20,font=("times new roman",15,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)  

      #---- Teacher -----

        teacher_label = Label(class_student_frame,text="Class Teacher:",font=("times new roman",15,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_Teacher,width=20,font=("times new roman",15,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

      #--------------------------------------------  Radio Buttons ------------------------------------------
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=10,pady=35)

      # ----- Radio button 2 ----
        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=6,column=1,padx=50,pady=35,sticky=W)

      #--------------------------------------------------- Button Frame --------------------------------------------------   #bd = border

        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=310,width=915,height=100)
      
      # save Button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",15,"bold"))
        save_btn.grid(row=0,column=0)

      # Update Button

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",15,"bold"))
        update_btn.grid(row=0,column=1)

      # Delete Button

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",15,"bold"))
        delete_btn.grid(row=0,column=2)

      #reset button

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",15,"bold"))
        reset_btn.grid(row=0,column=3)

      #Photo sample

        btn_frame1 =Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=370,width=920,height=60)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=40,height=2,font=("times new roman",15,"bold"))
        take_photo_btn.grid(row=0,column=0)

      # #Update photo sample button

        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=35,height=2,font=("times new roman",15,"bold"))
        update_photo_btn.grid(row=0,column=1)


        #-----------------------------------------------------------------------  Right Frame information -------------------------------------------------------------------------------------

        Right_frame =LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=940,y=10,width=960,height=800)

        img_right=Image.open(r"images/Current_course info.jpg")
        img_right=img_right.resize((947,420),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        # set image as label
        f_lb1 = Label(Right_frame,image=self.photoimg_right)
        f_lb1.place(x=5,y=0,width=947,height=140)

        # ---------------------------------------------- Creation of search frame ------------------------------------------

        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, 
                                 text="Search System", font=("times new roman", 15, "bold"))
        search_frame.place(x=5, y=145, width=947, height=150)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), 
                            bg="white", fg="black")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # Create Combobox for search criteria
        self.search_combo = ttk.Combobox(search_frame, font=("times new roman", 15, "bold"), 
                                        state="readonly", width=17)
        self.search_combo["values"] = ("Select", "Student_ID", "Mobile_No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Create Entry field for search value
        self.search_entry = ttk.Entry(search_frame, width=17, font=("times new roman", 15, "bold"))
        self.search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        # Search button
        search_btn = Button(search_frame, text="Search", command=self.search_data,
                           width=16, font=("times new roman", 15, "bold"))
        search_btn.grid(row=0, column=3, padx=4)

        # Show All button
        showall_btn = Button(search_frame, text="Show All", command=self.fetch_data,
                            width=16, font=("times new roman", 15, "bold"))
        showall_btn.grid(row=0, column=4, padx=4)


        #----------------------------------------------- Table Frame --------------------------------------------------------

        table_frame =Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=311,width=947,height=458)

        #----- scroll bar -----

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("Dep","course","Year","Sem","ID","Name","Div","Roll","Gender","DOB","E-mail","Mobile","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Divison")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("E-mail",text="E-mail")
        self.student_table.heading("Mobile",text="Mobile")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("Dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        

        self.student_table.column("DOB",width=100)
        self.student_table.column("E-mail",width=190)
        self.student_table.column("Mobile",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # --------------------- Function Declaration to Add_Data --------------------------------

    def add_data(self):

        if self.var_Dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_ID.get() == "":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
              conn = mysql.connector.connect(host="localhost",user="root",password="Bhanu@123",database="facialrecognition")
              
              my_cursor = conn.cursor()
              my_cursor.execute("insert into student(Dep, course, Year, Semester, Student_ID, Name, Divison, Roll, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_Dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_Year.get(),
                                                                                                            self.var_Semester.get(),
                                                                                                            self.var_std_ID.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_Div.get(),
                                                                                                            self.var_Roll.get(),
                                                                                                            self.var_Gender.get(),
                                                                                                            self.var_DOB.get(),
                                                                                                            self.var_Email.get(),
                                                                                                            self.var_Mobile.get(),
                                                                                                            self.var_Address.get(),
                                                                                                            self.var_Teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                        ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # ------------------------------------------------------------------ fetch data -----------------------------------------------------------------------------

    def fetch_data(self):

        conn = mysql.connector.connect(host="localhost",user="root",password="Bhanu@123",database="facialrecognition")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

  # # --------------------------------------------------------------------- get cursor ---------------------------------------------------------------------------

    def get_cursor(self,event=""):

        
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_Dep.set(data[0]),      
        self.var_course.set(data[1]),      
        self.var_Year.set(data[2]),      
        self.var_Semester.set(data[3]),      
        self.var_std_ID.set(data[4]),      
        self.var_std_name.set(data[5]),      
        self.var_Div.set(data[6]),      
        self.var_Roll.set(data[7]),      
        self.var_Gender.set(data[8]),      
        self.var_DOB.set(data[9]),      
        self.var_Email.set(data[10]),      
        self.var_Mobile.set(data[11]),      
        self.var_Address.set(data[12]),      
        self.var_Teacher.set(data[13]),      
        self.var_radio1.set(data[14])

# --------------------------------------------------------------------------- upadate function ----------------------------------------------------------------------

    def update_data(self):
        if self.var_Dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_ID.get() == "":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to Update this Student Details",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="Bhanu@123",database="facialrecognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update Student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(
                                                                                                                                                                                                          self.var_Dep.get(),
                                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                                          self.var_Year.get(),
                                                                                                                                                                                                          self.var_Semester.get(),
                                                                                                                                                                                                          
                                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                                          self.var_Div.get(),
                                                                                                                                                                                                          self.var_Roll.get(),
                                                                                                                                                                                                          self.var_Gender.get(),
                                                                                                                                                                                                          self.var_DOB.get(),
                                                                                                                                                                                                          self.var_Email.get(),
                                                                                                                                                                                                          self.var_Mobile.get(),
                                                                                                                                                                                                          self.var_Address.get(),
                                                                                                                                                                                                          self.var_Teacher.get(),
                                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                                          self.var_std_ID.get()
                                                                                                            
                                                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# -------------------------------------------------------------------------------- Delete Function ---------------------------------------------------------------------------------

    def delete_data(self):
        
      if self.var_std_ID.get() == "":
          messagebox.showerror("Error", "Student ID must be Required", parent=self.root)
      else:
          try:
              delete = messagebox.askyesno("Student Delete Page", "Do you want to Delete the Student Details?", parent=self.root)
              if delete > 0:
                  conn = mysql.connector.connect(host="localhost", user="root", password="Bhanu@123", database="facialrecognition")
                  my_cursor = conn.cursor()
                  sql = "DELETE FROM student WHERE Student_ID = %s"
                  val = (self.var_std_ID.get(),)  # Ensure val is a tuple
                  my_cursor.execute(sql, val)
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("Delete", "Successfully deleted Student Details", parent=self.root)
              else:
                  return  # If delete is canceled, do nothing
          except Exception as es:
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



# ---------------------------------------------------------------------------------- Reset Function -------------------------------------------------------------------------------
    def reset_data(self):
        self.var_Dep.set("Select Department")    
        self.var_course.set("Select Course")
        self.var_Year.set("Select Year")      
        self.var_Semester.set("Select Semester")      
        self.var_std_ID.set("")      
        self.var_std_name.set("")      
        self.var_Div.set("Select Divison")      
        self.var_Roll.set("")      
        self.var_Gender.set("Male")      
        self.var_DOB.set("")      
        self.var_Email.set("")      
        self.var_Mobile.set("")      
        self.var_Address.set("")      
        self.var_Teacher.set("")      
        self.var_radio1.set("")

# # ========================================= Search Data ===========================================================
    def search_data(self):
        if self.search_combo.get() == "Select" or self.search_entry.get() == "":
            messagebox.showerror("Error", "Select search criteria and enter value", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Bhanu@123",
                    database="facialrecognition"
                )
                my_cursor = conn.cursor()
                
                # Build the search query based on selected criteria
                if self.search_combo.get() == "Student_ID":
                    my_cursor.execute("SELECT * FROM student WHERE Student_ID LIKE %s", 
                                    ('%' + str(self.search_entry.get()) + '%',))
                elif self.search_combo.get() == "Mobile_No":
                    my_cursor.execute("SELECT * FROM student WHERE Phone LIKE %s",
                                    ('%' + str(self.search_entry.get()) + '%',))
                
                rows = my_cursor.fetchall()
                
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                    conn.commit()
                else:
                    messagebox.showinfo("Data", "No Record Found", parent=self.root)
                
                conn.close()
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
              
    
# From here we start working on the main project which is face_recognition 
# ----------------------------------------------------------------------------------------- Generate Data Set OR Take Photo Sample ---------------------------------------------------------------------------------
    def generate_dataset(self):
      if self.var_Dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_ID.get() == "":
          messagebox.showerror("Error", "All Fields are Required", parent=self.root)
      else:
          try:
              # Connect to the database
              conn = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="Bhanu@123",
                  database="facialrecognition"
              )
              my_cursor = conn.cursor()

              # Update student details
              my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s,Divison=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s,Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_ID=%s",
                  (
                      self.var_Dep.get(),
                      self.var_course.get(),
                      self.var_Year.get(),
                      self.var_Semester.get(),
                      self.var_std_name.get(),
                      self.var_Div.get(),
                      self.var_Roll.get(),
                      self.var_Gender.get(),
                      self.var_DOB.get(),
                      self.var_Email.get(),
                      self.var_Mobile.get(),
                      self.var_Address.get(),
                      self.var_Teacher.get(),
                      self.var_radio1.get(),
                      self.var_std_ID.get(),  # Pass Student_ID correctly
                  )
              )
              conn.commit()
              conn.close()

            # OpenCV face recognition
              face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

              def face_cropped(img):
                  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                  faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                  for (x, y, w, h) in faces:
                      return img[y:y + h, x:x + w]
                  return None

              cap = cv2.VideoCapture(0)
              img_id = 0

              while True:
                  ret, my_frame = cap.read()
                  if face_cropped(my_frame) is not None:
                      img_id += 1
                      face = cv2.resize(face_cropped(my_frame), (450, 450))
                      face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                      file_name_path = f"Data/user.{self.var_std_ID.get()}.{img_id}.jpg"
                      cv2.imwrite(file_name_path, face)

                      cv2.putText(
                          face, str(img_id), (50, 50),
                          cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2
                      )
                      cv2.imshow("Face after getting cropped", face)

                  if cv2.waitKey(1) == 13 or img_id == 100:  # 'Enter' key to stop
                      break

              cap.release()
              cv2.destroyAllWindows()

              messagebox.showinfo("Result", "Photo samples saved successfully!", parent=self.root)

          except Exception as es:
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)





          

                                                                                                                                            

                
                
        




                
                    
        
    
  



                 
                 
                         
                         
                         
                         
                 

                                                                                                                                                                                                                                                                                                                                                                                                                   





                                                                                                                                                                                                                                                                                                                                                                                                                   


              
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()



