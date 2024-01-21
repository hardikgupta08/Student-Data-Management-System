from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkfont

global enter_email_student
global enter_password_student
global enter_first_n
global enter_last_n
global enter_contact_n
global enter_cours
def open_student_login():
    root = Tk()
    frame = Frame(root, background="light green")
    frame.pack()
    root["bg"] = "#90EE90"
    root.title("Student Login Page")
    root.minsize(600, 600)

    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="hardik01",
        port=3306,
        database="management",
    )
    c = conn.cursor()

    enter_email_student = StringVar()
    enter_password_student = StringVar()

    a = Label(
        frame, text="LOGIN ", background="light green", font=("Verdana", 25)
    ).pack(side=TOP, pady=30)
    email = Label(
        frame, text="ENTER EMAIL : ", background="light green", font=("Arial", 15)
    ).pack()
    enter_email_student = Entry(frame, width=30, bd=5, font=("Arial", 15))
    enter_email_student.pack(side=TOP, pady=10)
    password = Label(
        frame, text="ENTER PASSWORD : ", background="light green", font=("Arial", 15)
    ).pack()
    enter_password_student = Entry(frame, show="*", width=30, bd=5, font=("Arial", 15))
    enter_password_student.pack(side=TOP, pady=10)

    def student_home():
        root = Tk()
        root.title("Student Home")
        root["bg"] = "#90EE90"
        root.minsize(1000, 700)
        root.maxsize(1000,700)
        sql3 = f'select first_name from registration_student where email = "{enter_email_student.get()}"'
        c.execute(sql3)
        name1 = c.fetchone()
        for a in name1:
            name = a
        l = Label(
            root, text=f"Welcome,{name}", font=("Inter", 30), background="light green"
        ).pack(side=TOP, pady=(50, 0))
        log = Button(
            root,
            text="Logout",
            font=("Verdana", 15),
            bd="5",
            bg="teal",
            fg="black",
            activebackground="teal",
            command=root.destroy,
        ).place(x=700,y = 50)
        style = ttk.Style()

        Table_details = Frame(root, relief="ridge",height=50)
        Table_details.pack(side=TOP, pady=(50, 0))
        data = ttk.Treeview(
            Table_details,
            column=(
                "Student ID",
                "First Name",
                "Last Name",
                "Contact Number",
                "Course Opted",
                "Date Of Birth",
                "Assignment 1",
                "Assignment 2",
                "Assignment 3",
                "Final Exam",
            )
        )

        data.heading("Student ID", text="Student ID")
        data.heading("First Name", text="First Name")
        data.heading("Last Name", text="Last Name")
        data.heading("Contact Number", text="Contact Number")
        data.heading("Course Opted", text="Course Opted")
        data.heading("Date Of Birth", text="Date Of Birth")
        data.heading("Assignment 1", text="Assignment 1")
        data.heading("Assignment 2", text="Assignment 2")
        data.heading("Assignment 3", text="Assignment 3")
        data.heading("Final Exam", text="Final Exam")

        data["show"] = "headings"
        data.column("Student ID", width=75)
        data.column("First Name", width=75)
        data.column("Last Name", width=75)
        data.column("Contact Number", width=75)
        data.column("Course Opted", width=75)
        data.column("Date Of Birth", width=75)
        data.column("Assignment 1", width=75)
        data.column("Assignment 2", width=75)
        data.column("Assignment 3", width=75)
        data.column("Final Exam", width=75)

        data.pack(fill=BOTH, expand=1)
        def fetch():
            sql2 = f'select registration_student.id,registration_student.first_name,registration_student.last_name,registration_student.contact_number,registration_student.course,registration_student.date_of_birth,marks.assignment_1,marks.assignment_2,marks.assignment_3,marks.final_exam from registration_student, marks where registration_student.email = marks.email and registration_student.email = "{enter_email_student.get()}"'
            c.execute(sql2)
            result = c.fetchall()
            for i in result:
                data.insert("", END, values=i,tags='TkTextFont')
            conn.commit()
        fetch()
        def refresh():
            for i in data.get_children():
                data.delete(i)
            Table_details.after(1000,fetch)
        update_personal_info = Button(
            root,
            text="Update Personal Info",
            font=("Verdana", 15),
            bd="5",
            bg="teal",
            fg="black",
            activebackground="teal",
            command=update_student,
        )
        update_personal_info.place(x= 220,y = 450)
        refresh = Button(root, text = "Refresh Data", font=("Verdana", 15),bd="5",bg="teal",fg="black",activebackground="teal",command=refresh)
        refresh.place(x= 520,y=450)
        root.mainloop()

    def handle_login():
        id_1 = enter_email_student.get()
        passwrd = enter_password_student.get()
        count = 0
        if id_1 == "" and passwrd == "":
            messagebox.showinfo(
                "Information", "Please Enter Username and Password to Login."
            )
        else:
            sql = "select email,password from registration_student"
            c.execute(sql)
            result = c.fetchall()
            conn.commit()
            for b in result:
                if id_1 == b[0] and passwrd == b[1]:
                    count += 1
            if count != 0:
                messagebox.showinfo("Success", "Login Successfull")
                student_home()
            else:
                messagebox.showinfo("Error", "Invalid Username or Password")

    submit = Button(
        root,
        text="SUBMIT",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=handle_login,
    ).place(x=300, y=275)
    back = Button(
        root,
        text="BACK",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=root.destroy,
    ).place(x=150, y=275)

    def update_student():
        window = Tk()
        window["bg"] = "#90EE90"
        window.title("Update Student Details")
        a1 = Label(
            window,
            text="Personal Information Update",
            background="light green",
            font=("Verdana", 25),
        )
        a1.pack(side=TOP, pady=30)

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="hardik01",
            port=3306,
            database="management",
        )
        c = conn.cursor()

        enter_first_n = StringVar()
        enter_last_n = StringVar()
        enter_contact_n = StringVar()
        enter_cours = StringVar()

        first_n = Label(
            window,
            text="ENTER FIRST NAME : ",
            background="light green",
            font=("Arial", 15),
        )
        first_n.pack()
        enter_first_n = Entry(window, width=30, bd=5, font=("Arial", 15))
        enter_first_n.pack(side=TOP, pady=10)

        last_n = Label(
            window,
            text="ENTER LAST NAME : ",
            background="light green",
            font=("Arial", 15),
        )
        last_n.pack()
        enter_last_n = Entry(window, width=30, bd=5, font=("Arial", 15))
        enter_last_n.pack(side=TOP, pady=10)

        contact_n = Label(
            window,
            text="ENTER CONTACT NUMBER : ",
            background="light green",
            font=("Arial", 15),
        )
        contact_n.pack()
        enter_contact_n = Entry(window, width=30, bd=5, font=("Arial", 15))
        enter_contact_n.pack(side=TOP, pady=10)

        cours = Label(
            window, text="ENTER COURSE : ", background="light green", font=("Arial", 15)
        )
        cours.pack()
        enter_cours = Entry(window, width=30, bd=5, font=("Arial", 15))
        enter_cours.pack(side=TOP, pady=10)

        def check():
            i = enter_first_n.get()
            j = enter_last_n.get()
            k = enter_contact_n.get()
            l = enter_cours.get()
            if i == "":
                messagebox.showerror("Error", "Please Enter First Name")
            else:
                if j == "":
                    messagebox.showerror("Error", "Please Enter Last name ")
                else:
                    if len(k) > 10 or len(k) < 10 or k.isdigit() == False:
                        messagebox.showinfo(
                            "Error", "CONTACT NUMBER MUST CONTAIN 10 DIGITS."
                        )
                    else:
                        if l == "":
                            messagebox.showerror(
                                "Error", "PLEASE ENTER THE COURSE YOU ARE TAKING"
                            )
                        else:
                            sql = f'update registration_student set first_name = "{i}",last_name = "{j}",contact_number = {k},course = "{l}" where email = "{enter_email_student.get()}"'
                            c.execute(sql)
                            conn.commit()
                            messagebox.showinfo(
                                "Information", "Data has been Updated Successfully"
                            )
                            window.destroy()
    
        submit_btn = Button(
            window,
            text="SUBMIT",
            font=("Verdana", 15),
            bd="5",
            bg="teal",
            fg="black",
            activebackground="teal",
            command=lambda:[check()]
        )
        submit_btn.pack()
        

        window.mainloop()

    root.mainloop()
