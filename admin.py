from sqlite3 import *
from tkinter import *
def getrecords(m):
    m.destroy()
    c=connect("inr.db")
    cur=c.cursor()
    x=cur.execute("select * from feedback")
    y=0
    t=0
    for i in x:
        n=i[:-1]
        n=n[1:]
        y+=sum(n)
        t+=1
    avg=y/t
    avg=avg/13
    avg=(avg/5)*100
    scr=Tk()
    img=PhotoImage(file="railways.png")
    l=Label(scr,image=img)
    l.place(x=0,y=0)
    l1=Label(scr,text="Welcome to Admin Portal ",font=("times",30,"bold"))
    l1.place(x=500,y=30)
    l2=Label(scr,text="Average",font=("times",30,"bold"))
    l2.place(x=500,y=300)
    l3=Label(scr,text="%f"%avg,font=("times",30,"bold"))
    l3.place(x=700,y=300)
    
    scr.mainloop()
    
def delrecords():
    c=connect("inr.db")
    cur=c.cursor()
    x=cur.execute("truncate table feedback")
    cur.commit()
def task():
    scr=Tk()
    img=PhotoImage(file="railways.png")
    l=Label(scr,image=img)
    l.place(x=0,y=0)
    l1=Label(scr,text="Welcome to Admin Portal ",font=("times",30,"bold"))
    l1.place(x=500,y=30)
    b=Button(scr,text="Click here to get records",font=("times",30,"bold"),command=lambda :getrecords(scr))
    b.place(x=500,y=300)
    b1=Button(scr,text="Click here to reset records",font=("times",30,"bold"),command=delrecords)
    b1.place(x=500,y=500)
    scr.mainloop()
task()
