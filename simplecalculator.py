from tkinter import *

root=Tk()
root.title("juin's simple gui Calculator")

entry_field=Entry(width=50,borderwidth=5)
entry_field.grid(row=0,column=0,columnspan=4)

def button_click(number):
    current=entry_field.get()
    entry_field.delete(0,END)
    entry_field.insert(0,str(current)+str(number))

def operator_click(operator):
    current=entry_field.get()
    entry_field.delete(0,END)
    entry_field.insert(0,str(current)+operator)

def equal_click():
    try:
        result=eval(entry_field.get())
        entry_field.delete(0,END)
        entry_field.insert(0,result)
    except:
        entry_field.delete(0,END)
        entry_field.insert(0,"ERROR")

def clear_click():
    entry_field.delete(0,END)

button_7=Button(root,text="7",padx=30,pady=10,command=lambda:button_click(7))
button_8=Button(root,text="8",padx=30,pady=10,command=lambda:button_click(8))
button_9=Button(root,text="9",padx=30,pady=10,command=lambda:button_click(9))
button_4=Button(root,text="4",padx=30,pady=10,command=lambda:button_click(4))
button_5=Button(root,text="5",padx=30,pady=10,command=lambda:button_click(5))
button_6=Button(root,text="6",padx=30,pady=10,command=lambda:button_click(6))
button_1=Button(root,text="1",padx=30,pady=10,command=lambda:button_click(1))
button_2=Button(root,text="2",padx=30,pady=10,command=lambda:button_click(2))
button_3=Button(root,text="3",padx=30,pady=10,command=lambda:button_click(3))
button_0=Button(root,text="0",padx=30,pady=10,command=lambda:button_click(0))

button_add=Button(root,text="+",padx=30,pady=10,command=lambda:operator_click("+"))
button_sub=Button(root,text="-",padx=30,pady=10,command=lambda:operator_click("-"))
button_mul=Button(root,text="*",padx=30,pady=10,command=lambda:operator_click("*"))
button_div=Button(root,text="/",padx=30,pady=10,command=lambda:operator_click("/"))
button_equal=Button(root,text="=",padx=30,pady=10,command=equal_click)
button_clear=Button(root,text="C",padx=30,pady=10,command=clear_click)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_div.grid(row=4,column=3)

    
