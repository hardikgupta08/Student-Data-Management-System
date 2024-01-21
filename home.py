#---------Base Window----------#

from tkinter import *
from admin_login import *
from student import *
from registration import *

root = Tk()
frame = Frame(root, background="light green")
frame.pack()

root["bg"] = "#90EE90"
root.geometry("600x600")
root.title("Welcome")
root.maxsize(800, 800)

wel = Label(frame, text="WELCOME", font=("Inter", 30), background="light green").pack(
    side=TOP, pady=(50, 0)
)
#---------Admin Login Button----------#
admin = Button(
    frame,
    text="ADMIN LOGIN",
    font=("Verdana", 13),
    bd="5",
    bg="teal",
    fg="black",
    activebackground="teal",
    command=open_admin_page,
).pack(side=TOP, pady=50)

#---------Existing Student Login----------#

existing_user = Button(
    frame,
    text="EXISTING STUDENT? SIGN IN.",
    font=("Verdana", 13),
    bd="5",
    bg="teal",
    fg="black",
    activebackground="teal",
    command=open_student_login,
).pack(side=TOP, pady=50)

#---------New Student Creation----------#

new_user = Button(
    frame,
    text="NEW STUDENT? REGISTER NOW.",
    font=("Verdana", 13),
    bd="5",
    bg="teal",
    fg="black",
    activebackground="teal",
    command=open_registration,
).pack(side=TOP, pady=50)

root.mainloop()
