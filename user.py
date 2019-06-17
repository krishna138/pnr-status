from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from twilio.rest import Client
import random,re
global var
def msg(a,b,c,d,x,y):
    x=re.search(r'\d+',x)
    if x!=None:
        x=x.string
    else:
        x=''
    d=re.search(r'\S+@\w+[.]\w{2,3}',d)
    if d==None:
        messagebox.showinfo("INR","Enter A valid email")
    try:
        if(len(x)!=10):
            messagebox.showinfo("INR","Enter A Valid Mobile Number")
        y.destroy()
    except:
        pass
    if len(x)==10:
        otp=random.randint(1000,9999)
        account_sid = "AC202680080586a621aa22f8c185335a6c"
        auth_token = "30618cde6069ba63cbb873b33930aa29"
        client = Client(account_sid, auth_token)
        client.messages.create(to="+91"+x,from_="+18653442353",body="Welcome to Indian Northen Railway your otp is %d"%otp)
        scr=Tk(className="Railway Feedback Form")
        f=Frame(scr)
        f.pack(fill=BOTH,expand=1)
        l=Label(f,text="Enter A Valid MOBILE NUMBER",font=("times",20,"bold"))
        l.pack(fill=X,side=TOP)
        e=Entry(f,font=("times",18))
        e.pack()
        e.insert(0,x)
        l1=Label(f,text="Enter otp",font=("times",20,"bold"))
        l1.pack(fill=X,side=TOP)
        e1=Entry(f,font=("times",18))
        e1.pack()
        b=Button(f,text="Submit",font=("times",20,"bold"),command=lambda :valid(e.get(),otp,e1.get(),scr))
        b1=Button(f,text="Resend otp",font=("times",20,"bold"),command=lambda :msg(e.get(),scr))
        b.pack()
        b1.pack()
        scr.mainloop()
    else:
        home()
        

def valid(x,a,b,y):
    global var
    if(len(x)!=10):
        messagebox.showinfo("INR","Enter A Valid Mobile Number")
    y.destroy()
    if (len(x)!=10)and(str(a)!=b):
        home()
    if len(x)==10 and (str(a)==b):
        var=x
        forms()
