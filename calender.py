from tkinter import *
import time
win=Tk()
win.geometry("1350x700+0+0")
win.resizable(width=False,height=False)
win.title("APSR(python 3.6)")
t=list()
def monthy():
    global t
    t=time.asctime()
    t=t.split(" ")
def dayton(ch):
    if ch=='Sun':
        n=0
    if ch=='Mon':
        n=1
    if ch=='Tue':
        n=2
    if ch=='Wed':
        n=3
    if ch=='Thu':
        n=4
    if ch=='Fri':
        n=5
    if ch=='Sat':
        n=6
    return n
def ntoday(no):
    if no==0:
        ch1='Sun'
    if no==1:
        ch1='Mon'
    if no==2:
        ch1='Tue'
    if no==3:
        ch1='Wed'
    if no==4:
        ch1='Thu'
    if no==5:
        ch1='Fri'
    if no==6:
        ch1='Sat'
    return ch1
Frame(win,width=1350,height=100).pack(side=TOP)
f2=Frame(win,width=1350,height=450,highlightbackground="BLACK",highlightcolor="GHOSTWHITE",highlightthickness=0)
f2.pack(side=TOP)
Frame(f2,width=400,height=450,highlightbackground="BLACK",highlightcolor="GHOSTWHITE",highlightthickness=0).pack(side=LEFT)
f21=Frame(f2,width=950,height=450,highlightbackground="BLACK",highlightcolor="GHOSTWHITE",highlightthickness=0)
f21.pack()
c=Frame(f21,width=550,height=450,highlightbackground="BLACK",highlightcolor="GHOSTWHITE",highlightthickness=4)
c.pack(side=LEFT)
c.pack_propagate(False)
Frame(f21,width=400,height=450,highlightbackground="BLACK",highlightcolor="GHOSTWHITE",highlightthickness=0).pack(side=RIGHT)
Frame(win,width=1350,height=150).pack(side=BOTTOM)
c1=Frame(c,width=550,height=70,highlightbackground="BLACK",highlightcolor="GHOSTWHITE",highlightthickness=1)
c1.pack(side=TOP)
c1.pack_propagate(False)
c2=Frame(c,width=550,height=380,highlightbackground="BLACK",highlightcolor="GHOSTWHITE",highlightthickness=0)
c2.pack()
c2.pack_propagate(False)
#===================================================================================================
monthy()
month=t[1]+"("+t[5]+")"
Button(c1,text=month,font=('arial',26),width=25).pack()
#====================================================================================================
Button(c2,text="SUNDAY",fg="WHITE",bg="RED",bd=4,height=3,width=10).grid(row=0,column=0)
Button(c2,text="MONDAY",fg="WHITE",bg="blue",bd=4,height=3,width=9).grid(row=0,column=1)
Button(c2,text="TUESDAY",fg="WHITE",bg="blue",bd=4,height=3,width=9).grid(row=0,column=2)
Button(c2,text="WEDNESDAY",fg="WHITE",bg="blue",bd=4,height=3,width=9).grid(row=0,column=3)
Button(c2,text="THURSDAY",fg="WHITE",bg="blue",height=3,bd=4,width=9).grid(row=0,column=4)
Button(c2,text="FRIDAY",fg="WHITE",bg="blue",height=3,bd=4,width=9).grid(row=0,column=5)
Button(c2,text="SATURDAY",fg="WHITE",bg="blue",height=3,bd=4,width=9).grid(row=0,column=6)
#=====================================================================================================
r11=Button(c2,text="",bd=4,height=2,width=10)
r11.grid(row=1,column=0)
r12=Button(c2,text="",bd=4,height=2,width=9)
r12.grid(row=1,column=1)
r13=Button(c2,text="",bd=4,height=2,width=9)
r13.grid(row=1,column=2)
r14=Button(c2,text="",bd=4,height=2,width=9)
r14.grid(row=1,column=3)
r15=Button(c2,text="",height=2,bd=4,width=9)
r15.grid(row=1,column=4)
r16=Button(c2,text="",height=2,bd=4,width=9)
r16.grid(row=1,column=5)
r17=Button(c2,text="",height=2,bd=4,width=9)
r17.grid(row=1,column=6)
#======================================================================================================
r21=Button(c2,text="",bd=4,height=2,width=10)
r21.grid(row=2,column=0)
r22=Button(c2,text="",bd=4,height=2,width=9)
r22.grid(row=2,column=1)
r23=Button(c2,text="",bd=4,height=2,width=9)
r23.grid(row=2,column=2)
r24=Button(c2,text="",bd=4,height=2,width=9)
r24.grid(row=2,column=3)
r25=Button(c2,text="",height=2,bd=4,width=9)
r25.grid(row=2,column=4)
r26=Button(c2,text="",height=2,bd=4,width=9)
r26.grid(row=2,column=5)
r27=Button(c2,text="",height=2,bd=4,width=9)
r27.grid(row=2,column=6)
#======================================================================================================
r31=Button(c2,text="",bd=4,height=2,width=10)
r31.grid(row=3,column=0)
r32=Button(c2,text="",bd=4,height=2,width=9)
r32.grid(row=3,column=1)
r33=Button(c2,text="",bd=4,height=2,width=9)
r33.grid(row=3,column=2)
r34=Button(c2,text="",bd=4,height=2,width=9)
r34.grid(row=3,column=3)
r35=Button(c2,text="",height=2,bd=4,width=9)
r35.grid(row=3,column=4)
r36=Button(c2,text="",height=2,bd=4,width=9)
r36.grid(row=3,column=5)
r37=Button(c2,text="",height=2,bd=4,width=9)
r37.grid(row=3,column=6)
#========================================================================================================
r41=Button(c2,text="",bd=4,height=2,width=10)
r41.grid(row=4,column=0)
r42=Button(c2,text="",bd=4,height=2,width=9)
r42.grid(row=4,column=1)
r43=Button(c2,text="",bd=4,height=2,width=9)
r43.grid(row=4,column=2)
r44=Button(c2,text="",bd=4,height=2,width=9)
r44.grid(row=4,column=3)
r45=Button(c2,text="",height=2,bd=4,width=9)
r45.grid(row=4,column=4)
r46=Button(c2,text="",height=2,bd=4,width=9)
r46.grid(row=4,column=5)
r47=Button(c2,text="",height=2,bd=4,width=9)
r47.grid(row=4,column=6)
#========================================================================================================
r51=Button(c2,text="",bd=4,height=2,width=10)
r51.grid(row=5,column=0)
r52=Button(c2,text="",bd=4,height=2,width=9)
r52.grid(row=5,column=1)
r53=Button(c2,text="",bd=4,height=2,width=9)
r53.grid(row=5,column=2)
r54=Button(c2,text="",bd=4,height=2,width=9)
r54.grid(row=5,column=3)
r55=Button(c2,text="",height=2,bd=4,width=9)
r55.grid(row=5,column=4)
r56=Button(c2,text="",height=2,bd=4,width=9)
r56.grid(row=5,column=5)
r57=Button(c2,text="",height=2,bd=4,width=9)
r57.grid(row=5,column=6)
#========================================================================================================

def cal1():
    global t
    ch=str(t[0])
    date=int(t[3])
    n1=dayton(ch)
    while(date):
        n1=n1-1
        date=date-1
        if n1<0:
            n1=6
        if date==1:
            break;
    print(ntoday(n1))
    print(date)
cal1()
win.mainloop()