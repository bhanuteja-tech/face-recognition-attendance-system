from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Help Desk")

        # Background image
        img = Image.open(r"images/0899623a-1944-45cf-882e-2cf4a3c99cf6.jpg")
        img = img.resize((1920, 1080), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1920, height=1080)
        
        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=350, y=100, width=1200, height=820)
        
        # Title
        title_lbl = Label(self.root, text="Help Desk", 
                         font=("times new roman", 35, "bold"), 
                         bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Description
        desc_text = """Welcome to the Face Recognition Attendance System Help Desk!
        
For any queries, technical support, or feedback, please feel free to contact our team members:"""
        
        desc_label = Label(main_frame, text=desc_text,
                          font=("times new roman", 15),
                          bg="white", fg="black",
                          justify=LEFT)
        desc_label.place(x=100, y=50)

        # Team Members Contact Information
        team_members = [
            {
                "name": "Bhanu Teja S",
                "role": "Project Lead & Developer",
                "email": "bhanutejasubbara@gmail.com"
            },
            {
                "name": "Mehrin Khan",
                "role": "Database Administrator",
                "email": "mehrin69khan@gmail.com"
            },
            {
                "name": "Uhitha Abburi",
                "role": "UI/UX Designer",
                "email": "uhithaabburi23@gmail.com"
            },
            {
                "name": "Jyothi Swaroop",
                "role": "System Analyst",
                "email": "jyothiswaroop368@gmail.com"
            }
        ]

        # Display team member information
        for i, member in enumerate(team_members):
            # Frame for each member
            member_frame = Frame(main_frame, bg="white", relief=RIDGE, bd=1)
            member_frame.place(x=100, y=150 + (i * 120), width=1000, height=100)
            
            # Name
            name_label = Label(member_frame, 
                             text=member["name"],
                             font=("times new roman", 15, "bold"),
                             bg="white", fg="navy")
            name_label.place(x=20, y=10)
            
            # Role
            role_label = Label(member_frame,
                             text=member["role"],
                             font=("times new roman", 12),
                             bg="white", fg="dark green")
            role_label.place(x=20, y=40)
            
            # Email
            email_label = Label(member_frame,
                              text=f"Email: {member['email']}",
                              font=("times new roman", 12),
                              bg="white", fg="blue")
            email_label.place(x=20, y=65)

        # Additional Information
        info_text = """
        For assistance, you can:
        • Report any technical issues or bugs
        • Request new features or improvements
        • Get help with system usage
        • Share your feedback and suggestions
        
        Our team will respond to your queries as soon as possible."""
        
        info_label = Label(main_frame, text=info_text,
                          font=("times new roman", 12),
                          bg="white", fg="black",
                          justify=LEFT)
        info_label.place(x=100, y=650)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()