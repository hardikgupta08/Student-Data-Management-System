#---------------Update Student Marks----------#

#-------------Necessary Import Statements--------#
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

#---------------global variables-------------#
global enter_stu_email
global enter_ass_1
global enter_ass_2
global enter_ass_3
global enter_final
global count


def update_marks_student():
    root = Tk()
    root['bg'] = "#90EE90"
    root.title("Update Marks")
    root.minsize(600,800)

    enter_stu_email = StringVar()
    enter_ass_1 = IntVar()
    enter_ass_2 = IntVar()
    enter_ass_3 = IntVar()
    enter_final = IntVar()


    stu = Label(root, text = "Update Marks Database",background="light green", font=("Verdana", 20)
        ).place(x= 120,y = 75)
    conn  =mysql.connector.connect(host = "localhost", username = "root", password = "hardik01", port = 3306,database = "management")
    c= conn.cursor()
    stu_email = Label(root, text= "Enter Student Email :",background="light green", font=("Verdana", 15)
    ).pack(side=TOP, pady=(150,0))
    enter_stu_email = Entry(root,width=30, bd=5, font=("Arial", 15))
    enter_stu_email.pack(
        side=TOP, pady=10
    )
    ass_1 = Label(root, text= "Enter Assignment 1 Marks :",background="light green", font=("Verdana", 15)
    ).pack(side=TOP, pady=(30,0))
    enter_ass_1 = Entry(root,width=30, bd=5, font=("Arial", 15))
    enter_ass_1.pack(
        side=TOP, pady=10
    )
    ass_2 = Label(root, text= "Enter Assignment 2 Marks :",background="light green", font=("Verdana", 15)
    ).pack(side=TOP, pady=(30,0))
    enter_ass_2 = Entry(root,width=30, bd=5, font=("Arial", 15))
    enter_ass_2.pack(
        side=TOP, pady=10
    )
    ass_3 = Label(root, text= "Enter Assignment 3 Marks :",background="light green", font=("Verdana", 15)
    ).pack(side=TOP, pady=(30,0))
    enter_ass_3 = Entry(root,width=30, bd=5, font=("Arial", 15))
    enter_ass_3.pack(
        side=TOP, pady=10
    )
    final = Label(root, text= "Enter Final Exam Score :",background="light green", font=("Verdana",15)
    ).pack(side=TOP, pady=(30,0))
    enter_final = Entry(root,width=30, bd=5, font=("Arial", 15))
    enter_final.pack(
        side=TOP, pady=10
    )
    
    
    #-----------------update check and database connect-------------#        
    def update(a,b,d,e,f):
        a = enter_stu_email.get()
        b = enter_ass_1.get()
        d = enter_ass_2.get()
        e = enter_ass_3.get()
        f = enter_final.get()
        sql1 = "select email from registration_student"
        c.execute(sql1)
        results =c.fetchall()
        conn.commit()
        count = 0
        for i in results:
            u = list(i)
            for z in u:
                if a == z:
                    count +=1
        if a == "":
            messagebox.showinfo("Error","Please Enter the Email.")
        elif count == 0:
            messagebox.showinfo("Alert","Please enter an Email ID that exists in the data.")
        else:
            if b == "":
                messagebox.showinfo("Error","Please Enter the Assignment 1 Marks.")
            else:
                if d == "":
                    messagebox.showinfo("Error","Please Enter the Assignment 2 Marks")
                else:
                    if e == "":
                        messagebox.showinfo("Error","Please Enter the Assignment 3 Marks")
                    else:
                        if f=="":
                            messagebox.showinfo("Error","Please Enter The Student's Final Exam Score.")
                        else:
                            sql2 = f'insert into `marks`(`email`,`assignment_1`,`assignment_2`,`assignment_3`,`final_exam`) values("{a}",{b},{d},{e},{f})'                                       
                            c.execute(sql2)
                            conn.commit()
                            root.destroy()
                            messagebox.showinfo("Info","Marks data updated.")
    
    submit = Button(
        root,
        text="SUBMIT",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal", command = lambda:[update(enter_stu_email,enter_ass_1,enter_ass_2,enter_ass_3,enter_final)]
    ).pack()
    root.mainloop()