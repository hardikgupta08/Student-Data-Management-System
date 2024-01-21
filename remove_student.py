# --------------Remove Student-----------#

# ------------Necessary Import Files----------#
from tkinter import *
import mysql.connector
from tkinter import messagebox

# ---------------global variables--------------#
global enter_email_stu
global count


def remove_stud():
    root = Tk()
    root.title("Remove Student")
    root.minsize(600, 500)
    root.maxsize(600, 500)
    root["bg"] = "#90EE90"

    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="hardik01",
        port=3306,
        database="management",
    )
    c = conn.cursor()

    enter_email_stu = StringVar()

    head = Label(
        root, text="Remove a Student", font=("Inter", 30), background="light green"
    ).pack(side=TOP, pady=(50, 0))
    email = Label(
        root, text="Enter Email:", font=("Inter", 30), background="light green"
    ).pack(side=TOP, pady=(50, 0))
    enter_email_stu = Entry(root, width=30, bd=5, font=("Arial", 15))
    enter_email_stu.pack(side=TOP, pady=(30, 0))

    # -----------------check Function---------------#
    def check(enter_email_stu):
        i = enter_email_stu.get()
        if i == "":
            messagebox.showinfo(
                "Alert",
                "Please enter the email of the Student whose data is to be deleted",
            )
        else:
            sql2 = f'delete from registration_student where email = "{i}"'
            sql3 = f'delete from marks where email = "{i}"'
            c.execute(sql2)
            c.execute(sql3)
            conn.commit()
            root.destroy()
            messagebox.showinfo("Info", "Student Deleted Successfully")

    submit = Button(
        root,
        text="SUBMIT",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=lambda: [check(enter_email_stu)],
    ).pack()
    root.mainloop()
