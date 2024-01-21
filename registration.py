# ----------------Student Registration Form------------#

from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
from student import *
import os, sys
import re
import email
from tkinter import messagebox
import mysql.connector

# ----------------Global Decleration of variables-----------#
global connection
global enter_fname
global enter_lname
global enter_contact
global enter_course
global enter_dob
global var
global enter_email
global enter_password
global reenter_password


def open_registration():
    window = Tk()

    # ------------------varaible type decleration-------------#
    enter_fname = StringVar()
    enter_lname = StringVar()
    enter_contact = IntVar()
    enter_course = StringVar()
    var = StringVar()
    enter_dob = StringVar()
    enter_email = StringVar()
    enter_password = StringVar()
    reenter_password = StringVar()

    frame = Frame(window, background="light green")
    frame.pack()

    window.title("Registration Form")
    window.minsize(600, 1000)
    window.maxsize(600, 1000)
    window.configure(background="light green")

    # ----------------frame and all the content insode the main frame-----------#

    a = Label(
        frame, text="Registration Form", background="light green", font=("Verdana", 25)
    )
    a.pack(side=TOP, pady=30)

    fname = Label(
        frame, text="ENTER FIRST NAME : ", background="light green", font=("Arial", 15)
    )
    fname.pack()
    enter_fname = Entry(frame, width=30, bd=5, font=("Arial", 15))
    enter_fname.pack(side=TOP, pady=10)

    lname = Label(
        frame, text="ENTER LAST NAME : ", background="light green", font=("Arial", 15)
    )
    lname.pack()
    enter_lname = Entry(frame, width=30, bd=5, font=("Arial", 15))
    enter_lname.pack(side=TOP, pady=10)

    contact_number = Label(
        frame,
        text="ENTER CONTACT NUMBER : ",
        background="light green",
        font=("Arial", 15),
    )
    contact_number.pack()
    enter_contact = Entry(frame, width=30, bd=5, font=("Arial", 15))
    enter_contact.pack(side=TOP, pady=10)

    course = Label(
        frame, text="ENTER COURSE : ", background="light green", font=("Arial", 15)
    )
    course.pack()
    enter_course = Entry(frame, width=30, bd=5, font=("Arial", 15))
    enter_course.pack(side=TOP, pady=10)

    # ---------------calender window function----------#

    def show_calender():
        date_window = Toplevel()
        date_window.title("Select a Date:")
        date_window.grab_set()
        date_window.geometry("250x250+590+370")
        cal = Calendar(date_window, selectmode="day", data_pattern="mm/dd/y")
        cal.place(x=0, y=0)

        def grab_date():
            enter_dob.delete(0, END)
            enter_dob.insert(0, cal.get_date())

        submit = Button(
            date_window,
            text="submit",
            command=lambda: [grab_date(), date_window.destroy()],
        )
        submit.place(x=100, y=200)
        date_window.mainloop()

    dob = Label(
        frame,
        text="ENTER DATE OF BIRTH : ",
        background="light green",
        font=("Arial", 15),
    )
    dob.pack()
    enter_dob = Entry(frame, width=10, bd=5, font=("Arial", 15))
    enter_dob.insert(0, ("dd/mm/yyyy"))
    enter_dob.place(x=30, y=480)
    enter_btn = Button(
        window,
        text="choose date",
        font=("Verdana", 10),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=show_calender,
    )
    enter_btn.place(x=350, y=480)
    enter_dob.bind("<1>", show_calender)

    email = Label(
        frame, text="ENTER EMAIL : ", background="light green", font=("Arial", 15)
    )
    email.pack(side=TOP, pady=(60, 10))
    enter_email = Entry(frame, width=30, bd=5, font=("Arial", 15))
    enter_email.pack()

    password = Label(
        frame, text="ENTER PASSWORD : ", background="light green", font=("Arial", 15)
    )
    password.pack()
    enter_password = Entry(frame, show="*", width=30, bd=5, font=("Arial", 15))
    enter_password.pack(side=TOP, pady=10)

    reenterpassword = Label(
        frame, text="RE-ENTER PASSWORD : ", background="light green", font=("Arial", 15)
    )
    reenterpassword.pack()
    reenter_password = Entry(frame, show="*", width=30, bd=5, font=("Arial", 15))
    reenter_password.pack(side=TOP, pady=10)

    # ------------------clear button function------------------#

    def clear():
        enter_fname.delete(0, END)
        enter_lname.delete(0, END)
        enter_contact.delete(0, END)
        enter_course.delete(0, END)
        enter_dob.delete(0, END)
        enter_email.delete(0, END)
        enter_password.delete(0, END)
        reenter_password.delete(0, END)

    # ------------------data check function----------------#

    def registration_2(i, b, k, d, e, f, g, h):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hardik01",
            port="3306",
            database="management",
        )
        c = connection.cursor()
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        i = enter_fname.get()
        b = enter_lname.get()
        k = enter_contact.get()
        d = enter_course.get()
        e = enter_dob.get()
        f = enter_email.get()
        g = enter_password.get()
        h = reenter_password.get()
        if i == "":
            messagebox.showinfo("Error", "FIRST NAME FIELD IS NECESSARY.")
        elif i.isalpha() == False:
            messagebox.showinfo("Error", "NAME SHOULD ONLY CONTAIN ALPHABETS.")
        else:
            if b == "":
                messagebox.showinfo("Error", "LAST NAME FIELD IS NECESSARY.")
            if b.isalpha() == False:
                messagebox.showinfo("Error", "NAME SHOULD ONLY CONTAIN ALPHABETS.")
            else:
                if len(k) > 10 or len(k) < 10 or k.isdigit() == False:
                    messagebox.showinfo(
                        "Error", "CONTACT NUMBER MUST CONTAIN 10 DIGITS."
                    )
                else:
                    if d == "":
                        messagebox.showinfo("Error", "COURSE FIELD IS NECESSARY")
                    else:
                        if e == "":
                            messagebox.showinfo(
                                "Error", "DOB FIELD SHOULD NOT BE EMPTY"
                            )
                        else:
                            if not re.fullmatch(regex, f):
                                messagebox.showinfo(
                                    "Error", "THE EMAIL ADDRESS IS NOT VALID."
                                )
                            else:
                                if not re.search(pat, g):
                                    messagebox.showinfo("Error", "INVALID PASSWORD")
                                else:
                                    if h != g:
                                        messagebox.showinfo(
                                            "Error", "THE PASSWORDS DO NOT MATCH"
                                        )
                                    else:
                                        window.destroy()
                                        insert_query = "insert into `registration_student`(`first_name`,`last_name`,`contact_number`,`course`,`date_of_birth`,`email`,`password`) values(%s,%s,%s,%s,%s,%s,%s)"
                                        vals = (i, b, k, d, e, f, g)
                                        c.execute(insert_query, vals)
                                        connection.commit()
                                        messagebox.showinfo(
                                            "Registration Successful",
                                            "Now you may login",
                                        )
                                        open_student_login()

    dsub = Button(
        window,
        text="Submit",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=lambda: [
            registration_2(
                enter_fname,
                enter_lname,
                enter_contact,
                enter_course,
                enter_dob,
                enter_email,
                enter_password,
                reenter_password,
            )
        ],
    ).place(x=350, y=800)
    back = Button(
        window,
        text="BACK",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=window.destroy,
    ).place(x=250, y=800)
    clear = Button(
        window,
        text="Clear",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal",
        command=clear,
    ).place(x=150, y=800)

    window.mainloop()
