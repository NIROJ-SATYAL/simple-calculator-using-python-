import tkinter
from tkinter import *
from functools import partial


win=Tk()
def sum(l1,x1,x2):
    n1=(x1.get())
    n2=(x2.get())
    sum=int(n1)+int(n2)
    l1.config(text='sum is: %d' %sum)
    return
def diff(l3,x1,x2):
    a1=(x1.get())
    a2=(x2.get())
    diff=int(a1)-int(a2)
    l3.config(text='difference is:%d' %diff)
    return
def div(l4,x1,x2):
    b1=(x1.get())
    b2=(x2.get())
    div=int(b1)/int(b2)
    l4.config(text='division is:%f' %div)
    return
def mul(l5,x1,x2):
    c1=(x1.get())
    c2=(x2.get())
    mul=int(c1)*int(c2)
    l5.config(text='mul is:%d' %mul)
    return
win.geometry("500x500")
b=Label(win,text='CALCULATOR',activeforeground='red')
b.grid(row=1,column=5)
l=Label(win,text='first num')
l.grid(row=2,column=0)
l2=Label(win,text='second  num')
l2.grid(row=3,column=0)
l1=Label(win)
l1.grid(row=9,column=0)
l3=Label(win)
l3.grid(row=10,column=0)
l4=Label(win)
l4.grid(row=11,column=0)
l5=Label(win)
l5.grid(row=12,column=0)
x1=StringVar()
x2=StringVar()
e1=Entry(win,textvariable=x1)
e1.grid(row=2,column=2)
e2=Entry(win,textvariable=x2)
e2.grid(row=3,column=2)
sum=partial(sum,l1,x1,x2)
diff=partial(diff,l3,x1,x2)
div=partial(div,l4,x1,x2)
mul=partial(mul,l5,x1,x2)
rb1=Button(win,text='calculate',activeforeground='blue',command=diff)
rb1.grid(row=5,column=0)
rb2=Button(win,text='calculate',activeforeground='red',command=sum)
rb2.grid(row=6,column=0)
rb3=Button(win,text='calculate',activeforeground='yellow',command=div)
rb3.grid(row=7,column=0)
rb4=Button(win,text='calculate',activeforeground='green',command=mul)
rb4.grid(row=8,column=0)
win.mainloop()