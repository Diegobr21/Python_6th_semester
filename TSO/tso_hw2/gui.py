from knapsack import *
from tkinter import*

root = Tk()
root.title("Knapsack problem-solver, TSO_FIME")
frame = Frame(root, width=820, height=520)
frame.pack()
frame.config(cursor = 'pencil', bg = 'blue', border = 15, relief = 'ridge')
root.resizable(0, 0)

"""
btn=Button(frame, text='Read instance', command= initialize())# ,command=classify)
btn.place(x=320, y=60)
"""
res_var1 = StringVar()
res_var2 = StringVar()
res_var3 = StringVar()
n_f_g = StringVar()

def reset():
    res_var1.set('')
    res_var2.set('')
    res_var3.set('')

def greatest_value():
    obj_func=select_from_gui(1)    
    res_var1.set(f"{obj_func} ")

def lower_weight():
    obj_func=select_from_gui(2)    
    res_var2.set(f"{obj_func} ")

def greatest_ratio():
    obj_func=select_from_gui(3)    
    res_var3.set(f"{obj_func} ")


    

titulo=Label(frame, text='Choose the heuristic to solve your problem')
titulo.config(bg='blue', fg='white', font=('verdana', 14))
titulo.place(x=170, y=50)

btn1=Button(frame, text='Pick greatest value', command= greatest_value)
btn1.place(x=70, y=200)

btn2=Button(frame, text='Pick lowest weight', command= lower_weight)
btn2.place(x=300, y=200)

btn3=Button(frame, text='Pick biggest ratio', command= greatest_ratio)
btn3.place(x=550, y=200)

res=Label(frame, text='ROF = Result of the objective function(sum of values)')
res.config(bg='blue', fg='white', font=('verdana', 12))
res.place(x=150, y=350)

rof1=Label(frame, text='ROF')
rof1.config(bg='blue', fg='white', font=('verdana', 10))
rof1.place(x=90, y=280)
result1=Entry(frame, width=20, textvariable=res_var1)
result1.place(x=60, y=300)

rof2=Label(frame, text='ROF')
rof2.config(bg='blue', fg='white', font=('verdana', 10))
rof2.place(x=320, y=280)
result2=Entry(frame, width=20, textvariable=res_var2)
result2.place(x=290, y=300)

rof3=Label(frame, text='ROF')
rof3.config(bg='blue', fg='white', font=('verdana', 10))
rof3.place(x=570, y=280)
result3=Entry(frame, width=20, textvariable=res_var3)
result3.place(x=540, y=300)


btnreset=Button(frame, text='Reset All', command=reset)
btnreset.place(x=390, y=420)

#At the bottom
root.mainloop()