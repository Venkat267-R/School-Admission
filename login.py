from tkinter import *
from tkinter import messagebox

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("ADMIN LOGIN")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="azure")

        login_frame = Frame(self.root,bg="azure")
        login_frame.place(x=250, y=100, width=800, height=500)

        school = Label(root, text="AQUILYNE WONDERS INTERNATIONAL SCHOOL", font=("times new roman", 30),
                       bg="azure", fg="magenta4").place(x=250, y=30)
        affi = Label(root, text="(AFFILIATED TO CBSE)", font=("times new roman", 15), bg="azure",
                     fg="magenta4").place(x=550, y=80)
        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"),bg="azure", fg="purple").place(x=250, y=100)
        username = Label(login_frame, text="USERNAME", font=("times new roman", 18, "bold"), bg="azure", fg="indian red").place(x=250, y=150)
        self.txt_username = Entry(login_frame, font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.txt_username.place(x=250, y=180, width=350, height=35)

        password = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="azure", fg="indian red").place(x=250, y=250)
        self.txt_password = Entry(login_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", show="♫")
        self.txt_password.place(x=250, y=280, width=350, height=35)

        btn_login = Button(login_frame, text="login", command=lambda:(self.login(), self.clear()), font=("times new roman", 20, "bold"), bg="lavender blush", cursor="hand2", fg="dark olive green").place(x=250, y=320, width=180, height=40)

    def login(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("ERROR","All Fields Required", parent=self.root)
        elif self.txt_username.get() != "AWIS@2020" or self.txt_password.get() != "2020Awis":
            messagebox.showerror("ERROR", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("SUCCESS", "Welcome Admin", parent=self.root)
            self.root.destroy()
            import admin
    def clear(self):
        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)




root=Tk()
obj = Login_Window(root)
root.mainloop()
