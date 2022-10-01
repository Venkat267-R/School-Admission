from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as my   # pip install mysql-connector-python



class Register:
    def __init__(self, root):
        self.root = root

        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="light cyan")
        frame1 = Frame(self.root, bg="bisque3")
        frame1.place(x=500, y=100, width=750, height=550)
        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="black")

        f_name = Label(frame1, text="Student Name", font=("times new roman", 15, "bold"), bg="bisque3", fg="black").place(
            x=50, y=50)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_fname.place(x=50, y=80, width=250)

        pname = Label(frame1, text="Parent/Guardian Name", font=("times new roman", 15, "bold"), bg="bisque3",
                      fg="black").place(x=370, y=50)
        self.txt_pname = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_pname.place(x=370, y=80, width=250)

        age = Label(frame1, text="student's age", font=("times new roman", 15, "bold"), bg="bisque3", fg="black").place(
            x=50, y=120)
        self.txt_age = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_age.place(x=50, y=150, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="bisque3", fg="black").place(x=370,
                                                                                                                y=120)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_email.place(x=370, y=150, width=250)

        contact = Label(frame1, text="Contact no. ", font=("times new roman", 15, "bold"), bg="bisque3",
                        fg="black").place(x=50, y=190)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_contact.place(x=50, y=220, width=250)

        class_admission = Label(frame1, text="class", font=("times new roman", 15, "bold"), bg="bisque3",
                                fg="black").place(x=50, y=260)
        self.cmb_class = ttk.Combobox(frame1, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.cmb_class["values"] = ("Select", "1", "2", "3", "4", "5")
        self.cmb_class.place(x=50, y=290, width=250)
        self.cmb_class.current(0)

        dob = Label(frame1, text="Date of Birth(yyyymmdd)", font=("times new roman", 15, "bold"), bg="bisque3",
                    fg="black").place(x=370, y=190)
        self.txt_dob = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_dob.place(x=370, y=220, width=250)

        sibling = Label(frame1, text="Whether a single child?", font=("times new roman", 15, "bold"), bg="bisque3",
                            fg="black").place(x=50, y=330)
        self.cmb_sibling = ttk.Combobox(frame1, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.cmb_sibling["values"] = ("Select", "YES", "NO")
        self.cmb_sibling.place(x=50, y=360, width=250)
        self.cmb_sibling.current(0)

        aadhaar = Label(frame1, text="Aadhaar no.", font=("times new roman", 15, "bold"), bg="bisque3", fg="black").place(
            x=370, y=260)
        self.txt_aadhaar = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_aadhaar.place(x=370, y=290, width=250)

        pincode = Label(frame1, text="Pincode", font=("times new roman", 15, "bold"), bg="bisque3", fg="black").place(
            x=370, y=330)
        self.txt_pincode = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_pincode.place(x=370, y=360, width=250)

        last = Label(frame1, text="Last School Attended ", font=("times new roman", 15, "bold"), bg="bisque3",
                     fg="black").place(x=370, y=400)
        self.txt_last = Entry(frame1, font=("times new roman", 15), bg="deep sky blue")
        self.txt_last.place(x=370, y=430, width=250)

        gender = Label(frame1, text="GENDER", font=("times new roman", 15, "bold"), bg="bisque3",
                    fg="black").place(x=50, y=400)
        self.cmb_gen = ttk.Combobox(frame1, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.cmb_gen["values"] = ("Select", "MALE", "FEMALE", "TRANSGENDER")
        self.cmb_gen.place(x=50, y=430, width=250)
        self.cmb_gen.current(0)

        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms and Conditions", onvalue=1, offvalue=0, variable=self.var_chk, fg="red",
                          bg="deep sky blue", font=("times new roman", 13)).place(x=50, y=470)
        btn = Button(frame1, text="REGISTER HERE--->", font=("times new roman", 15),command=lambda: (self.register_data(), self.clear()), bd=0, cursor="hand2", bg="deep sky blue", fg="red").place(x=370,y=470,width=250)

        school = Label(root, text="AQUILYNE WONDERS INTERNATIONAL SCHOOL", font=("times new roman",30), bg="light cyan", fg="purple3").place(x=250,y=10)
        affi = Label(root, text="(AFFILIATED TO CBSE)", font=("times new roman",15), bg="light cyan", fg="purple3").place(x=550,y=60)
        here = Label(frame1, text="Fill the form below for admission request",font=("times new roman",20),bg="bisque3", fg="black").place(x=50,y=10)
        affiliation = Label(root, text="Affiliation Number:", font=("times new roman",20), bg="light cyan", fg="purple3").place(x=5,y=100)
        affiliationno = Label(root, text="0000000",font=("times new roman",15), bg="light cyan", fg="black").place(x=5,y=130)
        scholaddress = Label(root, text="ADDRESS:", font=("times new roman",20), bg="light cyan", fg="purple3").place(x=5,y=200)
        school_address = Label(root, text="No27,Sabapathy street,Ullagaram, CHENNAI 600091",font=("times new roman",15), bg="light cyan", fg="black").place(x=5,y=230)
        schoolcontact = Label(root, text="CONTACT:", font=("times new roman",20), bg="light cyan", fg="purple3").place(x=5,y=300)
        school_contact = Label(root, text="+91 00000 00000",font=("times new roman",15), bg="light cyan", fg="black").place(x=5,y=330)
        school_contact2 = Label(root, text="aquilynewis2020@aquilyne.in", font=("times new roman",15), bg="light cyan", fg="black").place(x=5,y=360)
        school_contact3 = Label(root, text="044-0000 0000",font=("times new roman",15), bg="light cyan", fg="black").place(x=5,y=390)
        schoolwebsite = Label(root, text="WEBSITE:", font=("times new roman",20), bg="light cyan", fg="purple3").place(x=5,y=440)
        school_website = Label(root, text="https://www.aquilyneschool.edu",font=("times new roman",15), bg="light cyan", fg="black").place(x=5,y=470)

        log = Label(root, text="ADMINISTRATION LOGIN", font=("times new roman",20), bg="light cyan", fg="midnight blue").place(x=130,y=550)
        btn_login = Button(root, text="Sign In", font=("times new roman", 20),command=lambda :self.admin_login(), bd=0,fg="midnight blue",bg="spring green2", cursor="hand2").place(x=250, y=590)





    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_pname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_class.current(0)
        self.txt_aadhaar.delete(0, END)
        self.txt_age.delete(0, END)
        self.txt_last.delete(0, END)
        self.txt_pincode.delete(0, END)
        self.txt_dob.delete(0, END)
        self.cmb_gen.current(0)
        self.cmb_sibling.current(0)
    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_pname.get()=="" or self.txt_email.get() == "" or self.txt_contact.get() == "" or self.cmb_class.get() == "Select" or self.txt_age.get() == "" or self.txt_dob.get() == "" or self.cmb_sibling.get()=="Select" or self.txt_aadhaar.get() == "" or self.txt_pincode.get() == "" or self.txt_last.get()=="" or self.cmb_gen.get()=="Select":
            messagebox.showerror("ERROR", "All Fields Are Required", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("ERROR", "Please Agree To Our Terms and Conditions", parent=self.root)
        else:
            try:
                con = my.connect(host="localhost", user="root", password="tiger", database="schooladmissionportal")
                cur = con.cursor()
                cur.execute("insert into school (student_name,parent_name,contact,email,class,age,dob,single_child,aadhaar,pincode,last_school,gender) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(), self.txt_pname.get(), self.txt_contact.get(), self.txt_email.get(),
                  self.cmb_class.get(), self.txt_age.get(),self.txt_dob.get(),self.cmb_sibling.get() , self.txt_aadhaar.get(),
                   self.txt_pincode.get(), self.txt_last.get(),self.cmb_gen.get()
                             ))
                con.commit()
                con.close()
                messagebox.showinfo("SUCCESS", "Request successful!! We Wil Contact You Soon", parent=self.root)
                self.clear()
            except Exception as es:
                messagebox.showerror("error", f"error due to:{str(es)}", parent=self.root)

    def admin_login(self):
        self.root.destroy()
        import login


root = Tk()
obj = Register(root)
root.mainloop()
