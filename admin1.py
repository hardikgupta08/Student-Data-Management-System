# ------------Admin Home Page-----------#

# -------------Necessary Import Files----------#
from tkinter import *
from tkinter import ttk
from new_admin import *
from update_marks import *
from PIL import Image, ImageTk
from new_student import *
import mysql.connector
from remove_student import *
from random import *


# ---------------global variable---------------#
global data


# ------------Admin Page After Login-----------#
def admin_home():
    root = Tk()
    root["bg"] = "#90EE90"
    root.title("Admin Home Page")
    root.minsize(1500, 1000)
    root.maxsize(1500, 1000)

    # ----------------SQL connection-------------#
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hardik01",
        port="3306",
        database="management",
    )
    c = connection.cursor()

    stu = Label(
        root, text="Student Database", background="light green", font=("Verdana", 25)
    ).pack(side=TOP)

    # -------------Details Display Frame-----------------#
    Table_details = Frame(root, relief="ridge")
    Table_details.place(x=250, y=100, width=890, height=465)
    scroll_x = Scrollbar(Table_details, orient=HORIZONTAL)
    scroll_y = Scrollbar(Table_details, orient=VERTICAL)

    data = ttk.Treeview(
        Table_details,
        column=(
            "Student ID",
            "First Name",
            "Last Name",
            "Contact Number",
            "Course Opted",
            "Date Of Birth",
            "Email",
            "Password",
            "Assignment 1",
            "Assignment 2",
            "Assignment 3",
            "Final Exam",
        ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
    )

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=data.xview)
    scroll_y.config(command=data.yview)

    data.heading("Student ID", text="Student ID")
    data.heading("First Name", text="First Name")
    data.heading("Last Name", text="Last Name")
    data.heading("Contact Number", text="Contact Number")
    data.heading("Course Opted", text="Course Opted")
    data.heading("Date Of Birth", text="Date Of Birth")
    data.heading("Email", text="Email")
    data.heading("Password", text="Password")
    data.heading("Assignment 1", text="Assignment 1")
    data.heading("Assignment 2", text="Assignment 2")
    data.heading("Assignment 3", text="Assignment 3")
    data.heading("Final Exam", text="Final Exam")

    data["show"] = "headings"
    data.column("Student ID", width=100)
    data.column("First Name", width=100)
    data.column("Last Name", width=100)
    data.column("Contact Number", width=100)
    data.column("Course Opted", width=100)
    data.column("Date Of Birth", width=100)
    data.column("Email", width=100)
    data.column("Password", width=100)
    data.column("Assignment 1", width=100)
    data.column("Assignment 2", width=100)
    data.column("Assignment 3", width=100)
    data.column("Final Exam", width=100)

    data.pack(fill=BOTH, expand=1)

    # ---------------Fetch Data---------------#
    def fetch():
        sql = "select registration_student.id,registration_student.first_name,registration_student.last_name,registration_student.contact_number,registration_student.course,registration_student.date_of_birth,registration_student.email,registration_student.password,marks.assignment_1,marks.assignment_2,marks.assignment_3,marks.final_exam from registration_student, marks where registration_student.email = marks.email"
        c.execute(sql)
        result = c.fetchall()
        for i in result:
            data.insert("", END, values=i)
        connection.commit()

    # ------------Refresh the Details Frame----------#
    def refresh():
        for i in data.get_children():
            data.delete(i)
        Table_details.after(1000, fetch)

    fetch()

    refresh = Button(
        root,
        text="Refresh Data",
        font=("Verdana", 13),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=refresh,
    )
    refresh.place(x=1000, y=10)
    add_new = Button(
        root,
        text="Add New Student",
        font=("Verdana", 13),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=new_student_entry,
    ).place(x=200, y=700)
    remove_stu = Button(
        root,
        text="Remove Student",
        font=("Verdana", 13),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=remove_stud,
    ).place(x=1000, y=700)
    add_admin = Button(
        root,
        text="Add New Admin",
        font=("Verdana", 13),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=create_new_admin,
    ).place(x=450, y=700)
    update_marks = Button(
        root,
        text="Update Student Marks",
        font=("Verdana", 13),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=update_marks_student,
    ).place(x=700, y=700)
    log = Button(
        root,
        text="Logout",
        font=("Verdana", 13),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=root.destroy,
    ).place(x=1200, y=700)
    root.mainloop()
