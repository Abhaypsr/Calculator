import math
import cal as c
import comp as co
import matrix as mat
n=int()
from tkinter import*
win=Tk()
win.geometry("1350x700+0+0")
win.resizable(width=False,height=False)
win.title("APSR(python 3.6)")
def func():
    print("hii")
def changecolor():
    home1.config(bg="GRAY",fg="WHITE")
    calframe1.config(bg="GRAY",fg="WHITE")
a=StringVar()

""" design frames"""
b=""
ans=StringVar()
f1=Frame(win,highlightbackground="GHOSTWHITE",highlightcolor="GHOSTWHITE",highlightthickness=1,bg="WHITE",width=1350,height=65)
f1.pack(side=TOP)
f1.pack_propagate(False)
def home():
    for child in cf.winfo_children():
            child.destroy()
    changecolor()
    home1.config(bg="white",fg="GRAY")
    Label(cf,text="Success").pack()
def game():
     pass    
def calframe():
    for child in cf.winfo_children():
            child.destroy()
    changecolor()
    calframe1.config(bg="WHITE",fg="GRAY")
    def ccolor():
        b1.config(fg="WHITE",bg="GRAY")
        b2.config(fg="WHITE",bg="GRAY")
        b3.config(fg="WHITE",bg="GRAY")
        b4.config(fg="WHITE",bg="GRAY")
        b5.config(fg="WHITE",bg="GRAY")
        b6.config(fg="WHITE",bg="GRAY")
        b7.config(fg="WHITE",bg="GRAY")
        b8.config(fg="WHITE",bg="GRAY")
    def calentry():
        for child in f3.winfo_children():
            child.destroy()
        ccolor()
        b1.config(fg="GRAY",bg="WHITE")
        def ps():
            global b
            s=text.get("1.0","end-1c")
            b=c.cal1(s)
#            if b==int('0'):
#                print("Not valid")
            ans.set(str(b))
        Label(f3,text="     ",bg="GRAY").pack()
        Label(f3,text="     ",bg="GRAY").pack()
        Label(f3,text="     ",bg="GRAY").pack()
        Label(f3,text="     ",bg="GRAY").pack()
        text=Text(f3,width=30,height=1,font=('arial',16,'bold'),bd=8)
        text.pack(side=TOP)
        Label(f3,text="     ",bg="GRAY").pack()
        Button(f3,text="Calculate",command=ps,bg="GRAY",fg="WHITE",width=15,height=1,bd=8).pack()
        Label(f3,text="     ",bg="GRAY").pack()
        Label(f3,text="     ",bg="GRAY").pack()
        Entry(f3,textvariable=ans,font=('arial',16,'bold'),bd=8,state=DISABLED,width=8).pack()


