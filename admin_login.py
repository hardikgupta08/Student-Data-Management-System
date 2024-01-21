# ---------Admin Login Page----------#

# ---------Necessary import files----------#
from tkinter import *
from tkinter import messagebox
from admin1 import admin_home
import mysql.connector

# ---------Global Variables----------#
global admin
global pas


# ---------Admin Login Window----------#
def open_admin_page():
    root = Tk()
    frame = Frame(root, background="light green")
    frame.pack()
    root["bg"] = "#90EE90"
    root.title("ADMIN LOGIN")
    root.minsize(600, 600)
    admin1 = StringVar()
    pas = StringVar()

    # ---------SQL connection established----------#
    conn = mysql.connector.connect(host="localhost", username="root", password="hardik01", port=3306,
                                   database="management")
    c = conn.cursor()

    wel = Label(
        frame, text="WELCOME", background="light green", font=("Verdana", 25)
    ).pack(side=TOP, pady=30)
    admin_id = Label(
        frame, text="ADMIN-ID", background="light green", font=("Arial", 15)
    ).pack()
    enter_admin_id = Entry(frame, textvariable=admin1, width=30, bd=5, font=("Arial", 15))
    enter_admin_id.pack(
        side=TOP, pady=10
    )
    password = Label(
        frame, text="PASSWORD", background="light green", font=("Arial", 15)
    ).pack()
    enter_password = Entry(frame, show="*", textvariable=pas, width=30, bd=5, font=("Arial", 15))
    enter_password.pack(
        side=TOP, pady=10
    )

    # ---------Check Login info and display respective message----------#
    def handle_login():
        id_1 = enter_admin_id.get()
        passwrd = enter_password.get()
        count = 0
        if id_1 == "" and passwrd == "":
            messagebox.showinfo("Information", "Please Enter Username and Password to Login.")
        else:
            sql = "select admin_id,admin_password from admin_data"
            c.execute(sql)
            result = c.fetchall()
            conn.commit()
            for b in result:
                if id_1 == b[0] and passwrd == b[1]:
                    count += 1
            if count == 1:
                messagebox.showinfo('Success', "Login Successfull")
                root.destroy()
                admin_home()
            else:
                messagebox.showinfo('Error', 'Invalid Username or Password')

    submit = Button(
        root,
        text="SUBMIT",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal", command=handle_login
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
    root.mainloop()
