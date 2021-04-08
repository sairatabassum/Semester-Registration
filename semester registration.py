from tkinter import *
import os.path
from os import path
from tkinter import ttk
from tkinter import messagebox

def main():

 if __name__== "__main__":
   main()


#---Add new registration data---
def add_f():

    file=ID_entry.get()+'.txt'
    c=str(path.exists(file))
    #print(c)

    if(ID_entry.get()==""or Name_entry.get()==""or Section_entry.get()=="" or Status_Combo.get()=="" or len(Course_txt.get("1.0", "end-1c")) == 0 ):
        messagebox.showwarning("Error!", "All entries are required!!")

    elif (c == "True"):
        messagebox.showwarning("Error!","ID EXIST")

    else:
        file1 = open(file, 'a')

        file1.write(ID_entry.get() + "\n")
        file1.write(Name_entry.get() + "\n")
        file1.write(Section_entry.get() + "\n")
        file1.write(Status_Combo.get())
        file1.write("\n")
        file1.write(Course_txt.get("1.0", "end"))

        messagebox.showinfo("Success", "Add Successfully!!")

        file1.close()



#---Clear the Entry Bar--
def clear():
    ID_entry.delete(0, END)
    ID_entry.insert(0, "")

    Name_entry.delete(0, END)
    Name_entry.insert(0, "")

    Section_entry.delete(0, END)
    Section_entry.insert(0, "")

    Course_txt.delete("1.0", "end")
    Course_txt.insert(END, "")

    Status_Combo.set("")






def search_f():
    file = s1.get() + '.txt'
    c = str(path.exists(file))
    #print(c)


    if s1.get()=="":
        messagebox.showerror("Error!", "Search bar is empty!!")


    elif (c == "True"):
        w.delete("1.0", "end")
        w.insert(END, 30*blank+"Record is found!!")


    else:
        w.delete("1.0", "end")
        w.insert(END, 26*blank+"Record is not found!!")


def show_f():

    file = s1.get() + '.txt'
    c = str(path.exists(file))


    if s1.get()=="":
        messagebox.showerror("Error!", "Search bar is empty!!")

    elif c=="False":
        messagebox.showwarning("Error!", "Not Found!!")

    else:
        clear()
        f = open(s1.get()+".txt")

        f1 = f.readlines()
        i = 0
        yo = ""
        for x in f1:
            i += 1
            if i == 1:
                ID_entry.insert(0,x)
            elif i == 2:
                Name_entry.insert(0,x)
            elif i == 3:
                Section_entry.insert(0,x)
            elif i == 4:
                Status_Combo.set(x)
            else:
                yo += x
        Course_txt.insert(END, yo)




def delete_f():

    file = ID_entry.get() + '.txt'
    c = str(path.exists(file))

    print(c)

    if c=="True":
        os.remove(file)
        messagebox.showinfo("Delete", "Deleted Successfully!!")
    elif c=="False":
        messagebox.showerror("Error!", "Record is not exist!!")


def update_f():


    if (ID_entry.get() == "" or Name_entry.get() == "" or Section_entry.get() == "" or Status_Combo.get() == "" or len(Course_txt.get("1.0", "end-1c")) == 0):
        messagebox.showwarning("Error!", "All entries are required!!")
    else:
        if os.path.exists(s1.get()+'.txt'):
            os.remove(s1.get()+'.txt')
        else:
            print("The record does not exist")

        file1 = open(s1.get()+".txt", "a")
        file1.write(ID_entry.get())
        file1.write(Name_entry.get())
        file1.write(Section_entry.get())
        file1.write(Status_Combo.get())
        #file1.write("\n")
        file1.write(Course_txt.get("1.0", "end"))
        file1.close()

        messagebox.showinfo("Update", "Updated Successfully!!")

def clear1_f():
    w.delete("1.0", "end")
    w.insert(END, "")

    s1.delete(0, END)
    s1.insert(0, "")


#---Windows---
root=Tk()
blank=" "
root.title(200*blank+"Semester Registration")
root.iconbitmap(r'diu.ico')
root.geometry("1350x650")
root.configure(bg="#A9A9A9")




#----All_Variables----
id=StringVar()
name=StringVar()
section=StringVar()
course=StringVar()
status=StringVar()

#---Title---
t=Label(root,text="Semester Registration",font=("Times new roman",40,"bold"),height=1,width=1350,anchor=N,bg="#B22222",fg="#F5FFFA",bd=10,relief=GROOVE)
t.pack()

#---Frame1---
Frame_1=Frame(root,bd=10,relief=RIDGE,bg="#b62d2d")
Frame_1.place(x=20,y=100,width=560,height=600)


#---Frame1-Title------
Frame_1_title=Label(Frame_1,text=16*blank+"Add New Registration Data"+13*blank,bd=5,relief=GROOVE,fg="white",bg="#b62d2d",font=("Times new roman",20,"bold"))
Frame_1_title.grid(row=0,columnspan=2)