def home():
    scr1=Tk(className="Railway Feedback Form")
    f=Frame(scr1)
    f.pack(fill=BOTH,expand=1)
    l=Label(f,text="Passenger Name",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    ep=Entry(f,font=("times",18))
    ep.pack()
    l=Label(f,text="City",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    ec=Entry(f,font=("times",18))
    ec.pack()
    l=Label(f,text="State",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    es=Entry(f,font=("times",18))
    es.pack()
    l=Label(f,text="E-Mail ID",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    ee=Entry(f,font=("times",18))
    ee.pack()
##    def print_var(*_):
##        print(option.get())
##    v = IntVar()
##    l=Label(f,text="Gender",font=("times",20,"bold"))
##    l.pack(fill=X,side=TOP)
##    R1=Radiobutton(text="Male", variable=v, value=1).pack(anchor=W)
##    R2=Radiobutton(text="Female", variable=v, value=2).pack(anchor=W)
    l=Label(f,text="Enter A Valid MOBILE NUMBER",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    em=Entry(f,font=("times",18))
    em.pack()
    b=Button(f,text="Submit",font=("times",20,"bold"),command=lambda :msg(ep.get(),ec.get(),es.get(),ee.get(),em.get(),scr1))
    b.pack()
    scr1.mainloop()
def addrecord(x,*a):
    global var
    x.destroy()
    con=connect("inr.db")
    cur=con.cursor()
    try:
        cur.execute("create table feedback(pnr int not null UNIQUE,tw int,tf int,tm int,twb int,smell int,smellmos int,cc int,cd int,cv int,ca int,cvf int,bw int,hyg int,stais varchar(5))")
    except:
        pass
    cur.execute("insert into feedback values({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},'{14}')".format(int(var),*list(map(int,a[:-1])),a[-1]))
    con.commit()
    con.close()
    
def forms():
    scr=Tk(className="Railway Feedback Form")
    img=PhotoImage(file="")
    l=Label(scr,image=img)
    l.place(x=0,y=0)
    display=Label(scr,text="Toilet washing".ljust(100),fg="black", bg="aqua",font=("times",20,"bold"))
    display.grid(row=0,column=0)
    v=IntVar()
    opt1=OptionMenu(scr,v,1,2,3,4,5)
    opt1.grid(row=0,column=1)

    display1=Label(scr,text="Toilet floor drying".ljust(98),fg="black",bg="aqua",font=("times",20,"bold"))
    display1.grid(row=1,column=0)
    v1=IntVar()
    opt2=OptionMenu(scr,v1,1,2,3,4,5)
    opt2.grid(row=1,column=1)

    display2=Label(scr,text="Toilet mirror cleaning".ljust(95),fg="black",bg="aqua",font=("times",20,"bold"))
    display2.grid(row=2,column=0)
    v2=IntVar()
    opt3=OptionMenu(scr,v2,1,2,3,4,5)
    opt3.grid(row=2,column=1)

    display3=Label(scr,text="Toilet wash basin cleanng".ljust(92),fg="black",bg="aqua",font=("times",20,"bold"))
    display3.grid(row=3,column=0)
    v3=IntVar()
    opt4=OptionMenu(scr,v3,1,2,3,4,5)
    opt4.grid(row=3,column=1)

    display4=Label(scr,text="Smell of deodorant spray".ljust(91),fg="black",bg="aqua",font=("times",20,"bold"))
    display4.grid(row=4,column=0)
    v4=IntVar()
    opt5=OptionMenu(scr,v4,1,2,3,4,5)
    opt5.grid(row=4,column=1)

    display5=Label(scr,text="Smell of mosquito repellent spray".ljust(86),fg="black",bg="aqua",font=("times",20,"bold"))
    display5.grid(row=5,column=0)
    v5=IntVar()
    opt6=OptionMenu(scr,v5,1,2,3,4,5)
    opt6.grid(row=5,column=1)

    display0=Label(scr,text="Cleaning of coach aisle area with mopper".ljust(80),fg="black",bg="aqua",font=("times",20,"bold"))
    display0.grid(row=6,column=0)
    v6=IntVar()
    opt7=OptionMenu(scr,v6,1,2,3,4,5)
    opt7.grid(row=6,column=1)

    display7=Label(scr,text="Cleaning of door area".ljust(94),fg="black",bg="aqua",font=("times",20,"bold"))
    display7.grid(row=7,column=0)
    v7=IntVar()
    opt8=OptionMenu(scr,v7,1,2,3,4,5)
    opt8.grid(row=7,column=1)

    display8=Label(scr,text="Cleaning of vestibule area".ljust(92),fg="black",bg="aqua",font=("times",20,"bold"))
    display8.grid(row=8,column=0)
    v8=IntVar()
    opt9=OptionMenu(scr,v8,1,2,3,4,5)
    opt9.grid(row=8,column=1)

    display9=Label(scr,text="Cleaning of ac window glasses".ljust(88),fg="black",bg="aqua",font=("times",20,"bold"))
    display9.grid(row=9,column=0)
    v9=IntVar()
    opt10=OptionMenu(scr,v9,1,2,3,4,5)
    opt10.grid(row=9,column=1)

    display10=Label(scr,text="Cleaning of dustbin from ac coach".ljust(85),fg="black",bg="aqua",font=("times",20,"bold"))
    display10.grid(row=10,column=0)
    v10=IntVar()
    opt11=OptionMenu(scr,v10,1,2,3,4,5)
    opt11.grid(row=10,column=1)

    display11=Label(scr,text="Behaviour of worker".ljust(93),fg="black",bg="aqua",font=("times",20,"bold"))
    display11.grid(row=11,column=0)
    v11=IntVar()
    opt12=OptionMenu(scr,v11,1,2,3,4,5)
    opt12.grid(row=11,column=1)

    display12=Label(scr,text="Hygiene and cleanless of worker uniform".ljust(80),fg="black",bg="aqua",font=("times",20,"bold"))
    display12.grid(row=12,column=0)
    v12=IntVar()
    opt13=OptionMenu(scr,v12,1,2,3,4,5)
    opt13.grid(row=12,column=1)


    display13=Label(scr,text="Over all are you satisfied".ljust(94),fg="black",bg="aqua",font=("times",20,"bold"))
    display13.grid(row=13,column=0)
    v13=StringVar()
    opt14=OptionMenu(scr,v13,"Yes","No")
    opt14.grid(row=13,column=1)
    b=Button(scr,text="Submit",command=lambda :addrecord(scr,v.get(),v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get(),v11.get(),v12.get(),v13.get()),fg="black",font=("times",25,"bold"))
    b.grid(row=14,column=1)
home()
