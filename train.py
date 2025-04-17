from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import cv2
import mysql.connector
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train Data")
        
        
        
        #title section
        title_lb1 = Label(self.root,text="TRAIN DATA ",font=("times new roman",35,"bold"),bg="white",fg="BLACK")
        title_lb1.place(x=0,y=0,width=1920,height=40)


         # ----------- Labels ------------

        
        img_top=Image.open(r"images/llll.jpg")
        img_top=img_top.resize((1910,450),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=1910, height=450)
        
        # --------- button --------- 
        std_b1_1 = Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="Orange",fg="white")
        std_b1_1.place(x=0,y=470,width=1910,height=79)
        
        img_bottom=Image.open(r"images/llll.jpg")
        img_bottom=img_bottom.resize((1910,450),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=0, y=550, width=1910, height=450)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        print("Starting training process...")
        print(f"Found {len(path)} images to process")

        for image in path:
            try:
                # Load and preprocess each training image
                img = Image.open(image).convert('L')  # Convert to grayscale
                img = img.resize((200, 200), Image.LANCZOS)  # Consistent size with recognition
                
                # Convert to numpy array
                imageNp = np.array(img, 'uint8')
                
                # Apply preprocessing
                # 1. Histogram equalization for better contrast
                imageNp = cv2.equalizeHist(imageNp)
                
                # 2. Gaussian blur to reduce noise
                imageNp = cv2.GaussianBlur(imageNp, (5, 5), 0)
                
                # 3. Apply adaptive thresholding
                imageNp = cv2.adaptiveThreshold(imageNp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
                
                # Extract ID from filename
                id = int(os.path.split(image)[1].split('.')[1])
                
                faces.append(imageNp)
                ids.append(id)
                
                # Show progress
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
                
                print(f"Processed image: {image}")
                
            except Exception as e:
                print(f"Error processing image {image}: {str(e)}")
                continue

        if len(faces) == 0:
            messagebox.showerror("Error", "No valid training images found!")
            return

        ids = np.array(ids)
        print(f"Training with {len(faces)} images")

        # Create and train the LBPH Face Recognizer with optimized parameters
        clf = cv2.face.LBPHFaceRecognizer_create(
            radius=2,  # Radius of the circular pattern
            neighbors=12,  # Number of sample points
            grid_x=8,  # Number of cells in X direction
            grid_y=8,  # Number of cells in Y direction
            threshold=100.0  # Distance threshold
        )
        
        # Train the classifier
        clf.train(faces, ids)
        
        # Save the model
        clf.write("classifier.xml")
        
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", f"Training completed successfully with {len(faces)} images!")




            
        
        










if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
