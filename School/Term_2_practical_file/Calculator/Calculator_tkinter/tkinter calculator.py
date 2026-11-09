from tkinter import *
window=Tk()
window.title("CALCULATOR")#to rename the title of the window
expression=""
text=StringVar()
window.configure(background="light blue")
def press(n):
    global expression
    expression+=str(n)
    text.set(expression)
def btnclear():
    global expression
    expression=""
    text.set(expression)
def btnequals():
    global expression
    expression=expression.lstrip('0')
    n=""
    m=0
    for i in expression:
        if i=="0":
           if m==0:
               n=n+i
        elif i=="+" or "-" or "/" or "*":
           m=1
           n=n+i
        else:
            m=0
            n=n+i
    result=str(eval(n))
    expression=""
    text.set(result)
    expression=""
display=Entry(window,textvariable=text,bg="light grey")
display.grid(columnspan=4,ipadx=70)
button1=Button(window,text='1',bg="dark blue",fg="White",command=lambda: press(1),height=1,width=7)
button1.grid(row=2,column=0)
button2 = Button(window, text=' 2 ', fg='White', bg='dark blue',command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
button3 = Button(window, text=' 3 ', fg='White', bg='dark blue',command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
button4 = Button(window, text=' 4 ', fg='White', bg='dark blue',command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
button5 = Button(window, text=' 5 ', fg='White', bg='dark blue',command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
button6 = Button(window, text=' 6 ', fg='White', bg='dark blue',command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
button7 = Button(window, text=' 7 ', fg='White', bg='dark blue',command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
button8 = Button(window, text=' 8 ', fg='White', bg='dark blue',command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
button9 = Button(window, text=' 9 ', fg='White', bg='dark blue',command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
button0 = Button(window, text=' 0 ', fg='White', bg='dark blue',command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=1)
plus = Button(window, text=' + ', fg='dark blue', bg='White',command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)
minus = Button(window, text=' - ', fg='dark blue', bg='White',command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)
multiply = Button(window, text=' * ', fg='dark blue', bg='White',command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)
divide = Button(window, text=' / ', fg='dark blue', bg='White',command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)
equal = Button(window, text=' = ', fg='dark blue', bg='White',command=btnequals, height=1, width=7)
equal.grid(row=5, column=2)
clear = Button(window, text='Clear', fg='dark blue', bg='White',command=btnclear, height=1, width=7)
clear.grid(row=6, column=1)
Decimal= Button(window, text='.', fg='dark blue', bg='White',command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=5, column=0)
window.mainloop()