#----Entry----
ID=Label(Frame_1,text="ID No: ",fg="white",bg="#b62d2d",font=("Times new roman",15,"bold"))
ID.grid(row=1,column=0,sticky="w",padx=10,pady=20)
ID_entry=Entry(Frame_1,textvariable=id,bd=5,relief=GROOVE,font=("Times new roman",15),width=32)
ID_entry.grid(row=1,column=1,sticky="w",pady=40,padx=10)



Name=Label(Frame_1,text="Name: ",fg="white",bg="#b62d2d",font=("Times new roman",15,"bold"))
Name.grid(row=2,column=0,sticky="w",padx=10,pady=20)
Name_entry=Entry(Frame_1,textvariable=name,bd=5,relief=GROOVE,font=("Times new roman",15),width=32)
Name_entry.grid(row=2,column=1,sticky="w",pady=20,padx=10)



Section=Label(Frame_1,text="Section: ",fg="white",bg="#b62d2d",font=("Times new roman",15,"bold"))
Section.grid(row=3,column=0,sticky="w",padx=10,pady=20)
Section_entry=Entry(Frame_1,textvariable=section,bd=5,relief=GROOVE,font=("Times new roman",15),width=32)
Section_entry.grid(row=3,column=1,sticky="w",pady=40,padx=10)



Status=Label(Frame_1,text="Registration Status: ",fg="white",bg="#b62d2d",font=("Times new roman",15,"bold"))
Status.grid(row=4,column=0,sticky="w",padx=5,pady=10)
Status_Combo=ttk.Combobox(Frame_1,textvariable=status,font=("Times new roman",15),width=31,state="readonly")
Status_Combo['values']=("Pending","Partially Complete","Complete")
Status_Combo.grid(row=4,column=1,sticky="w",padx=5,pady=20)



Course=Label(Frame_1,text="Write Course: ",fg="white",bg="#b62d2d",font=("Times new roman",15,"bold"))
Course.grid(row=5,column=0,sticky="w",padx=10,pady=20)
Course_txt=Text(Frame_1,width=30,height=3,font=("",15))
Course_txt.grid(row=5,column=1,sticky="w",padx=5,pady=20)



#----Button_Frame---
Button_Frame=Frame(Frame_1,bd=5,relief=RIDGE,bg="#b62d2d")
Button_Frame.place(x=30,y=520,width=500)


#----3_Button----
clear_button=Button(Button_Frame,text="Clear",width=12,activebackground="#87CEFA",bg="#A9A9A9",command=clear)
clear_button.grid(row=0,column=1,padx=10,pady=10)
update_button=Button(Button_Frame,text="Update",width=12,activebackground="#87CEFA",bg="#A9A9A9",command=update_f)
update_button.grid(row=0,column=2,padx=10,pady=10)
Delete_button=Button(Button_Frame,text="Delete",width=15,activebackground ="#87CEFA",bg="#A9A9A9",command=delete_f)
Delete_button.grid(row=0,column=3,padx=10,pady=10)
Add_button=Button(Button_Frame,text="Add",width=12,activebackground ="#87CEFA",bg="#A9A9A9",command=add_f)
Add_button.grid(row=0,column=4,padx=10,pady=10)


#----Frame2----
Frame_2=Frame(root,bd=4,relief=RIDGE,bg="#b62d2d")
Frame_2.place(x=600,y=100,width=750,height=600)


#---Frame2_Title----
Frame_2_title=Label(Frame_2,text=36*blank+"Search By Student ID"+32*blank,bd=5,relief=GROOVE,fg="white",bg="#b62d2d",font=("Times new roman",20,"bold"))
Frame_2_title.grid(row=0,columnspan=3)


#----Search_Frame---
Search_Frame=Frame(Frame_2,bg="#b62d2d")
Search_Frame.place(x=20,y=50,width=650,height=540)


#---Search-----
s=Label(Search_Frame,text="Enter ID No: ",fg="white",bg="#b62d2d",font=("Times new roman",15,"bold"))
s.grid(row=0,column=0,sticky="w",padx=2,pady=10)
s1=Entry(Search_Frame,bd=2,font=("Times new roman",12),width=35)
s1.grid(row=0,column=1,sticky="w",pady=10,padx=2)
de=Button(Search_Frame,text="Search",width=8,height=0,bg="#A9A9A9",activebackground ="#87CEFA",font=("Times new roman",12),command=search_f)
de.grid(row=0,column=2,sticky="w",pady=10,padx=4)
details=Button(Search_Frame,text="Show Details",width=10,height=0,bg="#A9A9A9",activebackground ="#87CEFA",font=("Times new roman",12),command=show_f)
details.grid(row=0,column=3,sticky="w",pady=10,padx=4)


#---record_found---
w_Frame=Frame(Search_Frame,bg="#b62d2d")
w_Frame.place(x=20,y=50,width=650,height=540)
w=Text(w_Frame,width=105,height=5,font=("Times new roman",20,"bold"),fg="blue")
w.grid(row=0, column=0)
de2=Button(Search_Frame,text="Clear",width=8,height=0,bg="#A9A9A9",activebackground ="#87CEFA",font=("Times new roman",12),command=clear1_f)
de2.grid(row=3,column=1,padx=100,pady=160)

root.mainloop()