#-----------------------------------complex number-----------------------------------------------------------------
    def complex1():
        ccolor()
        b2.config(fg="GRAY",bg="WHITE")
        a1v=StringVar()
        b1v=StringVar()
        c1v=StringVar()
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var=IntVar()
        va1=IntVar()
        va2=IntVar()
        va3=IntVar()
        va4=IntVar()
        va5=IntVar()
        va6=IntVar()
        va7=IntVar()
        va8=IntVar()
        va9=IntVar()
        va10=IntVar()
        va11=IntVar()
        va12=IntVar()
        va13=IntVar()
        va14=IntVar()
        va15=IntVar()
        va16=IntVar()
        for child in f3.winfo_children():
            child.destroy()
        def reset():
            va1.set(0)
            va2.set(0)
            va3.set(0)
            va4.set(0)
            va5.set(0)
            va6.set(0)
            va7.set(0)
            va8.set(0)
            va9.set(0)
            va10.set(0)
            va11.set(0)
            va12.set(0)
            va13.set(0)
            va14.set(0)
            va15.set(0)
            va16.set(0)
        reset()
        def check():
            for child in f32.winfo_children():
                child.destroy()
            def func():
                if va1.get()==1:
                    reset()
                    va1.set(1)
                    ans.set(co.modulus(a1v.get()))
                if va2.get()==1:
                    reset()
                    va2.set(1)
                    ans.set(co.argument(a1v.get()))
                if va3.get()==1:
                    reset()
                    va3.set(1)
                    ans.set(co.modulus(b1v.get()))
                if va4.get()==1:
                    reset()
                    va4.set(1)
                    ans.set(co.argument(b1v.get()))
                if va5.get()==1:
                    reset()
                    va5.set(1)
                    ans.set(co.modulus(c1v.get()))
                if va6.get()==1:
                    reset()
                    va6.set(1)
                    ans.set(co.argument(c1v.get()))
                if va7.get()==1:
                    reset()
                    va7.set(1)
                    ans.set(co.ab(a1v.get(),b1v.get(),'+'))
                if va8.get()==1:
                    reset()
                    va8.set(1)
                    ans.set(co.ab(a1v.get(),b1v.get(),'-'))
                if va9.get()==1:
                    reset()
                    va9.set(1)
                    ans.set(co.ab(a1v.get(),b1v.get(),'*'))
                if va10.get()==1:
                    reset()
                    va10.set(1)
                    ans.set(co.ab(a1v.get(),b1v.get(),'/'))
                if va11.get()==1:
                    reset()
                    va11.set(1)
                    ans.set(co.abc(a1v.get(),b1v.get(),c1v.get(),'+','+'))
                if va12.get()==1:
                    reset()
                    va12.set(1)
                    ans.set(co.abc(a1v.get(),b1v.get(),c1v.get(),'-','-'))
                if va13.get()==1:
                    reset()
                    va13.set(1)
                    ans.set(co.abc(a1v.get(),b1v.get(),c1v.get(),'+','-'))
                if va14.get()==1:
                    reset()
                    va14.set(1)
                    ans.set(co.abc(a1v.get(),b1v.get(),c1v.get(),'*','*'))
                if va15.get()==1:
                    reset()
                    va15.set(1)
                    ans.set(co.abc(a1v.get(),b1v.get(),c1v.get(),'*','/'))
                if va16.get()==1:
                    reset()
                    va16.set(1)
                    ans.set(co.abc(a1v.get(),b1v.get(),c1v.get(),'/','*'))    
                if va1.get()==1 or va2.get()==1 or va3.get()==1 or va4.get()==1 or va5.get()==1 or va6.get()==1 or va7.get()==1 or va8.get()==1 or va9.get()==1 or va10.get()==1 or va11.get()==1 or va12.get()==1 or va13.get()==1 or va14.get()==1 or va15.get()==1 or va16.get()==1:
                    for child in f33.winfo_children():
                        child.destroy()
                    Label(f33,text="\t\t\tAns :",bg="GRAY").pack(side=LEFT)
                    Entry(f33,textvariable=ans,bd=5,bg="GRAY",fg="WHITE",width=20).pack(side=LEFT)
            if (var1.get()==1):
                a1.configure(state=NORMAL)
                mofa= Checkbutton(f32, text="Modulus of (a)\t\t", bd=11,bg="GRAY",variable=va1,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                aofa= Checkbutton(f32, text="Argumnet of (a)\t\t",bd=11,bg="GRAY", variable=va2,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                mofa.grid(row=0,column=0)
                aofa.grid(row=1,column=0)
            elif (var1.get()==0):
                a1.configure(state=DISABLED)
                mofa.destroy()
            if (var2.get()==1):
                b1.configure(state=NORMAL)
                mofb= Checkbutton(f32, text="Modulus of (b)\t\t", bd=11,bg="GRAY",variable=va3,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                aofb= Checkbutton(f32, text="Argumnet of (b)\t\t",bd=11,bg="GRAY", variable=va4,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                mofb.grid(row=2,column=0)
                aofb.grid(row=3,column=0)
                aofab= Checkbutton(f32, text="a+b\t\t", bd=11,bg="GRAY",variable=va7,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                sofab= Checkbutton(f32, text="a-b\t\t",bd=11,bg="GRAY", variable=va8,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                mofab= Checkbutton(f32, text="a*b\t\t", bd=11,bg="GRAY",variable=va9,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                dofab= Checkbutton(f32, text="a/b\t\t",bd=11,bg="GRAY", variable=va10,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                aofab.grid(row=0,column=1)
                sofab.grid(row=1,column=1)
                mofab.grid(row=2,column=1)
                dofab.grid(row=3,column=1)
            elif (var2.get()==0):
                b1.configure(state=DISABLED)
            if (var3.get()==1):
                if(var2.get()==1):
                    c1.configure(state=NORMAL)
                    mofc= Checkbutton(f32, text="Modulus of (c)\t\t", bd=11,bg="GRAY",variable=va5,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    aofc= Checkbutton(f32, text="Argumnet of (c)\t\t",bd=11,bg="GRAY", variable=va6,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    mofc.grid(row=4,column=0)
                    aofc.grid(row=5,column=0)
                    aofabc= Checkbutton(f32, text="a+b+c",bd=11,bg="GRAY", variable=va11,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    aofabc.grid(row=0,column=3)
                    sofabc1= Checkbutton(f32, text="a-b-c",bd=11,bg="GRAY", variable=va12,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    sofabc1.grid(row=1,column=3)
                    sofabc= Checkbutton(f32, text="a+b-c",bd=11,bg="GRAY", variable=va13,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    sofabc.grid(row=2,column=3)
                    mofabc1= Checkbutton(f32, text="a*b*c",bd=11,bg="GRAY", variable=va14,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    mofabc1.grid(row=3,column=3)
                    mofabc2= Checkbutton(f32, text="(a*b)/c",bd=11,bg="GRAY", variable=va15,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    mofabc2.grid(row=4,column=3)
                    dofabc= Checkbutton(f32, text="a/(b*c)",bd=11,bg="GRAY", variable=va16,font=('arial',12, 'bold'),onvalue = 1, offvalue = 0,command=func)
                    dofabc.grid(row=5,column=3)
            elif (var3.get()==0):
                c1.configure(state=DISABLED)
        f31=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=1,width=960,height=160,bg="GRAY",relief="raise")
        f31.pack(side=TOP)
        f31.pack_propagate(False)
        f32=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,width=960,height=300,bg="GRAY")
        f32.pack(side=TOP)
        f32.pack_propagate(False)
        f33=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=1,width=960,height=160,bg="GRAY")
        f33.pack(side=BOTTOM)
        f33.pack_propagate(False)        
        Label(f31,text="Enter data",font=('arial',30, 'bold'),bg="GRAY",fg="WHITE").pack()
        Label(f31,text="  \t ",bg="GRAY").pack(side=LEFT)
        a = Checkbutton(f31, text="a", variable=var1,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=check)
        a.pack(side=LEFT)
        Label(f31,text="   ",bg="GRAY").pack(side=LEFT)
        a1=Entry(f31,textvariable=a1v,state=DISABLED,width=15,bd=5)
        a1.pack(side=LEFT)
        Label(f31,text="   \t",bg="GRAY").pack(side=LEFT)
        Label(f31,text="   ",bg="GRAY").pack(side=LEFT)
        b = Checkbutton(f31, text="b", variable=var2,font=('arial',18, 'bold'),command=check,onvalue = 1,bg="GRAY", offvalue = 0)
        b.pack(side=LEFT)
        Label(f31,text="   ",bg="GRAY").pack(side=LEFT)
        b1=Entry(f31,textvariable=b1v,state=DISABLED,width=15,bd=5)
        b1.pack(side=LEFT)
        Label(f31,text="   \t",bg="GRAY").pack(side=LEFT)
        Label(f31,text="   ",bg="GRAY").pack(side=LEFT)
        c = Checkbutton(f31, text="c", variable=var3,font=('arial',18, 'bold'),command=check,onvalue = 1,bg="GRAY", offvalue = 0)
        c.pack(side=LEFT)
        Label(f31,text="   ",bg="GRAY").pack(side=LEFT)
        c1=Entry(f31,textvariable=c1v,state=DISABLED,width=15,bd=5)
        c1.pack(side=LEFT)        

#--------------------------------complex finish and Equation start------------------------------------------------------------------        

    def equation():
        ccolor()
        b4.config(fg="GRAY",bg="WHITE")
        for child in f3.winfo_children():
            child.destroy()
        def reset():
            a.set(0)
            b.set(0)
            c.set(0)
            d.set(0)
            e.set(0)
            f.set(0)
            g.set(0)
            h.set(0)
        a=IntVar()
        b=IntVar()
        c=IntVar()
        d=IntVar()
        e=IntVar()
        f=IntVar()
        g=IntVar()
        h=IntVar()
        i=IntVar()
        j=IntVar()
        k=IntVar()
        l=IntVar()
        def quar():
            for child in f321.winfo_children():
                child.destroy()
            for child in f322.winfo_children():
                child.destroy()
            reset()
            def calcu():
                for child in f322.winfo_children():
                    child.destroy()
                a1=a.get()
                b1=b.get()
                c1=c.get()
                d1=d.get()
                if b1*b1-4*a1*c1>=0:
                    q=math.pow(b1*b1-4*a1*c1,1/2)
                    ans=(-b1+q)/(2*a1)
                    Label(f322,text="    \t\t\t\t         ",bg="GRAY").pack(side=LEFT)
                    Label(f322,text="X1 =",bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text=ans,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                    ans=(-b1-q)/(2*a1)
                    Label(f322,text="       &      ",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text="X2 =",bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text=ans,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                else:
                    q=math.pow(0-(b1*b1-4*a1*c1),1/2)
                    ans=-b1/(2*a1)
                    Label(f322,text="      \t\t\t\t       ",bg="GRAY").pack(side=LEFT)
                    Label(f322,text="X1 =",bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text=ans,bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text="+",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    ans=q/(2*a1)
                    Label(f322,text=ans,bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text="i",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text="       &      ",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text="X2 =",bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text=ans,bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text="-",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    ans=q/(2*a1)
                    Label(f322,text=ans,bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    Label(f322,text="i",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                    
            Label(f321,text=" ",bg="GRAY").grid(row=1,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=1)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=2)
            Label(f321,text="QUATRATIC EQUATION-\t",font=('arial',30,'bold'),bg="GRAY",fg="WHITE").grid(row=3,columnspan=30)
            Label(f321,text="   ",bg="GRAY").grid(row=4,columnspan=20)
            Entry(f321,textvariable=a,bd=3,width=3).grid(row=5,column=3)
            Label(f321,text="X^2 +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=5,column=4)
            Entry(f321,textvariable=b,bd=3,width=3).grid(row=5,column=5)
            Label(f321,text="X +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=5,column=6)
            Entry(f321,textvariable=c,bd=3,width=3).grid(row=5,column=7)
            Label(f321,text="=",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=5,column=8)
            Entry(f321,textvariable=d,bd=3,width=3,state=DISABLED,bg="WHITE").grid(row=5,column=9)
            Label(f321,text=" ",bg="GRAY").grid(row=6,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=7,column=0)
            Button(f321,text="Calculate Value",bg="WHITE",bd=2,width=15,command=calcu,fg="powder blue",font=('arial',25)).grid(row=8,columnspan=15)
            Label(f321,text="\n\n\n\n\n",bg="GRAY").grid(row=9,column=5)
            
        def cubic():
            for child in f321.winfo_children():
                child.destroy()
            for child in f322.winfo_children():
                child.destroy()
            reset()
            a1=a.get()
            b1=b.get()
            c1=c.get()
            d1=d.get()
            e1=e.get()
            def calcu():
                for child in f322.winfo_children():
                    child.destroy()
                a1=a.get()
                b1=b.get()
                c1=c.get()
                d1=d.get()
                e1=e.get()
                Label(f322,text="    \t\t  Ans=  ",fg="WHITE",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                for i in range(-15,20):
                    if a1*i*i*i+b1*i*i+c1*i+d1==0:
                        Label(f322,text=" ,",bg="GRAY",fg="WHITE",font=('arial',20,'bold')).pack(side=LEFT)
                        Label(f322,text=i,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                    
            Label(f321,text=" ",bg="GRAY").grid(row=1,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=1)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=2)
            Label(f321,text="CUBIC EQUATION-\t",font=('arial',30,'bold'),bg="GRAY",fg="WHITE").grid(row=3,columnspan=30)
            Label(f321,text="   ",bg="GRAY").grid(row=4,columnspan=20)
            Label(f321,text="   ",bg="GRAY").grid(row=5,columnspan=20)
            Label(f321,text="   ",bg="GRAY").grid(row=6,columnspan=20)
            Entry(f321,textvariable=a,bd=3,width=3).grid(row=7,column=3)
            Label(f321,text="X^3 +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=4)
            Entry(f321,textvariable=b,bd=3,width=3).grid(row=7,column=5)
            Label(f321,text="X^2 +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=6)
            Entry(f321,textvariable=c,bd=3,width=3).grid(row=7,column=7)
            Label(f321,text="X +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=8)
            Entry(f321,textvariable=d,bd=3,width=3,bg="WHITE").grid(row=7,column=9)
            Label(f321,text="=",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=10)
            Entry(f321,textvariable=e,bd=3,width=3,state=DISABLED).grid(row=7,column=11)
            Label(f321,text=" ",bg="GRAY").grid(row=8,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=9,column=0)
            Button(f321,text="Calculate Value",bg="WHITE",bd=2,width=15,command=calcu,fg="powder blue",font=('arial',25)).grid(row=10,columnspan=15)
            Label(f321,text="\n\n\n\n\n",bg="GRAY").grid(row=11,column=5)
        def onev():
            for child in f321.winfo_children():
                child.destroy()
            for child in f322.winfo_children():
                child.destroy()
            reset()
            def calcu():
                for child in f322.winfo_children():
                    child.destroy()
                a1=a.get()
                b1=b.get()
                ans=-b1/a1
                Label(f322,text="    \t\t  X =  ",fg="WHITE",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                Label(f322,text=ans,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
            Label(f321,text=" ",bg="GRAY").grid(row=0,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=1,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=0)
            Label(f321,text="One Variable Equation-",bg="GRAY",fg="WHITE",font=('arial',30)).grid(row=3,columnspan=20)
            Entry(f321,textvariable=a,bd=3,width=3).grid(row=4,column=0)
            Label(f321,text="X+",bg="GRAY",fg="WHITE",font=('arial',20)).grid(row=4,column=1)
            Entry(f321,textvariable=b,bd=3,width=3).grid(row=4,column=2)
            Label(f321,text="= 0",bg="GRAY",fg="WHITE",font=('arial',20)).grid(row=4,column=3)
            Label(f321,text=" ",bg="GRAY").grid(row=5,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=6,column=0)
            Button(f321,text="Calculate",bg="WHITE",bd=2,width=10,command=calcu,fg="powder blue",font=('arial',30)).grid(row=7,columnspan=10)
        def twov():
            for child in f321.winfo_children():
                child.destroy()
            for child in f322.winfo_children():
                child.destroy()
            reset()
            def calcu():
                for child in f322.winfo_children():
                    child.destroy()
                a1=a.get()
                b1=b.get()
                c1=c.get()
                a2=d.get()
                b2=e.get()
                c2=f.get()
                if a1*b2-a2*b1==0:
                    print('Error')
                    return
                else:
                    x=(c1*b2-c2*b1)/(a1*b2-a2*b1);
                    y=(a1*c2-a2*c1)/(a1*b2-a2*b1);
                Label(f322,text="\t X =  ",fg="WHITE",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                Label(f322,text=x,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                Label(f322,text="      Y =  ",fg="WHITE",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                Label(f322,text=y,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)

            Label(f321,text=" ",bg="GRAY").grid(row=1,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=1)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=2)
            Label(f321,text="Two Variable Equation-\t",font=('arial',30,'bold'),bg="GRAY",fg="WHITE").grid(row=3,columnspan=30)
            Label(f321,text="   ",bg="GRAY").grid(row=4,columnspan=25)
            Label(f321,text="   ",bg="GRAY").grid(row=5,columnspan=25)
            Label(f321,text="   ",bg="GRAY").grid(row=6,columnspan=25)
            Entry(f321,textvariable=a,bd=3,width=3).grid(row=7,column=3)
            Label(f321,text="X +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=4)
            Entry(f321,textvariable=b,bd=3,width=3).grid(row=7,column=5)
            Label(f321,text="Y =",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=6)
            Entry(f321,textvariable=c,bd=3,width=3,bg="WHITE").grid(row=7,column=7)
            Label(f321,text=" ",bg="GRAY").grid(row=8,column=2)
            Entry(f321,textvariable=d,bd=3,width=3).grid(row=9,column=3)
            Label(f321,text="X +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=9,column=4)
            Entry(f321,textvariable=e,bd=3,width=3).grid(row=9,column=5)
            Label(f321,text="Y =",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=9,column=6)
            Entry(f321,textvariable=f,bd=3,width=3,bg="WHITE").grid(row=9,column=7)
            Label(f321,text=" ",bg="GRAY").grid(row=10,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=11,column=0)
            Button(f321,text="Calculate",bg="WHITE",bd=2,width=10,fg="powder blue",font=('arial',25),command=calcu).grid(row=12,columnspan=10)
        def threev():
            for child in f321.winfo_children():
                child.destroy()
            for child in f322.winfo_children():
                child.destroy()
            reset()
            def calcu():
                for child in f322.winfo_children():
                    child.destroy()
                a1=a.get()
                b1=b.get()
                c1=c.get()
                d1=d.get()
                a2=e.get()
                b2=f.get()
                c2=g.get()
                d2=h.get()
                a3=i.get()
                b3=j.get()
                c3=k.get()
                d3=l.get()
                if (a1*b2-a2*b1)*(c2*b3-c3*b2)-(c1*b2-b1*c2)*(a2*b3-a3*b2)==0 and (a1*b2-a2*b1)*(a1*c3-c1*a3)-(a1*c2-c1*a2)*(a1*b3-a3*b1)==0:
                    print("Error")
                    return
                else:
                    x=((d1*b2-d2*b1)*(c2*b3-c3*b2)-(d2*b3-d3*b2)*(c1*b2-b1*c2))/((a1*b2-a2*b1)*(c2*b3-c3*b2)-(c1*b2-b1*c2)*(a2*b3-a3*b2));
                    y=((a1*d2-a2*d1)*(a1*c3-a3*c1)-(a1*d3-a3*d1)*(a1*c2-a2*c1))/((a1*b2-a2*b1)*(a1*c3-c1*a3)-(a1*c2-c1*a2)*(a1*b3-a3*b1));
                    z=((a1*b2-a2*b1)*(a1*d3-d1*a3)-(a1*d2-a2*d1)*(a1*b3-b1*a3))/((a1*b2-b1*a2)*(a1*c3-c1*a3)-(a1*c2-a2*c1)*(a1*b3-b1*a3));
                Label(f322,text="\t X =  ",fg="WHITE",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                Label(f322,text=x,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                Label(f322,text="      Y =  ",fg="WHITE",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                Label(f322,text=y,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
                Label(f322,text="      Z =  ",fg="WHITE",bg="GRAY",font=('arial',20)).pack(side=LEFT)
                Label(f322,text=z,bg="GRAY",fg="WHITE",font=('arial',20)).pack(side=LEFT)
            Label(f321,text=" ",bg="GRAY").grid(row=1,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=1)
            Label(f321,text=" ",bg="GRAY").grid(row=2,column=2)
            Label(f321,text="Three Variable Equation-\t",font=('arial',30,'bold'),bg="GRAY",fg="WHITE").grid(row=3,columnspan=30)
            Label(f321,text="   ",bg="GRAY").grid(row=4,columnspan=25)
            Label(f321,text="   ",bg="GRAY").grid(row=5,columnspan=25)
            Label(f321,text="   ",bg="GRAY").grid(row=6,columnspan=25)
            Entry(f321,textvariable=a,bd=3,width=3).grid(row=7,column=3)
            Label(f321,text="X +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=4)
            Entry(f321,textvariable=b,bd=3,width=3).grid(row=7,column=5)
            Label(f321,text="Y +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=6)
            Entry(f321,textvariable=c,bd=3,width=3,bg="WHITE").grid(row=7,column=7)
            Label(f321,text="Z =",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=7,column=8)
            Entry(f321,textvariable=d,bd=3,width=3,bg="WHITE").grid(row=7,column=9)
            Label(f321,text=" ",bg="GRAY").grid(row=8,column=2)
            Entry(f321,textvariable=e,bd=3,width=3).grid(row=9,column=3)
            Label(f321,text="X +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=9,column=4)
            Entry(f321,textvariable=f,bd=3,width=3).grid(row=9,column=5)
            Label(f321,text="Y +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=9,column=6)
            Entry(f321,textvariable=g,bd=3,width=3,bg="WHITE").grid(row=9,column=7)
            Label(f321,text="Z =",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=9,column=8)
            Entry(f321,textvariable=h,bd=3,width=3,bg="WHITE").grid(row=9,column=9)
            Label(f321,text=" ",bg="GRAY").grid(row=10,column=0)
            Entry(f321,textvariable=i,bd=3,width=3).grid(row=11,column=3)
            Label(f321,text="X +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=11,column=4)
            Entry(f321,textvariable=j,bd=3,width=3).grid(row=11,column=5)
            Label(f321,text="Y +",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=11,column=6)
            Entry(f321,textvariable=k,bd=3,width=3,bg="WHITE").grid(row=11,column=7)
            Label(f321,text="Z =",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=11,column=8)
            Entry(f321,textvariable=l,bd=3,width=3,bg="WHITE").grid(row=11,column=9)
            Label(f321,text=" ",bg="GRAY").grid(row=12,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=13,column=0)
            Button(f321,text="Calculate",bg="WHITE",bd=2,width=10,fg="powder blue",font=('arial',25),command=calcu).grid(row=14,columnspan=10)
            
        f31=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=1,bg="GRAY",height=620,width=200)
        f31.pack(side=LEFT)
        f31.pack_propagate(False)
        f32=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",height=620,width=760)
        f32.pack(side=RIGHT)
        f32.pack_propagate(False)
        f321=Frame(f32,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",height=500,width=760)
        f321.pack(side=TOP)
        f321.pack_propagate(False)
        f322=Frame(f32,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",height=120,width=760)
        f322.pack()
        f322.pack_propagate(False)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="Quardratic Equation",bg="WHITE",fg="GRAY",bd=10,width=20,command=quar).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="Cubic Equation",bg="WHITE",bd=10,fg="GRAY",width=20,command=cubic).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="One Variable Equation",bg="WHITE",bd=10,fg="GRAY",width=20,command=onev).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="Two variable Equation",bg="WHITE",bd=10,fg="GRAY",width=20,command=twov).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="Three Variable Equation",bg="WHITE",bd=10,fg="GRAY",width=20,command=threev).pack(side=TOP)
        

#===============================Equation finish &  matrix start====================================================
    def matrix():
        ccolor()
        b3.config(fg="GRAY",bg="WHITE")
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        r1=IntVar()
        r2=IntVar()
        r3=IntVar()
        c1=IntVar()
        c2=IntVar()
        c3=IntVar()
        a4=IntVar()
        b4=IntVar()
        c4=IntVar()
        d4=IntVar()
        e4=IntVar()
        f4=IntVar()
        g4=IntVar()
        h4=IntVar()
        i4=IntVar()
        j4=IntVar()
        k4=IntVar()
        l4=IntVar()
        m4=IntVar()
        n4=IntVar()
        o4=IntVar()
        p4=IntVar()
        a5=IntVar()
        b5=IntVar()
        c5=IntVar()
        d5=IntVar()
        e5=IntVar()
        f5=IntVar()
        g5=IntVar()
        h5=IntVar()
        i5=IntVar()
        j5=IntVar()
        k5=IntVar()
        l5=IntVar()
        m5=IntVar()
        n5=IntVar()
        o5=IntVar()
        p5=IntVar()
        a6=IntVar()
        b6=IntVar()
        c6=IntVar()
        d6=IntVar()
        e6=IntVar()
        f6=IntVar()
        g6=IntVar()
        h6=IntVar()
        i6=IntVar()                  
        j6=IntVar()
        k6=IntVar()
        l6=IntVar()
        m6=IntVar()
        n6=IntVar()
        o6=IntVar()
        p6=IntVar()
        var=StringVar()
        var4=IntVar()
        for child in f3.winfo_children():
            child.destroy()
        def func1():
            if var1.get()==1:
                a1.configure(state=NORMAL)
                aa1.configure(state=NORMAL)
            if var2.get()==1:
                b1.configure(state=NORMAL)
                bb1.configure(state=NORMAL)
            if var3.get()==1:
                cc1.configure(state=NORMAL)
                cc11.configure(state=NORMAL)
        def makelist(n):
            a=[]
            b=[]
            c=[]
            if n==1:
                o=r1.get()
                se=c1.get()
                if o*se>=1:
                    a.append(a4.get())
                if o*se>=2:
                    a.append(b4.get())
                if o*se>=3:
                    a.append(c4.get())
                if o*se>=4:
                    a.append(d4.get())
                if o*se>=5:
                    a.append(e4.get())
                if o*se>=6:
                    a.append(f4.get())
                if o*se>=7:
                    a.append(g4.get())
                if o*se>=8:
                    a.append(h4.get())
                if o*se>=9:
                    a.append(i4.get())
                if o*se>=10:
                    a.append(j4.get())
                if o*se>=11:
                    a.append(k4.get())
                if o*se>=12:
                    a.append(l4.get())
                if o*se>=13:
                    a.append(m4.get())
                if o*se>=14:
                    a.append(n4.get())
                if o*se>=15:
                    a.append(o4.get())
                if o*se>=16:
                    a.append(p4.get())
                return a
            if n==2:
                o=r2.get()
                se=c2.get()
                if o*se>=1:
                    b.append(a5.get())
                if o*se>=2:
                    b.append(b5.get())
                if o*se>=3:
                    b.append(c5.get())
                if o*se>=4:
                    b.append(d5.get())
                if o*se>=5:
                    b.append(e5.get())
                if o*se>=6:
                    b.append(f5.get())
                if o*se>=7:
                    b.append(g5.get())
                if o*se>=8:
                    b.append(h5.get())
                if o*se>=9:
                    b.append(i5.get())
                if o*se>=10:
                    b.append(j5.get())
                if o*se>=11:
                    b.append(k5.get())
                if o*se>=12:
                    b.append(l5.get())
                if o*se>=13:
                    b.append(m5.get())
                if o*se>=14:
                    b.append(n5.get())
                if o*se>=15:
                    b.append(o5.get())
                if o*se>=16:
                    b.append(p5.get())
                return b
            if n==3:
                o=r3.get()
                se=c3.get()
                if o*se>=1:
                    c.append(a6.get())
                if o*se>=2:
                    c.append(b6.get())
                if o*se>=3:
                    c.append(c6.get())
                if o*se>=4:
                    c.append(d6.get())
                if o*se>=5:
                    c.append(e6.get())
                if o*se>=6:
                    c.append(f6.get())
                if o*se>=7:
                    c.append(g6.get())
                if o*se>=8:
                    c.append(h6.get())
                if o*se>=9:
                    c.append(i6.get())
                if o*se>=10:
                    c.append(j6.get())
                if o*se>=11:
                    c.append(k6.get())
                if o*se>=12:
                    c.append(l6.get())
                if o*se>=13:
                    c.append(m6.get())
                if o*se>=14:
                    c.append(n6.get())
                if o*se>=15:
                    c.append(o6.get())
                if o*se>=16:
                    c.append(p6.get())
                return c
        def printf(n,r,c):
            for child in f33.winfo_children():
                child.destroy()
            k=0
            n=[n]
            s=IntVar()
            Label(f33,text="Ans= ",bg="GRAY").grid(row=0,column=0)
            for i in range(r):
                for j in range(1,c+1):
                    s.set(n[k])
                    Entry(f33,textvariable=s,width=2).grid(row=i,column=j)
                    k=k+1
            Label(f33,text="\n\n",bg="GRAY").grid(row=5,column=1)
        def func2():
            for child in f33.winfo_children():
                child.destroy()
            if var4.get()==1:
                ans=makelist(1)
                ans=mat.determinant(ans,r1.get(),c1.get())
                printf(ans,1,1)
            if var5.get()==1:
                ans=makelist(2)
                ans=mat.determinant(ans,r2.get(),c2.get())
                printf(ans,1,1)
            if var9.get()==1:
                ans=makelist(3)
                ans=mat.determinant(ans,r3.get(),c3.get())
                printf(ans,1,1)
            if var6.get()==1:
                ans1=makelist(1)
                ans2=makelist(2)
                ans=mat.ab(ans1,r1.get(),c1.get(),ans2,r2.get(),c2.get(),'+')
                printf(ans,r1.get(),c1.get())
            if var7.get()==1:
                ans1=makelist(1)
                ans2=makelist(2)
                ans=mat.ab(ans1,r1.get(),c1.get(),ans2,r2.get(),c2.get(),'-')
                printf(ans,r1.get(),c1.get())
            if var8.get()==1:
                ans1=makelist(1)
                ans2=makelist(2)
                ans=mat.ab(ans1,r1.get(),c1.get(),ans2,r2.get(),c2.get(),'*')
                printf(ans,r1.get(),c2.get())
            if var10.get()==1:
                ans1=makelist(1)
                ans2=makelist(2)
                ans3=makelist(3)
                ans=mat.ab(ans1,r1.get(),c1.get(),ans2,r2.get(),c2.get(),'+')
                ans=mat.ab(ans,r1.get(),c1.get(),ans3,r3.get(),c3.get(),'+')
                printf(ans,r1.get(),c3.get())
            if var11.get()==1:
                ans1=makelist(1)
                ans2=makelist(2)
                ans3=makelist(3)
                ans=mat.ab(ans1,r1.get(),c1.get(),ans2,r2.get(),c2.get(),'*')
                ans=mat.ab(ans,r1.get(),c2.get(),ans3,r3.get(),c3.get(),'*')
                printf(ans,r1.get(),c3.get())
        def check():
            for child in f321.winfo_children():
                child.destroy()
            for child in f322.winfo_children():
                child.destroy()
            if var1.get()==1:
                i='1'
                j='1'
                s='a'
                k=0
                
                for i in range(1,r1.get()+1):
                    for j in range(1,c1.get()+1):
                        p=str(i)
                        q=str(j)
#                        s=s+p+q
                        Label(f321,text=s+p+q,bg="GRAY",width=5).grid(row=k,column=0)
                        Label(f321,text="=",bg="GRAY").grid(row=k,column=1)
                        k=k+1
                        s='a'
                o=r1.get()
                se=c1.get()
                if o*se>=1:
                    Entry(f321,textvariable=a4,width=5,bd=3).grid(row=0,column=2)
                if o*se>=2:
                    Entry(f321,textvariable=b4,width=5,bd=3).grid(row=1,column=2)
                if o*se>=3:
                    Entry(f321,textvariable=c4,width=5,bd=3).grid(row=2,column=2)
                if o*se>=4:
                    Entry(f321,textvariable=d4,width=5,bd=3).grid(row=3,column=2)
                if o*se>=5:
                    Entry(f321,textvariable=e4,width=5,bd=3).grid(row=4,column=2)
                if o*se>=6:
                    Entry(f321,textvariable=f4,width=5,bd=3).grid(row=5,column=2)
                if o*se>=7:
                    Entry(f321,textvariable=g4,width=5,bd=3).grid(row=6,column=2)
                if o*se>=8:
                    Entry(f321,textvariable=h4,width=5,bd=3).grid(row=7,column=2)
                if o*se>=9:
                    Entry(f321,textvariable=i4,width=5,bd=3).grid(row=8,column=2)
                if o*se>=10:
                    Entry(f321,textvariable=j4,width=5,bd=3).grid(row=9,column=2)
                if o*se>=11:
                    Entry(f321,textvariable=k4,width=5,bd=3).grid(row=10,column=2)
                if o*se>=12:
                    Entry(f321,textvariable=l4,width=5,bd=3).grid(row=11,column=2)
                if o*se>=13:
                    Entry(f321,textvariable=m4,width=5,bd=3).grid(row=12,column=2)
                if o*se>=14:
                    Entry(f321,textvariable=n4,width=5,bd=3).grid(row=13,column=2)
                if o*se>=15:
                    Entry(f321,textvariable=o4,width=5,bd=3).grid(row=14,column=2)
                if o*se>=16:
                    Entry(f321,textvariable=p4,width=5,bd=3).grid(row=15,column=2)
                Label(f321,text="       ",bg="GRAY").grid(row=1,column=3)
            
            if var2.get()==1:
                i='1'
                j='1'
                s='b'
                k=0
                
                for i in range(1,r2.get()+1):
                    for j in range(1,c2.get()+1):
                        p=str(i)
                        q=str(j)
#                        s=s+p+q
                        Label(f321,text=s+p+q,bg="GRAY",width=5).grid(row=k,column=4)
                        Label(f321,text="=",bg="GRAY").grid(row=k,column=5)
                        k=k+1
                        s='b'
                o=r2.get()
                se=c2.get()
                if o*se>=1:
                    Entry(f321,textvariable=a5,width=5,bd=3).grid(row=0,column=6)
                if o*se>=2:
                    Entry(f321,textvariable=b5,width=5,bd=3).grid(row=1,column=6)
                if o*se>=3:
                    Entry(f321,textvariable=c5,width=5,bd=3).grid(row=2,column=6)
                if o*se>=4:
                    Entry(f321,textvariable=d5,width=5,bd=3).grid(row=3,column=6)
                if o*se>=5:
                    Entry(f321,textvariable=e5,width=5,bd=3).grid(row=4,column=6)
                if o*se>=6:
                    Entry(f321,textvariable=f5,width=5,bd=3).grid(row=5,column=6)
                if o*se>=7:
                    Entry(f321,textvariable=g5,width=5,bd=3).grid(row=6,column=6)
                if o*se>=8:
                    Entry(f321,textvariable=h5,width=5,bd=3).grid(row=7,column=6)
                if o*se>=9:
                    Entry(f321,textvariable=i5,width=5,bd=3).grid(row=8,column=6)
                if o*se>=10:
                    Entry(f321,textvariable=j5,width=5,bd=3).grid(row=9,column=6)
                if o*se>=11:
                    Entry(f321,textvariable=k5,width=5,bd=3).grid(row=10,column=6)
                if o*se>=12:
                    Entry(f321,textvariable=l5,width=5,bd=3).grid(row=11,column=6)
                if o*se>=13:
                    Entry(f321,textvariable=m5,width=5,bd=3).grid(row=12,column=6)
                if o*se>=14:
                    Entry(f321,textvariable=n5,width=5,bd=3).grid(row=13,column=6)
                if o*se>=15:
                    Entry(f321,textvariable=o5,width=5,bd=3).grid(row=14,column=6)
                if o*se>=16:
                    Entry(f321,textvariable=p5,width=5,bd=3).grid(row=15,column=6)
                Label(f321,text="         ",bg="GRAY").grid(row=1,column=7)
                
            if var3.get()==1:
                i='1'
                j='1'
                s='c'
                k=0
                
                for i in range(1,r3.get()+1):
                    for j in range(1,c3.get()+1):
                        p=str(i)
                        q=str(j)
#                        s=s+p+q
                        Label(f321,text=s+p+q,bg="GRAY",width=5).grid(row=k,column=8)
                        Label(f321,text="=",bg="GRAY").grid(row=k,column=9)
                        k=k+1
                        s='c'
                o=r3.get()
                se=c3.get()
                if o*se>=1:
                    Entry(f321,textvariable=a6,width=5,bd=3).grid(row=0,column=10)
                if o*se>=2:
                    Entry(f321,textvariable=b6,width=5,bd=3).grid(row=1,column=10)
                if o*se>=3:
                    Entry(f321,textvariable=c6,width=5,bd=3).grid(row=2,column=10)
                if o*se>=4:
                    Entry(f321,textvariable=d6,width=5,bd=3).grid(row=3,column=10)
                if o*se>=5:
                    Entry(f321,textvariable=e6,width=5,bd=3).grid(row=4,column=10)
                if o*se>=6:
                    Entry(f321,textvariable=f6,width=5,bd=3).grid(row=5,column=10)
                if o*se>=7:
                    Entry(f321,textvariable=g6,width=5,bd=3).grid(row=6,column=10)
                if o*se>=8:
                    Entry(f321,textvariable=h6,width=5,bd=3).grid(row=7,column=10)
                if o*se>=9:
                    Entry(f321,textvariable=i6,width=5,bd=3).grid(row=8,column=10)
                if o*se>=10:
                    Entry(f321,textvariable=j6,width=5,bd=3).grid(row=9,column=10)
                if o*se>=11:
                    Entry(f321,textvariable=k6,width=5,bd=3).grid(row=10,column=10)
                if o*se>=12:
                    Entry(f321,textvariable=l6,width=5,bd=3).grid(row=11,column=10)
                if o*se>=13:
                    Entry(f321,textvariable=m6,width=5,bd=3).grid(row=12,column=10)
                if o*se>=14:
                    Entry(f321,textvariable=n6,width=5,bd=3).grid(row=13,column=10)
                if o*se>=15:
                    Entry(f321,textvariable=o6,width=5,bd=3).grid(row=14,column=10)
                if o*se>=16:
                    Entry(f321,textvariable=p6,width=5,bd=3).grid(row=15,column=10)
            if var1.get()==1:
                f322.configure(highlightthickness=1)
                Checkbutton(f322, text="|A|", variable=var4,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
                if var2.get()==1:
                    Checkbutton(f322, text="|B|", variable=var5,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
                    Checkbutton(f322, text="A+B", variable=var6,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
                    Checkbutton(f322, text="A-B", variable=var7,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
                    Checkbutton(f322, text="A*B", variable=var8,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
                    if var3.get()==1:
                        Checkbutton(f322, text="|C|", variable=var9,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
                        Checkbutton(f322, text="A+B+C", variable=var10,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
                        Checkbutton(f322, text="A*B*C", variable=var11,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func2).pack(side=TOP)
        f31=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,width=960,height=100,bg="GRAY",relief="raise")
        f31.pack(side=TOP)
        f31.pack_propagate(False)
        f32=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,width=960,height=360,bg="GRAY")
        f32.pack(side=TOP)
        f32.pack_propagate(False)
        f321=Frame(f32,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,width=660,height=360,bg="GRAY")
        f321.pack(side=LEFT)
        f321.pack_propagate(False)
        f322=Frame(f32,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,width=300,height=360,bg="GRAY")
        f322.pack(side=RIGHT)
        f322.pack_propagate(False)
        f33=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,width=960,height=160,bg="GRAY")
        f33.pack(side=BOTTOM)
        f33.pack_propagate(False)        
        a = Checkbutton(f31, text="Order of A:", variable=var1,font=('arial',18, 'bold'),onvalue = 1,bg="GRAY", offvalue = 0,command=func1)
        a.pack(side=LEFT)
        a1=Entry(f31,textvariable=r1,state=DISABLED,width=5,bd=2)
        a1.pack(side=LEFT)
        aa1=Entry(f31,textvariable=c1,state=DISABLED,width=5,bd=2)
        aa1.pack(side=LEFT)
        Label(f31,text="   \t",bg="GRAY").pack(side=LEFT)
        Label(f31,text="   ",bg="GRAY").pack(side=LEFT)
        b = Checkbutton(f31, text="Order of B:", variable=var2,font=('arial',18, 'bold'),command=func1,onvalue = 1,bg="GRAY", offvalue = 0)
        b.pack(side=LEFT)
        b1=Entry(f31,textvariable=r2,state=DISABLED,width=5,bd=2)
        b1.pack(side=LEFT)
        bb1=Entry(f31,textvariable=c2,state=DISABLED,width=5,bd=2)
        bb1.pack(side=LEFT)
        Label(f31,text="   \t",bg="GRAY").pack(side=LEFT)
        Label(f31,text="   ",bg="GRAY").pack(side=LEFT)
        c = Checkbutton(f31, text="Order of C:", variable=var3,font=('arial',18, 'bold'),command=func1,onvalue = 1,bg="GRAY", offvalue = 0)
        c.pack(side=LEFT)
        
        cc1=Entry(f31,textvariable=r3,state=DISABLED,width=5,bd=2)
        cc1.pack(side=LEFT) 
        cc11=Entry(f31,textvariable=c3,state=DISABLED,width=5,bd=2)
        cc11.pack(side=LEFT)
        Button(f31,text="Click",command=check).pack()
#-------------------------------matrix finish  &  trignometry start-------------------------------------------------------------------------------------
    
    def trigno():
        ccolor()
        b5.config(fg="GRAY",bg="WHITE")
        for child in f3.winfo_children():
            child.destroy()
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        sinv=IntVar()
        cosv=IntVar()
        tanv=IntVar()
        cosecv=IntVar()
        secv=IntVar()
        cotv=IntVar()
        sina=IntVar()
        cosa=IntVar()
        tana=IntVar()
        coseca=IntVar()
        seca=IntVar()
        cota=IntVar()
        asina=IntVar()
        acosa=IntVar()
        atana=IntVar()
        asinv=IntVar()
        acosv=IntVar()
        atanv=IntVar()
        def trigno1():
            if var1.get()==1:
                sin1.configure(state=NORMAL)
            if var2.get()==1:
                cos1.configure(state=NORMAL)
            if var3.get()==1:
                tan1.configure(state=NORMAL)
            if var4.get()==1:
                cosec1.configure(state=NORMAL)
            if var5.get()==1:
                sec1.configure(stae=NORMAL)
            if var6.get()==1:
                cot1.configure(state=NORMAL)
            if var7.get()==1:
                asin1.configure(state=NORMAL)
            if var8.get()==1:
                acos1.configure(state=NORMAL)
            if var9.get()==1:
                atan1.configure(state=NORMAL)
        def func():
            if var1.get()==1:
                x=sinv.get()
                x=x*3.14/180
                x=(math.sin(x))
                sina.set(x)
            if var2.get()==1:
                x=cosv.get()
                x=x*3.14/180
                x=(math.cos(x))
                cosa.set(x)
            if var3.get()==1:
                x=tanv.get()
                x=x*3.14/180
                x=(math.tan(x))
                tana.set(x)
            if var4.get()==1:
                x=cosecv.get()
                x=x*3.14/180
                x=(math.sin(x))
                if x==0:
                    return
                coseca.set(1/x)
            if var5.get()==1:
                x=secv.get()
                x=x*3.14/180
                x=(math.cos(x))
                if x==0:
                    return
                seca.set(1/x)
            if var6.get()==1:
                x=cotv.get()
                x=x*3.14/180
                x=(math.tan(x))
                if x==0:
                    return
                cota.set(1/x)
            if var7.get()==1:
                x=asinv.get()
                x=x*3.14/180
                x=math.asin(x)
                asina.set(x)
            if var8.get()==1:
                x=acosv.get()
                x=x*3.14/180
                x=math.acos(x)
                acosa.set(x)
            if var9.get()==1:
                x=atanv.get()
                x=x*3.14/180
                x=math.atan(x)
                atana.set(x)
        f31=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",width=530,height=620)
        f31.pack(side=LEFT)
        f31.pack_propagate(False)
        f32=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",width=430,height=620)
        f32.pack(side=RIGHT)
        f32.pack_propagate(False)
        Label(f31,text="\t\t",bg="GRAY").grid(row=0,column=1)
        sin=Checkbutton(f31, text="Sin", variable=var1,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        sin.grid(row=0,column=2)
        sin1=Entry(f31,textvariable=sinv,width=3,bd=2,state=DISABLED)
        sin1.grid(row=0,column=3)
        Label(f31,text="=",bg="GRAY").grid(row=0,column=4)
        sin2=Entry(f31,textvariable=sina,width=15,bd=4,state=DISABLED)
        sin2.grid(row=0,column=5)
        cos=Checkbutton(f31, text="Cos", variable=var2,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        cos.grid(row=1,column=2)
        cos1=Entry(f31,textvariable=cosv,width=3,bd=2,state=DISABLED)
        cos1.grid(row=1,column=3)
        Label(f31,text="=",bg="GRAY").grid(row=1,column=4)
        cos2=Entry(f31,textvariable=cosa,width=15,bd=4,state=DISABLED)
        cos2.grid(row=1,column=5)
        tan=Checkbutton(f31, text="Tan", variable=var3,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        tan.grid(row=2,column=2)
        tan1=Entry(f31,textvariable=tanv,width=3,bd=2,state=DISABLED)
        tan1.grid(row=2,column=3)
        Label(f31,text="=",bg="GRAY").grid(row=2,column=4)
        tan2=Entry(f31,textvariable=tana,width=15,bd=4,state=DISABLED)
        tan2.grid(row=2,column=5)
        cosec=Checkbutton(f31, text="Cosec", variable=var4,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        cosec.grid(row=3,column=2)
        cosec1=Entry(f31,textvariable=cosecv,width=3,bd=2,state=DISABLED)
        cosec1.grid(row=3,column=3)
        Label(f31,text="=",bg="GRAY").grid(row=3,column=4)
        cosec2=Entry(f31,textvariable=coseca,width=15,bd=4,state=DISABLED)
        cosec2.grid(row=3,column=5)
        sec=Checkbutton(f31, text="Sec", variable=var5,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        sec.grid(row=4,column=2)
        sec1=Entry(f31,textvariable=secv,width=3,bd=2,state=DISABLED)
        sec1.grid(row=4,column=3)
        Label(f31,text="=",bg="GRAY").grid(row=4,column=4)
        sec2=Entry(f31,textvariable=seca,width=15,bd=4,state=DISABLED)
        sec2.grid(row=4,column=5)
        cot=Checkbutton(f31, text="Cot", variable=var6,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        cot.grid(row=5,column=2)
        cot1=Entry(f31,textvariable=cotv,width=3,bd=2,state=DISABLED)
        cot1.grid(row=5,column=3)
        Label(f31,text="=",bg="GRAY").grid(row=5,column=4)
        cot2=Entry(f31,textvariable=cota,width=15,bd=4,state=DISABLED)
        cot2.grid(row=5,column=5)
        
        
        asin=Checkbutton(f32, text="Sin`", variable=var7,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        asin.grid(row=0,column=0)
        asin1=Entry(f32,textvariable=asinv,width=3,bd=2,state=DISABLED)
        asin1.grid(row=0,column=1)
        Label(f32,text="=",bg="GRAY").grid(row=0,column=2)
        asin2=Entry(f32,textvariable=asina,width=15,bd=4,state=DISABLED)
        asin2.grid(row=0,column=3)
        acos=Checkbutton(f32, text="Cos`", variable=var8,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        acos.grid(row=1,column=0)
        acos1=Entry(f32,textvariable=acosv,width=3,bd=2,state=DISABLED)
        acos1.grid(row=1,column=1)
        Label(f32,text="=",bg="GRAY").grid(row=1,column=2)
        acos2=Entry(f32,textvariable=acosa,width=15,bd=4,state=DISABLED)
        acos2.grid(row=1,column=3)
        atan=Checkbutton(f32, text="Tan`", variable=var9,font=('arial',18, 'bold'),command=trigno1,onvalue = 1,bg="GRAY", offvalue = 0)
        atan.grid(row=2,column=0)
        atan1=Entry(f32,textvariable=atanv,width=3,bd=2,state=DISABLED)
        atan1.grid(row=2,column=1)
        Label(f32,text="=",bg="GRAY").grid(row=2,column=2)
        atan2=Entry(f32,textvariable=atana,width=15,bd=4,state=DISABLED)
        atan2.grid(row=2,column=3)
        Label(f32,text="\t\t\t",bg="GRAY").grid(row=0,column=4)
        
        
        Label(f31,text="      ",bg="GRAY").grid(row=6,column=3)
        Button(f31,text="Done",command=func).grid(row=7,column=3)
    
#-------------------------------trignometry finish & p and c start------------------------------------------------------------------------------------------
    
    def pandc():
        ccolor()
        b6.config(fg="GRAY",bg="WHITE")
        for child in f3.winfo_children():
            child.destroy()
        var1=IntVar()
        var2=IntVar()
        p2v=IntVar()
        p3v=IntVar()
        p4v=IntVar()
        c2v=IntVar()
        c3v=IntVar()
        c4v=IntVar()
        def pandc1():
            if var1.get()==1:
                p2.configure(state=NORMAL)
                p3.configure(state=NORMAL)
            if var2.get()==1:
                c2.configure(state=NORMAL)
                c3.configure(state=NORMAL)
        def pandc2():
            def fact(n):
                n1=1
                for i in range(1,n+1):
                    n1=n1*i
                return n1
            if var1.get()==1:
                m1=p2v.get()
                n1=p3v.get()
                if m1<n1:
                    return
                a=fact(m1)
                b=fact(m1-n1)
                p4v.set(a/b)
            if var2.get()==1:
                m1=c2v.get()
                n1=c3v.get()
                if m1<n1:
                    return
                a=fact(m1)
                b=fact(n1)
                c=fact(m1-n1)
                b=b*c
                c4v.set(a/b)
        f31=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",width=530,height=620)
        f31.pack(side=LEFT)
        f31.pack_propagate(False)
        f32=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",width=430,height=620)
        f32.pack(side=RIGHT)
        f32.pack_propagate(False)
        Label(f31,text="\t",bg="GRAY").grid(row=0,column=0)
        p1=Checkbutton(f31, text="    P", variable=var1,font=('arial',18, 'bold'),command=pandc1,onvalue = 1,bg="GRAY", offvalue = 0)
        p1.grid(row=0,column=1)
        p2=Entry(f31,textvariable=p2v,width=3,state=DISABLED,bd=3)
        p2.grid(row=0,column=1)
        p3=Entry(f31,textvariable=p3v,width=3,state=DISABLED,bd=3)
        p3.grid(row=0,column=2)
        Label(f31,text="=",bg="GRAY").grid(row=0,column=3)
        p4=Entry(f31,textvariable=p4v,width=10,bd=4,state=DISABLED)
        p4.grid(row=0,column=4)
        c1=Checkbutton(f31, text="    C", variable=var2,font=('arial',18, 'bold'),command=pandc1,onvalue = 1,bg="GRAY", offvalue = 0)
        c1.grid(row=1,column=1)
        c2=Entry(f31,textvariable=c2v,width=3,state=DISABLED,bd=3)
        c2.grid(row=1,column=1)
        c3=Entry(f31,textvariable=c3v,width=3,state=DISABLED,bd=3)
        c3.grid(row=1,column=2)
        Label(f31,text="=",bg="GRAY").grid(row=1,column=3)
        c4=Entry(f31,textvariable=c4v,width=10,bd=4,state=DISABLED)
        c4.grid(row=1,column=4)
        Label(f31,text="\t",bg="GRAY",bd=4).grid(row=2,column=2)
        Button(f31,text="Find",bd=8,bg="GRAY",command=pandc2).grid(row=3,column=2)
        
#-----------------------------p and c finish and other start-------------------------------------------------------------------------------
        
    def other():
        ccolor()
        b7.config(fg="GRAY",bg="WHITE")
        for child in f3.winfo_children():
            child.destroy()
        x=IntVar()
        y=IntVar()
        ans=IntVar()
        def power():
            for child in f321.winfo_children():
                child.destroy()
            def cal():
                ans.set(math.pow(x.get(),y.get()))
            Label(f321,text=" ",bg="GRAY").grid(row=0,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=1,column=0)
            Entry(f321,bd=3,textvariable=x,width=3).grid(row=2,column=1)
            Label(f321,bd=6,text="Pow",bg="GRAY",fg="WHITE",font=('arial',15)).grid(row=2,column=2)
            Entry(f321,bd=3,textvariable=y,width=3).grid(row=2,column=3)
            Label(f321,bd=6,bg="GRAY",text="=",font=('arial',15)).grid(row=2,column=4)
            Entry(f321,bd=3,textvariable=ans,width=4).grid(row=2,column=5)
            Label(f321,text=" ",bg="GRAY").grid(row=3,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=4,column=0)
            Button(f321,bd=3,text="Calculate",bg="WHITE",fg="powder blue",font=('arial',25),command=cal).grid(row=4,columnspan=5)
        def e():
            for child in f321.winfo_children():
                child.destroy()
            def cal():
                ans.set(math.pow(math.e,x.get()))
            Label(f321,text=" ",bg="GRAY").grid(row=0,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=1,column=0)
            Label(f321,bd=6,text="e^",bg="GRAY",fg="WHITE",font=('arial',20)).grid(row=2,column=1)
            Entry(f321,bd=3,textvariable=x,width=3).grid(row=2,column=2)
            Label(f321,bd=6,bg="GRAY",text="=",font=('arial',15)).grid(row=2,column=3)
            Entry(f321,bd=3,textvariable=ans,width=10).grid(row=2,column=4)
            Label(f321,text=" ",bg="GRAY").grid(row=3,column=0)
            Label(f321,text=" ",bg="GRAY").grid(row=4,column=0)
            Button(f321,bd=3,text="Calculate",bg="WHITE",fg="powder blue",font=('arial',25),command=cal).grid(row=4,columnspan=5)
        f31=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=1,bg="GRAY",height=620,width=200)
        f31.pack(side=LEFT)
        f31.pack_propagate(False)
        f32=Frame(f3,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",height=620,width=760)
        f32.pack(side=RIGHT)
        f32.pack_propagate(False)
        f321=Frame(f32,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",height=500,width=760)
        f321.pack(side=TOP)
        f321.pack_propagate(False)
        f322=Frame(f32,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=0,bg="GRAY",height=120,width=760)
        f322.pack()
        f322.pack_propagate(False)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="POWER",bg="WHITE",fg="GRAY",bd=10,width=20,command=power).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="log",bg="WHITE",bd=10,fg="GRAY",width=20,command=func).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="e^x",bg="WHITE",bd=10,fg="GRAY",width=20,command=e).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="X mod Y",bg="WHITE",bd=10,fg="GRAY",width=20,command=func).pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Label(f31,text="\n",bg="GRAY").pack(side=TOP)
        Button(f31,text="log10",bg="WHITE",bd=10,fg="GRAY",width=20,command=func).pack(side=TOP)

#==================================other finish================================================================================
        
        
    f2=Frame(cf,highlightbackground="BLACK",highlightcolor="BLACK",highlightthickness=1,bg="dim gray",width=365,height=620)
    f2.pack(side=LEFT)
    f2.pack_propagate(False)
    f3=Frame(cf,highlightbackground="BLACK", highlightcolor="BLACK",highlightthickness=3,width=960,height=620,bg="GRAY")
    f3.pack(side=RIGHT)
    f3.pack_propagate(False)
    list = f3.grid_slaves()
    for l in list:
        l.destroy()
    Label(f2,text="         ",bg="white").pack()
    b1=Button(f2,text="NORMAL MODE",fg="WHITE",bg="GRAY",width=30,height=2,command=calentry,bd=8)
    b1.pack()
    Label(f2,text="         ",bg="white").pack()
    b2=Button(f2,text="COMPLEX ANALYSIS",fg="WHITE",bg="GRAY",width=30,height=2,command=complex1,bd=8)
    b2.pack()
    Label(f2,text="         ",bg="white").pack()
    b3=Button(f2,text="MATRIX",fg="WHITE",bg="GRAY",width=30,height=2,command=matrix,bd=8)
    b3.pack()
    Label(f2,text="         ",bg="white").pack()
    b4=Button(f2,text="EQUATION SOLVE",fg="WHITE",bg="GRAY",width=30,height=2,command=equation,bd=8)
    b4.pack()
    Label(f2,text="         ",bg="white").pack()
    b5=Button(f2,text="TRIGNOMETRY",fg="WHITE",bg="GRAY",width=30,height=2,command=trigno,bd=8)
    b5.pack()
    Label(f2,text="         ",bg="white").pack()
    b6=Button(f2,text="PERMUTATION & COMBINATION",fg="WHITE",bg="GRAY",width=30,height=2,command=pandc,bd=8)
    b6.pack()
    Label(f2,text="         ",bg="white").pack()
    b7=Button(f2,text="OTHERS",fg="WHITE",bg="GRAY",width=30,height=2,command=other,bd=8)
    b7.pack()
    Label(f2,text="         ",bg="white").pack()
    b8=Button(f2,text="HELP",fg="WHITE",bg="GRAY",width=30,height=2,command=func,bd=8)
    b8.pack()
    Label(f2,text="         ",bg="white").pack()
""" frame design finish"""

""" Button in frame1"""

home1=Button(f1,text="HOME",width=28,height=3,bg="GRAY",fg="WHITE",command=home,bd=14)
home1.pack(side=LEFT)
Button(f1,text="PROFILE",width=28,height=3,bg="GRAY",fg="WHITE",command=func,bd=14).pack(side=LEFT)
Button(f1,text="GAMES",width=28,height=3,fg="WHITE",bg="GRAY",command=func,bd=11).pack(side=LEFT)
calframe1=Button(f1,text="CALCULATOR",width=28,height=3,fg="WHITE",bg="GRAY",command=calframe,bd=11)
calframe1.pack(side=LEFT)
Button(f1,text="Help",width=28,height=3,fg="WHITE",bg="GRAY",command=func,bd=11).pack(side=LEFT)
Button(f1,text="QUIT",width=28,height=3,fg="WHITE",bg="GRAY",command=win.destroy,bd=11).pack(side=LEFT)
f5=Frame(win,highlightbackground="GHOSTWHITE",highlightcolor="GHOSTWHITE",highlightthickness=1,bg="GRAY",width=1370,height=20,bd=8)
f5.pack(side=BOTTOM)
f5.pack_propagate(False)
f6=Frame(win,highlightbackground="WHITE",highlightcolor="GHOSTWHITE",highlightthickness=1,width=20,height=615,bg="GRAY")
f6.pack(side=LEFT)
f6.pack_propagate(False)
f7=Frame(win,highlightbackground="WHITE",highlightcolor="GHOSTWHITE",highlightthickness=1,width=20,height=615,bg="GRAY")
f7.pack(side=RIGHT)
f7.pack_propagate(False)
cf=Frame(win,highlightbackground="GHOSTWHITE",highlightcolor="GHOSTWHITE",highlightthickness=1,bg="WHITE",width=1325,height=620)
cf.pack()
cf.pack_propagate(False)
""" Button in frame1 finish"""
win.mainloop()
