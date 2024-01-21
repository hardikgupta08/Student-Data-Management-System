#-----------------New Admin Creation Page-------------#

#-------------Necessary import files-----------#
from tkinter import *
import mysql.connector
from tkinter import messagebox
import re

#--------------global variables-----------#
global name
global ad
global pas


def create_new_admin():
    root = Tk()
    root.title("New Admin")
    root['bg'] = "#90EE90"
    label = Label(root, text = "Create New Admin",font=("Inter", 30), background="light green").pack(
    side=TOP, pady=(50, 0))
    
    #------------SQL connection---------------#
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "hardik01",port ="3306",database = "management")
    c = connection.cursor()


    name = StringVar()
    ad = StringVar()
    pas = StringVar()
    
    
    new_name  = Label(root, text = "ENTER NEW ADMIN NAME: ",background="light green", font=("Arial", 15)
    ).pack()
    name = Entry(root,width=30, bd=5, font=("Arial", 15))
    name.pack(side =TOP, pady = 10)
    new_ad  = Label(root, text = "ENTER NEW ADMIN ID: ",background="light green", font=("Arial", 15)
    ).pack()
    ad = Entry(root,width=30, bd=5, font=("Arial", 15))
    ad.pack(side=TOP, pady=10)
    ad_pas = Label(root, text = "Enter Admin Password: ",background="light green", font=("Arial", 15)
    ).pack()
    pas = Entry(root, width = 30, bd = 5, font=("Arial", 15))
    pas.pack(side=TOP, pady=10)

    #------------Check Data in Admin and Validate the data------------#
    def check_admin(i,j,k):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"    
        pat = re.compile(reg)
        i = name.get()
        j = ad.get()
        k = pas.get()
        if i == "" or j == "" or k == "":
            messagebox.showinfo("Error","Enter all of the required data.")
        elif not re.search(pat, k):
            messagebox.showinfo("Error","Invalid Password Format.")
        else:
            sql = "select admin_id from admin_data;"
            c.execute(sql)
            result = c.fetchall()
            connection.commit()
            count = 0
            if result:
                for a in result:
                    b = list(a)
                    for z in b:
                        if j == z:
                            count +=1
                if count != 0:
                    messagebox.showinfo("Alert","The User already Exists. Please Enter a different ID.")
                else:
                    insert_query = "insert into `admin_data`(`name`,`admin_id`,`admin_password`) values(%s,%s,%s);"
                    vals = (i,j,k)                                        
                    c.execute(insert_query,vals)
                    connection.commit()
                    root.destroy()
                    messagebox.showinfo("Info","New User Created Successfully.")
            else:
                insert_query = "insert into `admin_data`(`name`,`admin_id`,`admin_password`) values(%s,%s,%s);"
                vals = (i,j,k)                                        
                c.execute(insert_query,vals)
                connection.commit()
                root.destroy()
                messagebox.showinfo("Info","New User Created Successfully.")

        
    submit = Button(
        root,
        text="SUBMIT",
        font=("Verdana", 15),
        bd="5",
        bg="teal",
        fg="black",
        activebackground="teal", command = lambda:[check_admin(name,ad,pas)]
    ).pack()
    root.mainloop()