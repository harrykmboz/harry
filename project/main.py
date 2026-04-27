import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from dashboard import HotalManagementSystem
class LoginSignup:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Signup")
        self.root.geometry("1550x800+0+0")
        self.root.state("zoomed")
        
        # Setup DB
        self.db_connection()

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"./hotel images/myh.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        self.frame = Frame(self.root, bg="black")
        self.frame.place(x=570, y=170, width=340, height=450)

        # Icon Image
        img1 = Image.open(r"./hotel images/LoginIconAppl.png")
        img1 = img1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=690, y=175, width=100, height=100)

        # Title
        get_str = Label(self.frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username Label + Entry
        lbl_username = Label(self.frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        lbl_username.place(x=70, y=155)
        self.txtuser = ttk.Entry(self.frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password Label + Entry
        password = Label(self.frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(self.frame, show="*", font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # Icons for username and password
        img2 = Image.open(r"./hotel images/LoginIconAppl.png")
        img2 = img2.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=610, y=323, width=25, height=25)

        img3 = Image.open(r"./hotel images/lock-512.png")
        img3 = img3.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root, image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=610, y=395, width=25, height=25)

        # Buttons
        loginbtn = Button(self.frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                          fg="white", bg="red", activeforeground="white", activebackground="red", command=self.login_user)
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(self.frame, text="New User Register", font=("times new roman", 10, "bold"),
                             borderwidth=0, fg="white", bg="black", activeforeground="white",
                             activebackground="black", command=self.open_register_window)
        registerbtn.place(x=20, y=350, width=160)

        forgetbtn = Button(self.frame, text="Forget Password", font=("times new roman", 10, "bold"),
                           borderwidth=0, fg="white", bg="black", activeforeground="white",
                           activebackground="black", command=self.open_forgot_password_window) 
        forgetbtn.place(x=15, y=370, width=160)

    def db_connection(self):
        conn = sqlite3.connect("hotel.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def login_user(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return

        conn = sqlite3.connect("hotel.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Success", f"Welcome {username}!")
            self.new_window=Toplevel(self.root)
            self.app=HotalManagementSystem(self.new_window)
            # You can call your main system here if needed
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def open_register_window(self):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Register")
        self.new_window.geometry("1550x800+0+0")
        self.new_window.configure(bg="black")
        self.new_window.state("zoomed")

        # Background Image
        self.bg1 = ImageTk.PhotoImage(file=r"./hotel images/myh.jpg")
        lbl_bg1 = Label(self.new_window, image=self.bg1)
        lbl_bg1.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        self.reg_frame = Frame(self.new_window, bg="black")
        self.reg_frame.place(x=570, y=150, width=340, height=450)

        # Icon
        img0 = Image.open(r"./hotel images/LoginIconAppl.png")
        img0 = img0.resize((100, 100))
        self.photoimage0 = ImageTk.PhotoImage(img0)
        lblimg0 = Label(self.reg_frame, image=self.photoimage0, bg="black", borderwidth=0)
        lblimg0.place(relx=0.5, y=10, anchor="n")

        # Title
        get_str = Label(self.reg_frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(relx=0.5, y=120, anchor="n")

        # Username Entry
        lbl_username = Label(self.reg_frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        lbl_username.place(x=70, y=155)
        self.reg_username = ttk.Entry(self.reg_frame, font=("times new roman", 15, "bold"))
        self.reg_username.place(x=40, y=180, width=270)

        # Password Entry
        password = Label(self.reg_frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.reg_password = ttk.Entry(self.reg_frame, show="*", font=("times new roman", 15, "bold"))
        self.reg_password.place(x=40, y=250, width=270)

        # Icons (optional)
        img6 = Image.open(r"./hotel images/LoginIconAppl.png")
        img6 = img6.resize((25, 25))
        self.photoimage6 = ImageTk.PhotoImage(img6)
        lblimg6 = Label(self.reg_frame, image=self.photoimage6, bg="black", borderwidth=0)
        lblimg6.place(x=10, y=180, width=25, height=25)

        img7 = Image.open(r"./hotel images/lock-512.png")
        img7 = img7.resize((25, 25))
        self.photoimage7 = ImageTk.PhotoImage(img7)
        lblimg7 = Label(self.reg_frame, image=self.photoimage7, bg="black", borderwidth=0)
        lblimg7.place(x=10, y=250, width=25, height=25)

        # Signup Button
        signbtn = Button(self.reg_frame, text="Sign Up", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                         fg="white", bg="red", activeforeground="white", activebackground="red",
                         command=self.signup_user)
        signbtn.place(relx=0.5, y=320, anchor="n", width=120, height=35)
        
    def open_forgot_password_window(self):
        # New Toplevel window for forgetting password
        self.forgot_win = Toplevel(self.root)
        self.forgot_win.title("Forget Password")
        self.forgot_win.geometry("400x300+700+250")
        self.forgot_win.configure(bg="black")

        lbl = Label(self.forgot_win, text="Forget Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        lbl.pack(pady=10)

        lbl_username = Label(self.forgot_win, text="Enter Username", font=("times new roman", 15), fg="white", bg="black")
        lbl_username.pack(pady=5)
        self.forgot_username_entry = ttk.Entry(self.forgot_win, font=("times new roman", 15))
        self.forgot_username_entry.pack(pady=5)

        lbl_new_pass = Label(self.forgot_win, text="Enter New Password", font=("times new roman", 15), fg="white", bg="black")
        lbl_new_pass.pack(pady=5)
        self.forgot_new_pass_entry = ttk.Entry(self.forgot_win, font=("times new roman", 15), show="*")
        self.forgot_new_pass_entry.pack(pady=5)

        reset_btn = Button(self.forgot_win, text="Reset Password", font=("times new roman", 15, "bold"),
                           fg="white", bg="red",  command=self.reset_password)
        reset_btn.pack(pady=20)
    def signup_user(self):
        username = self.reg_username.get()
        password = self.reg_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect("hotel.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.new_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()

    def forgot_password(self):
        messagebox.showinfo("Info", "Password reset functionality coming soon.")
    
    def reset_password(self):
        username = self.forgot_username_entry.get()
        new_password = self.forgot_new_pass_entry.get()
        if not username or not new_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect("hotel.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        if c.fetchone():
            c.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
            conn.commit()
            messagebox.showinfo("Success", "Password has been reset!")
            self.forgot_win.destroy()
        else:
            messagebox.showerror("Error", "Username not found.")
        conn.close()
    
          
if __name__ == "__main__":
    root = Tk()
    app = LoginSignup(root)
    root.mainloop()
    
