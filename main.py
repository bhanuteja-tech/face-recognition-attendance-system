import tkinter
from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os
# from helpsupport import Helpsupport
from datetime import datetime
from tkinter import messagebox
from time import strftime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"images/Backgroundimage.jpg")
        img=img.resize((650,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=650,height=140)
        
        #Second heade image 
        img1=Image.open(r"images/Faceimage.jpg")
        img1=img1.resize((650,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=650,y=0,width=650,height=140)
        
        #Third header image 
        img2=Image.open(r"images/Worldimage.jpg")
        img2=img2.resize((650,200),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1300,y=0,width=600,height=140)

        #backgorund image 
        bg1=Image.open(r"C:\Users\bhanu\Downloads\Images\0899623a-1944-45cf-882e-2cf4a3c99cf6.jpg")
        bg1=bg1.resize((1920,1080),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1920,height=1080)


        #title section
        title_lb1 = Label(bg_img,text="ADVANCED FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="BLACK")
        title_lb1.place(x=0,y=0,width=1920,height=40)

        # ========================== time section ==========================
        def time_current():
            string = strftime("%H:%M:%S")
            time_lb1.config(text=string)
            time_lb1.after(1000,time_current)

        time_lb1 = Label(bg_img,font=("times new roman",20,"bold"),bg="white",fg="navyblue")
        time_lb1.place(x=0,y=40,width=1920,height=40)
        time_current()

#         # Create buttons below the section 
#         # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"images/Backla.jpg")
        std_img_btn=std_img_btn.resize((220,220),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,command=self.student_details,cursor="hand2")
        std_b1.place(x=100,y=100,width=220,height=220)

        std_b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="WHITE",fg="navyblue")
        std_b1_1.place(x=100,y=300,width=220,height=40)

#       # --------------- Detect Face  button 2 ----------------

        det_img_btn=Image.open(r"images/Face_button.jpg")
        det_img_btn=det_img_btn.resize((220,220),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",command=self.face_data)
        det_b1.place(x=400,y=100,width=220,height=220)

        det_b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue",command=self.face_data)
        det_b1_1.place(x=400,y=300,width=220,height=40)

#       # ---------- Attendance System  button 3 ----------
        att_img_btn=Image.open(r"images/Attendance'.jpg")
        att_img_btn=att_img_btn.resize((220,220),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",command=self.attendance_data)
        att_b1.place(x=700,y=100,width=220,height=220)

        att_b1_1 = Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue",command=self.attendance_data)
        att_b1_1.place(x=700,y=300,width=220,height=40)

        #----------- Help  Support  button 4 -------------
        hlp_img_btn=Image.open(r"images/help.jpg")
        hlp_img_btn=hlp_img_btn.resize((220,220),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, image=self.hlp_img1, cursor="hand2", command=self.help_desk)
        hlp_b1.place(x=1000,y=100,width=220,height=220)

        hlp_b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_desk,
                          font=("times new roman", 15, "bold"), bg="white", fg="navyblue")
        hlp_b1_1.place(x=1000,y=300,width=220,height=40)

#         # Top 4 buttons end.......
#         # ---------------------------------------------------------------------------------------------------------------------------
#         # Start below buttons.........
#       # Train   button 5
        tra_img_btn=Image.open(r"images/Train.jpg")
        tra_img_btn=tra_img_btn.resize((220,220),Image.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,image=self.tra_img1,cursor="hand2",command=self.train_data)
        tra_b1.place(x=100,y=400,width=220,height=220)

        tra_b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=100,y=600,width=220,height=40)

#        # Photo   button 6
        pho_img_btn=Image.open(r"images/Images.jpg")
        pho_img_btn=pho_img_btn.resize((220,220),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,image=self.pho_img1,cursor="hand2",command=self.open_img)
        pho_b1.place(x=400,y=400,width=220,height=220)

        pho_b1_1 = Button(bg_img,text="Images",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=400,y=600,width=220,height=40)

#         # Developers   button 7
        dev_img_btn=Image.open(r"images/Devloper.jpg")
        dev_img_btn=dev_img_btn.resize((220,220),Image.LANCZOS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,image=self.dev_img1,cursor="hand2",command=self.developer_data)
        dev_b1.place(x=700,y=400,width=220,height=220)

        dev_b1_1 = Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,
                          font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=700,y=600,width=220,height=40)

#         # exit   button 8
        exi_img_btn=Image.open(r"images/Exit_button.jpg")
        exi_img_btn=exi_img_btn.resize((220,220),Image.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,image=self.exi_img1,cursor="hand2",command=self.isexit)
        exi_b1.place(x=1000,y=400,width=220,height=220)

        exi_b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.isexit,font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=1000,y=600,width=220,height=40)

# # ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data")


    def isexit(self):
        self.isexit = tkinter.messagebox.askyesno("Face Recognition System", "Are you sure you want to exit?", parent=self.root)
        if self.isexit >0:
            self.root.destroy()
        else:
            return 

    
    
    
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

     
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)



#         os.startfile("dataset")
# # ==================Functions Buttons=====================
#     def student_pannels(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Student(self.new_window)

#     def train_pannels(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Train(self.new_window)
    
#     def face_rec(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Face_Recognition(self.new_window)
    
#     def attendance_pannel(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Attendance(self.new_window)
    
#     def developr(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Developer(self.new_window)
    
#     def helpSupport(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Helpsupport(self.new_window)

#     def Close(self):
#         root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
