from tkinter import *
import webbrowser
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Developer Information")

        # Background image
        img = Image.open(r"images/0899623a-1944-45cf-882e-2cf4a3c99cf6.jpg")
        img = img.resize((1920, 1080), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1920, height=1080)
        
        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=350, y=100, width=1200, height=800)
        
        # Title
        title_lbl = Label(self.root, text="Developer Information", 
                         font=("times new roman", 35, "bold"), 
                         bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Developer Image
        # Left side image
        img_left = Image.open(r"images/Bhanuteja.jpg")
        img_left = img_left.resize((200, 200), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        dev_img = Label(main_frame, image=self.photoimg_left)
        dev_img.place(x=500, y=50, width=200, height=200)

        # Developer Info
        dev_label = Label(main_frame, text="Hello, I'm Bhanu Teja.S", 
                         font=("times new roman", 20, "bold"), 
                         bg="white", fg="black")
        dev_label.place(x=450, y=270)

        dev_desc = Label(main_frame, text="Data science | Machine Learning Enthusiast", 
                        font=("times new roman", 15), 
                        bg="white", fg="dark blue")
        dev_desc.place(x=400, y=320)

        # Introduction text
        intro_text = "I am a passionate Data enthusiast with expertise in building Face Recognition and Machine Learning systems."
        intro_label = Label(main_frame, text=intro_text,
                          font=("times new roman", 12),
                          bg="white", fg="black",
                          justify=LEFT,
                          wraplength=800)
        intro_label.place(x=200, y=370)

        # Bullet points description
        bullet_points = [
            "This project utilizes OpenCV for Face Recognition, enabling accurate and efficient face detection and recognition.",
            
            "The GUI is developed using Tkinter, providing an intuitive and user-friendly interface for easy interaction.",
            
            "Database management is handled through SQL, ensuring secure and organized storage of attendance records.",
            
            "Image processing is implemented using PIL (Python Imaging Library) for optimal handling of visual data.",
            
            "The system employs the Haarcascade_frontal_face algorithm for face detection and LBPH (Local Binary Patterns Histograms) algorithm for face recognition.",
            
            "Once a face is detected and recognized, the system automatically marks attendance in the database."
        ]

        # Create bullet point labels
        for i, point in enumerate(bullet_points):
            bullet_label = Label(main_frame, 
                               text=f"• {point}",
                               font=("times new roman", 12),
                               bg="white",
                               fg="black",
                               justify=LEFT,
                               wraplength=750)
            bullet_label.place(x=200, y=420 + (i * 40))

        # Visit Portfolio Button
        visit_btn = Button(main_frame, text="Visit Portfolio", 
                          command=self.open_portfolio,
                          cursor="hand2",
                          font=("times new roman", 15, "bold"),
                          bg="blue", fg="white")
        visit_btn.place(x=500, y=700, width=200, height=40)

    def open_portfolio(self):
        webbrowser.open_new("https://portfolio-git-main-bhanu-tejas-projects-544289e2.vercel.app/")

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()


