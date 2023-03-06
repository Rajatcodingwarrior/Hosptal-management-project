from tkinter import *
import sqlite3 as sql
import matplotlib.pyplot as plt
import pandas as pd
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image
import gtts  
from playsound import playsound

conn=sql.connect("project.db")
c=conn.cursor()
conn2=sql.connect("project2.db")
c0=conn2.cursor()
root=Tk()
root.geometry("900x900")
root.minsize(900,900)
root.maxsize(900,900)
f1=Frame(root,bg="blue")
f2=Frame(root,bg="green")
f1.pack(side=TOP,fill=X)
f2.pack(side=TOP,fill=X)


##################################################
def getvalsm():
    rootra9=Toplevel()
    rootra9.geometry("1540x900")
    rootra9.title("Hospital Management 'hellow user'")
    fz0009=Frame(rootra9,bg="blue")

    imagec =Image.open('ppp.jpg')
    imager = ImageTk.PhotoImage(imagec)


    a=Label(fz0009,text="Topic : HOSPITAL MANAGEMENT",bg="red",fg="white",font="sansns 30 bold italic underline",borderwidth=5,relief=SUNKEN,padx=10)
    a.pack(pady=5)
    Button(fz0009,image=imager,command=umar,bg="red",fg="white",font="lucida",height=650,width=1350,borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=10)
    fz0009.pack(fill=X)
    Button(fz0009,text="end",bg="red",fg="white",font="sansns 50 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=350)
    fz0009.pack(fill=X)
    ooo=Frame(rootra9,bg="blue")
    Button(fz0009,text="end",bg="red",fg="white",font="sansns 50 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=350)
    fz0009.pack(fill=X)
    ooo.pack()
    rootra9.mainloop()
#######################################################

def umar():
    if userentry.get()=="rajat" and passentry.get()=="rkkr":
        t1 = gtts.gTTS("Welcome to our software of hospital manaagement")
        t1.save("welcome.mp3")
        playsound("welcome.mp3") 
        print("Welcome to our software of hospital manaagement")
        root2=Toplevel()
        root2.geometry("1530x900")
        root2.minsize(1530,900)
        root2.title("Main Menu")
        f1=Frame(root2,bg="blue",padx=5)
        a1=Label(f1,text="Topic : Hospital Mangement",bg="red",fg="white",font="sunsns 30 bold",borderwidth=10,relief=SUNKEN)
        a2=Label(f1,text="Main Menu",bg="red",fg="white",font="sunsns 30 bold",borderwidth=10,relief=SUNKEN)

        def pg1():
            root1 = Toplevel()
            root1.title("top window")
            root1.geometry("1570x900")

            def pp_1():
                with conn:
                    try:
                        c.execute("select * from Ward25")
                        a1=p_1.get()
                        a2=p_2.get()
                        a3=p_3.get()
                        c.execute(f"insert into Ward25(Ward_No,NO_of_patients,Floor) values(?,?,?)",(a1,a2,a3))
                        conn.commit()
                    except:
                        c.execute("create table Ward25(Ward_No int primary key,NO_of_patients int,Floor int);")
                        a1=p_1.get()
                        a2=p_2.get()
                        a3=p_3.get()
                        c.execute(f"insert into Ward25(Ward_No,NO_of_patients,Floor) values(?,?,?)",(a1,a2,a3))
                        conn.commit()                               

            def pp_2():
                with conn2:
                    try:
                        c0.execute("select * from patient3")
                        a4=p_4.get()
                        a5=p_5.get()
                        a6=p_6.get()
                        a7=p_7.get()
                        a8=p_8.get()
                        a9=p_9.get()
                        c0.execute(f"insert into patient3(srno, pname, fname, phno, sex, age) values(?,?,?,?,?,?)",(a4,a5,a6,a7,a8,a9))
                        conn2.commit()
                        c0.execute("select * from patient3")
                        print(c0.fetchall())

                    except:
                        c0.execute("create table patient3(srno int,pname varchar(50),fname varchar(50),phno int,sex varchar(50),age int);")
                        a4=p_4.get()
                        a5=p_5.get()
                        a6=p_6.get()
                        a7=p_7.get()
                        a8=p_8.get()
                        a9=p_9.get()
                        c0.execute(f"insert into patient3(srno, pname, fname, phno, sex, age) values(?,?,?,?,?,?)",(a4,a5,a6,a7,a8,a9))
                        conn2.commit()                                 
                        c0.execute("select * from patient3")
                        conn2.commit()                                 
                        print(c0.fetchall())


                
            def pp_3():
                with conn:
                    try:
                        c.execute("select * from doctors")
                        a10=p_10.get()
                        a11=p_11.get()
                        a12=p_12.get()
                        a13=p_13.get()
                        a14=p_14.get()
                        a15=p_15.get()
                        a16=p_16.get()
                        c.execute(f"insert into doctors(srno,dname,fname,age,sex,qualification,experience) values(?,?,?,?,?,?,?)",(a10,a11,a12,a13,a14,a15,a16))
                        conn.commit()
                    except:
                        c.execute("create table doctors(srno int primary key,dname varchar(50),fname varchar(50),age int,sex varchar(50),qualification varchar(50),experience int);")
                        a10=p_10.get()
                        a11=p_11.get()
                        a12=p_12.get()
                        a13=p_13.get()
                        a14=p_14.get()
                        a15=p_15.get()
                        a16=p_16.get()
                        c.execute(f"insert into doctors(srno,dname,fname,age,sex,qualification,experience) values(?,?,?,?,?,?,?)",(a10,a11,a12,a13,a14,a15,a16))
                        conn.commit()        


            f1=Frame(root1,bg="blue")
            Label(f1,text="Add New Record",bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(fill=X,pady=6)
            f1.pack(side=TOP,fill=X)
            f2=Frame(root1,bg="blue")
            Label(f2,text="New Ward",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f2.pack(side=TOP,fill=X)

            f3=Frame(root1,bg="blue")
            Label(f3,text="Ward No.",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f3,text="No. of Patient",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f3,text="Floor",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f3.pack(fill=X)

            f4=Frame(root1,bg="blue")
            p_1=IntVar()
            p_2=IntVar()
            p_3=IntVar()
            
            Entry(f4,textvariable=p_1,bg="white",fg="black",width=15,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            
            Entry(f4,textvariable=p_2,bg="white",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            
            Entry(f4,textvariable=p_3,bg="white",fg="black",width=15,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            
            f4.pack(fill=X)
            
            

            f5=Frame(root1,bg="blue")
            Button(f5,text="---Add Now",command=pp_1,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            
            f5.pack(fill=X)

            f6=Frame(root1,bg="blue")
            Label(f6,text="New Patient",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f6.pack(fill=X)

            f7=Frame(root1,bg="blue")
            Label(f7,text="Sr No.",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="PName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="FName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Ph.No.",bg="grey",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Sex",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Age",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f7.pack(fill=X)

            f8=Frame(root1,bg="blue")
            p_4=IntVar()
            p_5=StringVar()
            p_6=StringVar()
            p_7=IntVar()
            p_8=StringVar()
            p_9=IntVar()

            Entry(f8,textvariable=p_4,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p_5,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p_6,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p_7,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p_8,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p_9,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f8.pack(fill=X)

            f9=Frame(root1,bg="blue")
            Button(f9,text="---Add Now",command=pp_2,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f9.pack(fill=X)


            f10=Frame(root1,bg="blue")
            Label(f10,text="New Doctor",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT,anchor="w")
            f10.pack(fill=X)

            f11=Frame(root1,bg="blue")
            Label(f11,text="Sr No.",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="DName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="FName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Age",bg="grey",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Sex",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Qualification",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Experience(yr)",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f11.pack(fill=X)

            f12=Frame(root1,bg="blue")
            p_10=IntVar()
            p_11=StringVar()
            p_12=StringVar()
            p_13=IntVar()
            p_14=StringVar()
            p_15=StringVar()
            p_16=IntVar()

            Entry(f12,textvariable=p_10,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p_11,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p_12,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p_13,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p_14,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p_15,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p_16,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f12.pack(fill=X)

            f13=Frame(root1,bg="blue")
            Button(f13,text="---Add Now",command=pp_3,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f13.pack(fill=X)


            f14=Frame(root1,bg="blue")
            Button(f14,text="Click to go to previous page",command=root1.destroy,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=60)
            f14.pack(fill=X)




        def pg2():
            rootp2 = Toplevel()
            rootp2.title("Update Records ---P2")
            rootp2.geometry("1600x900")


            def p2_r():
                conn=sql.connect("project.db")
                c=conn.cursor()
                with conn:
                    z1=p22_1.get()
                    z2=p22_2.get()
                    z3=p22_3.get()
                    c.execute(f"update Ward25 set Ward_No={z1},NO_of_patients={z2},Floor={z3} where Ward_No={z1}")
                    conn.commit()
                    c.execute("select *  from Ward25")
                    c.fetchall()

            def p2_2():
                conn2=sql.connect("project2.db")
                c=conn.cursor()
                with conn2:
                    z4=p22_4.get()
                    z5=p22_5.get()
                    z6=p22_6.get()
                    z7=p22_7.get()
                    z8=p22_8.get()
                    z9=p22_9.get()
                    c0.execute(f"update patient3 set srno={z4},pname={z5},fname={z6},phno={z7},sex={z8},age={z9} where srno={z4}")
                    conn2.commit()
                    c0.execute("select *  from patient3")
                    c0.fetchall()

            def p2_3():
                conn=sql.connect("project.db")
                c=conn.cursor()
                with conn:
                    z10=p22_10.get()
                    z11=p22_11.get()
                    z12=p22_12.get()
                    z13=p22_13.get()
                    z14=p22_14.get()
                    z15=p22_15.get()
                    z16=p22_16.get()
                    c.execute(f"update doctors set srno={z10},dname={z11},fname={z12},age={z13},sex={z14},qualification={z15},experience={z16} where srno={z10}")
                    conn.commit()
                    c.execute("select *  from doctors")
                    c.fetchall()
            f1=Frame(rootp2,bg="blue")
            Label(f1,text="Update Records",bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(fill=X,pady=6)
            f1.pack(side=TOP,fill=X)
            f2=Frame(rootp2,bg="blue")
            Label(f2,text="Update Ward",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f2.pack(side=TOP,fill=X)

            f3=Frame(rootp2,bg="blue")
            Label(f3,text="Ward No.",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f3,text="No. of Patient",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f3,text="Floor",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f3.pack(fill=X)

            f4=Frame(rootp2,bg="blue")
            p22_1=IntVar()
            p22_2=IntVar()
            p22_3=IntVar()
            Entry(f4,textvariable=p22_1,bg="white",fg="black",width=15,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f4,textvariable=p22_2,bg="white",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f4,textvariable=p22_3,bg="white",fg="black",width=15,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f4.pack(fill=X)

            f5=Frame(rootp2,bg="blue")
            Button(f5,text="---Update Now",command=p2_r,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f5.pack(fill=X)

            f6=Frame(rootp2,bg="blue")
            Label(f6,text="Update Patient",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f6.pack(fill=X)

            f7=Frame(rootp2,bg="blue")
            Label(f7,text="Sr No.",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="PName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="FName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Ph.No.",bg="grey",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Sex",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Age",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f7.pack(fill=X)

            f8=Frame(rootp2,bg="blue")
            p22_4=IntVar()
            p22_5=StringVar()
            p22_6=StringVar()
            p22_7=IntVar()
            p22_8=StringVar()
            p22_9=IntVar()

            Entry(f8,textvariable=p22_4,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p22_5,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p22_6,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p22_7,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p22_8,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=p22_9,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f8.pack(fill=X)

            f9=Frame(rootp2,bg="blue")
            Button(f9,text="---Update Now",command=p2_2,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f9.pack(fill=X)


            f10=Frame(rootp2,bg="blue")
            Label(f10,text="Update Doctor",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT,anchor="w")
            f10.pack(fill=X)

            f11=Frame(rootp2,bg="blue")
            Label(f11,text="Sr No.",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="DName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="FName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Age",bg="grey",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Sex",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Qualification",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Experience(yr)",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f11.pack(fill=X)

            f12=Frame(rootp2,bg="blue")
            p22_10=IntVar()
            p22_11=StringVar()
            p22_12=StringVar()
            p22_13=IntVar()
            p22_14=StringVar()
            p22_15=StringVar()
            p22_16=IntVar()

            Entry(f12,textvariable=p22_10,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p22_11,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p22_12,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p22_13,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p22_14,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p22_15,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=p22_16,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f12.pack(fill=X)

            f13=Frame(rootp2,bg="blue")
            Button(f13,text="---Update Now",command=p2_3,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f13.pack(fill=X)


            f14=Frame(rootp2,bg="blue")
            Button(f14,text="Click to go to previous page",command=rootp2.destroy,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=60)
            f14.pack(fill=X)



            rootp2.mainloop()



        def pg3():
            rootp3 = Toplevel()
            rootp3.title("Delete Records ---P2")
            rootp3.geometry("1570x900")


            def p3_1():

                conn=sql.connect("project.db")
                c=conn.cursor()
                
                with conn:
                    y1=pr3_1.get()
                    y2=pr3_2.get()
                    y3=pr3_3.get()
                    c.execute(f"delete from Ward25 where Ward_No={y1} and NO_of_patients={y2}")
                    conn.commit()
                    c.execute("select *  from Ward25")
                    c.fetchall()


            def p3_2():

                conn2=sql.connect("project2.db")
                c0=conn2.cursor()
                
                with conn2:
                    y4=pr3_4.get()
                    y5=pr3_5.get()
                    y6=pr3_6.get()
                    y7=pr3_7.get()
                    y8=pr3_8.get()
                    y9=pr3_9.get()
                    c0.execute(f"delete from patient3 where srno={y4} and pname={y5}")
                    conn2.commit()
                    c0.execute("select *  from patient3")
                    c0.fetchall()
            def p3_3():
                conn=sql.connect("project.db")
                c=conn.cursor()
                
                with conn:
                    y10=pr3_10.get()
                    y11=pr3_11.get()
                    y12=pr3_12.get()
                    c.execute(f"delete from doctors where srno={y10} and dname={y11}")
                    conn.commit()
                    c.execute("select *  from doctors")
                    c.fetchall()
            f1=Frame(rootp3,bg="blue")
            Label(f1,text="Delete Records",bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(fill=X,pady=6)
            f1.pack(side=TOP,fill=X)
            f2=Frame(rootp3,bg="blue")
            Label(f2,text="Delete Ward",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f2.pack(side=TOP,fill=X)

            f3=Frame(rootp3,bg="blue")
            Label(f3,text="Ward No.",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f3,text="No. of Patient",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f3,text="Floor",bg="grey",fg="black",width=12,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f3.pack(fill=X)

            f4=Frame(rootp3,bg="blue")
            pr3_1=IntVar()
            pr3_2=IntVar()
            pr3_3=IntVar()
            Entry(f4,textvariable=pr3_1,bg="white",fg="black",width=15,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f4,textvariable=pr3_2,bg="white",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f4,textvariable=pr3_3,bg="white",fg="black",width=15,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f4.pack(fill=X)

            f5=Frame(rootp3,bg="blue")
            Button(f5,text="---Delete Now",command=p3_1,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f5.pack(fill=X)

            f6=Frame(rootp3,bg="blue")
            Label(f6,text="Delete Patient",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f6.pack(fill=X)

            f7=Frame(rootp3,bg="blue")
            Label(f7,text="Sr No.",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="PName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="FName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Ph.No.",bg="grey",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Sex",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f7,text="Age",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f7.pack(fill=X)

            f8=Frame(rootp3,bg="blue")
            pr3_4=IntVar()
            pr3_5=StringVar()
            pr3_6=StringVar()
            pr3_7=IntVar()
            pr3_8=StringVar()
            pr3_9=IntVar()

            Entry(f8,textvariable=pr3_4,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=pr3_5,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=pr3_6,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=pr3_7,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=pr3_8,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f8,textvariable=pr3_9,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f8.pack(fill=X)

            f9=Frame(rootp3,bg="blue")
            Button(f9,text="---Delete Now",command=p3_2,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f9.pack(fill=X)


            f10=Frame(rootp3,bg="blue")
            Label(f10,text="Delete Doctor",bg="grey",fg="black",font="sansns 16 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT,anchor="w")
            f10.pack(fill=X)

            f11=Frame(rootp3,bg="blue")
            Label(f11,text="Sr No.",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="DName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="FName",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Age",bg="grey",fg="black",width=14,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Sex",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Qualification",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            Label(f11,text="Experience(yr)",bg="grey",fg="black",width=13,font="sansns 14 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT)
            f11.pack(fill=X)

            f12=Frame(rootp3,bg="blue")
            pr3_10=IntVar()
            pr3_11=StringVar()
            pr3_12=StringVar()
            pr3_13=IntVar()
            pr3_14=StringVar()
            pr3_15=StringVar()
            pr3_16=IntVar()

            Entry(f12,textvariable=pr3_10,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=pr3_11,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=pr3_12,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=pr3_13,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=pr3_14,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=pr3_15,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            Entry(f12,textvariable=pr3_16,bg="white",fg="black",width=16,font="sansns 14 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
            f12.pack(fill=X)

            f13=Frame(rootp3,bg="blue")
            Button(f13,text="---Delete Now",command=p3_3,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=RIGHT)
            f13.pack(fill=X)


            f14=Frame(rootp3,bg="blue")
            Button(f14,text="Click to go to previous page",command=rootp3.destroy,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=60)
            f14.pack(fill=X)



            rootp3.mainloop()

        def pg4():
            rootp4 = Toplevel()
            rootp4.geometry("1530x900")
            rootp4.minsize(1530,900)
            rootp4.title("Display Records---P4")
            f4_1=Frame(rootp4,bg="blue",padx=5)
            a2=Label(f4_1,text="Display",bg="red",fg="white",font="sunsns 30 bold",borderwidth=10,relief=SUNKEN)

            def pg1():
                with conn:
                    c.execute("select * from Ward25")
                    df=c.fetchall()
                    df1=pd.DataFrame(df,columns=["Ward No.","No of Patients","Floor"])

                    rootra=Tk()
                    rootra.geometry("1540x900")
                    rootra.title("Display WARD TABLE..................%")
                    f0001=Frame(rootra,bg="blue")


                    a=Label(f0001,text="-----------------WARD TABLE----------------",bg="red",fg="white",font="sansns 30 bold",borderwidth=5,relief=SUNKEN,padx=10)
                    a.pack(pady=5)


                    Button(f0001,text=f"{df1.to_string(index=False)}",command=rootra.destroy,bg="red",fg="white",font="lucida 20 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=10)
                    f0001.pack(fill=X)
                    Button(f0001,text="end",bg="red",fg="white",font="sansns 50 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=350)
                    f0001.pack(fill=X)


                    rootra.mainloop()
                    

                


            def pg2():
                with conn2:
                    c0.execute("select * from patient3")
                    dfr=c0.fetchall()
                    dfr1=pd.DataFrame(dfr,columns=["Srno","FName","PName","Ph_No","Sex","Age"])

                    rootrra=Tk()
                    rootrra.geometry("1540x900")
                    rootrra.title("Display PATIENT TABLE..................%")
                    f00001=Frame(rootrra,bg="blue")


                    a=Label(f00001,text="-----------------PATIENT TABLE----------------",bg="red",fg="white",font="sansns 30 bold",borderwidth=5,relief=SUNKEN,padx=10)
                    a.pack(pady=5)


                    Button(f00001,text=f"{dfr1.to_string(index=False)}",command=rootrra.destroy,bg="red",fg="white",font="lucida 20 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=10)
                    f00001.pack(fill=X)
                    gamma=Button(f00001,text="end",bg="red",fg="white",font="sansns 50 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5)
                    gamma.pack(pady=350)
                    f00001.pack(fill=X)


                    rootrra.mainloop()
            def pg3():
                with conn:
                    c.execute("select * from doctors")
                    dfz=c.fetchall()
                    dfz1=pd.DataFrame(dfz,columns=["srnn","dname","fname","age","sex","qualification","experience"])

                    rootra2=Tk()
                    rootra2.geometry("1540x900")
                    rootra2.title("Display DOCTORS TABLE..................%")
                    fz0001=Frame(rootra2,bg="blue")


                    a=Label(fz0001,text="-----------------DOCTORS TABLE----------------",bg="red",fg="white",font="sansns 30 bold",borderwidth=5,relief=SUNKEN,padx=10)
                    a.pack(pady=5)


                    Button(fz0001,text=f"{dfz1.to_string(index=False)}",command=rootra2.destroy,bg="red",fg="white",font="lucida 20 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=10)
                    fz0001.pack(fill=X)
                    Button(fz0001,text="end",bg="red",fg="white",font="sansns 50 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).pack(pady=350)
                    fz0001.pack(fill=X)
                    rootra2.mainloop()
                    




            b1=Button(f4_1,text="1.Ward Records",command=pg1,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=10,pady=15)
            b2=Button(f4_1,text="2.Patient Records",command=pg2,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=20,pady=15)
            b3=Button(f4_1,text="3.Doctor RecordS",command=pg3,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=25,pady=15)

            f4_1.pack(side=TOP,fill=X)
            a2.pack(side=TOP,pady=5,fill=X)
            b1.pack(side=TOP,anchor="nw",pady=15)
            b2.pack(side=TOP,anchor="nw",pady=15)
            b3.pack(side=TOP,anchor="nw",pady=15)
            f4_2=Frame(rootp4,bg="blue")
            Button(f4_2,text="Click to go to previous page",command=rootp4.destroy,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=170,side=BOTTOM)
            f4_2.pack(fill=X)
            rootp4.mainloop()

        def pg5():
            rootp5 = Toplevel()
            rootp5.title("Statistics----P5")
            rootp5.geometry("1570x900")


            def p55_1():
                conn=sql.connect("project.db")
                c=conn.cursor()
                with conn:

                    c.execute("select * from Ward25")
                    df2=c.fetchall()
                    df2=pd.DataFrame(df2,columns=["Ward No","No of Patients",".    |Floor"])
                    df2.plot.bar(x="Ward No",y="No of Patients",rot=0,title="BAR GRAPH",xlabel="Ward No",ylabel="No of Patients",color="red")
                    plt.show()


            def p55_2():

                conn=sql.connect("project.db")
                c=conn.cursor()
                with conn:

                    c.execute("select * from Ward25")
                    df2=c.fetchall()
                    df2=pd.DataFrame(df2,columns=["Ward No","No of Patients",".    |Floor"])
                    df2.plot.pie(x="Ward No",y="No of Patients",title="BAR GRAPH")
                    plt.show()
                 



            def p55_3():

                conn=sql.connect("project.db")
                c=conn.cursor()
                with conn:

                    c.execute("select * from Ward25")
                    df2=c.fetchall()
                    df2=pd.DataFrame(df2,columns=["Ward No","No of Patients",".    |Floor"])
                    df2.plot.line(x="Ward No",y="No of Patients",title="BAR GRAPH",xlabel="Ward No",ylabel="No of Patients")
                    plt.show()
                
                    

            def p5_4():
                conn2=sql.connect("project2.db")
                c0=conn2.cursor()
                with conn2:

                    c0.execute("select * from patient3")
                    df3=c0.fetchall()
                    df3=pd.DataFrame(df3,columns=["Srno","FName","PName","Ph_No","Sex","Age"])
                    df3.plot.bar(x="Srno",y="Age",rot=0,title="BAR GRAPH",xlabel="Srno",ylabel="Age",color="red")
                    plt.show()


            def p5_5():
                conn2=sql.connect("project2.db")
                c0=conn2.cursor()
                with conn2:

                    c0.execute("select * from patient3")
                    df3=c0.fetchall()
                    df3=pd.DataFrame(df3,columns=["Srno","FName","PName","Ph_No","Sex","Age"])
                    df3.plot.pie(x="Srno",y="Age",title="PIE CHART")
                    plt.show()



            def p5_6():
                conn2=sql.connect("project2.db")
                c0=conn2.cursor()
                with conn2:

                    c0.execute("select * from patient3")
                    df3=c0.fetchall()
                    df3=pd.DataFrame(df3,columns=["Srno","FName","PName","Ph_No","Sex","Age"])
                    df3.plot.hist(bins=len(df3.index),x="Srno",y="Age",title="Histogram")
                    plt.show()


            def p5_7():
                conn2=sql.connect("project2.db")
                c0=conn2.cursor()
                with conn2:

                    c0.execute("select * from patient3")
                    df3=c0.fetchall()
                    df3=pd.DataFrame(df3,columns=["Srno","FName","PName","Ph_No","Sex","Age"])
                    df3.plot.line(x="Srno",y="Age",title="PIE CHART",color="red",xlabel="Srno",ylabel="Age")
                    plt.show()



            def p5_8():
                conn=sql.connect("project.db")
                c=conn.cursor()
                with conn:

                    c.execute("select * from doctors")
                    dfr2=c.fetchall()
                    dfr2=pd.DataFrame(dfr2,columns=["Srno","DName","FName","Age","Sex","Qualification","Experience"])
                    dfr2.plot.bar(x="DName",y="Experience",rot=0,title="BAR GRAPH",xlabel="DName",ylabel="Experience",color="red")
                    plt.show()

            def p5_9():
                conn=sql.connect("project.db")
                c=conn.cursor()
                with conn:

                    c.execute("select * from doctors")
                    dfr2=c.fetchall()
                    dfr2=pd.DataFrame(dfr2,columns=["Srno","DName","FName","Age","Sex","Qualification","Experience"])
                    dfr2.plot.pie(x="DName",y="Experience",title="PIE GRAPH")
                    plt.show()

            f5_1=Frame(rootp5,bg="blue")
            Label(f5_1,text="--Statistics--",bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(fill=X,pady=6)
            f5_1.pack(side=TOP,fill=X)
            f5_2=Frame(rootp5,bg="blue")
            Label(f5_2,text="Wards (Ward No. V/S No. of Patients)",bg="grey",fg="black",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f5_2.pack(side=TOP,fill=X)


            f5_5=Frame(rootp5,bg="blue")
            Button(f5_5,text="Bar Graph",command=p55_1,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            Button(f5_5,text="Pie Chart",command=p55_2,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            Button(f5_5,text="Line Graph",command=p55_3,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            f5_5.pack(fill=X)

            f5_6=Frame(rootp5,bg="blue")
            Label(f5_6,text="Patient Records(Age V/S No. of Patients) ",bg="grey",fg="black",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(side=LEFT,anchor="w",pady=6)
            f5_6.pack(fill=X)



            f5_9=Frame(rootp5,bg="blue")
            Button(f5_9,text="Bar Graph",command=p5_4,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            Button(f5_9,text="Pie Chart",command=p5_5,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            Button(f5_9,text="Histogram",command=p5_6,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            Button(f5_9,text="Line Graph",command=p5_7,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            f5_9.pack(fill=X)


            f5_10=Frame(rootp5,bg="blue")
            Label(f5_10,text="Doctors Record(DName V/S Expeience)",bg="grey",fg="black",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT,anchor="w")
            f5_10.pack(fill=X)


            f5_13=Frame(rootp5,bg="blue")
            Button(f5_13,text="Bar Graph",command=p5_8,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            Button(f5_13,text="Pie Chart",command=p5_9,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=6,side=LEFT)
            f5_13.pack(fill=X)


            f5_14=Frame(rootp5,bg="blue")
            Button(f5_14,text="Click to go to previous page",command=rootp5.destroy,bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).pack(pady=140)
            f5_14.pack(fill=X)
            


            rootp5.mainloop()
        def alpha():
            root2.destroy()
            root.destroy()


        b1=Button(f1,text="Add new record",command=pg1,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=10,pady=5)
        b2=Button(f1,text="Update record",command=pg2,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=20,pady=5)
        b3=Button(f1,text="Delete record",command=pg3,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=25,pady=5)
        b4=Button(f1,text="Display",command=pg4,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=55,pady=5)
        b5=Button(f1,text="Stastics",command=pg5,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=50,pady=5)
        b6=Button(f1,text="Exit",command=alpha,bg="grey",fg="black",font="lucida 20 bold",borderwidth=10,relief=SUNKEN,padx=80,pady=5)

        f1.pack(side=TOP,fill=X)
        a1.pack(side=TOP,fill=X,pady=5)
        a2.pack(side=TOP,pady=5)
        b1.pack(side=TOP,anchor="nw",pady=5)
        b2.pack(side=TOP,anchor="nw",pady=5)
        b3.pack(side=TOP,anchor="nw",pady=5)
        b4.pack(side=TOP,anchor="nw",pady=5)
        b5.pack(side=TOP,anchor="nw",pady=5)
        b6.pack(side=TOP,anchor="nw",pady=5)

        a4=Label(f1,text="Thanku for choosing us:              Helpline no.= 0110 0211 2218",bg="red",fg="white",font="lucida 12 bold",borderwidth=10,relief=SUNKEN)
        a4.pack(fill=X,pady=30)
        












    
    else:
        tmsg.askretrycancel("Wrong passward","Try Again")


a=Label(f1,text="WELCOME TO OUR SOFTWARE",bg="red",fg="white",font="sansns 20 bold",borderwidth=5,relief=SUNKEN,padx=10).grid(row=1,column=1)
photo=PhotoImage(file="username.png")
Label(f1,image=photo,pady=10).grid(row=2,column=1)
Label(f1,text="Username",bg="black",fg="white",font="sansns 15 bold",borderwidth=5,relief=SUNKEN).grid(row=3,column=1)
Label(f1,text="Passward",bg="black",fg="white",font="sansns 15 bold",borderwidth=5,relief=SUNKEN).grid(row=5,column=1)
photo1=PhotoImage(file="passward.png")
Label(f1,image=photo1).grid(row=4,column=1)



userentry=StringVar()
passentry=StringVar()


Entry(f1,textvariable=userentry,bg="white",fg="black",font="sansns 15 bold",borderwidth=5,relief=SUNKEN).grid(row=3,column=2)
Entry(f1,textvariable=passentry,bg="white",fg="black",font="sansns 15 bold",borderwidth=5,relief=SUNKEN).grid(row=5,column=2)


Button(f1,text="Submit",command=getvalsm,bg="red",fg="white",font="sansns 15 bold",borderwidth=5,relief=SUNKEN,padx=10,pady=5).grid(pady=10,row=6,column=1)


a1=Label(f2,text=""".......................................MADE BY......................................... 
                1)RAJAT RAJ
                2)CHEHAK SALUJA
                3)NAINA SINGH
                4)UMAR ABDULLAH
                    
                    """,bg="red",fg="white",font="sansns 12 bold",borderwidth=10,relief=SUNKEN)
a1.pack(side=TOP,fill=X)

root.mainloop()

