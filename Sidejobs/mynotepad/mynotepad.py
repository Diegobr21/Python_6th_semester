from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from io import open

fileroute=""

def aboutus():
    MessageBox.showinfo('About Us', 'This is a GUI for test purposes, just have fun')
def help():
    MessageBox.showinfo('Help', 'This is a GUI for test purposes, just have fun')
def exit():
    answer=MessageBox.askyesno('Exit', 'Are you sure you want to exit')
    if answer:
        root.destroy()
def newf():
    global fileroute
    mssg.set('New File')
    fileroute=""
    textbox.delete(1.0, 'end')
def bg_color():
    color=ColorChooser.askcolor(title='Choose new background color')
    textbox.config(bg=color[1])
def font_color():
    color=ColorChooser.askcolor(title='Choose new font color')
    textbox.config(fg=color[1])

def openf():
    global fileroute
    mssg.set('Open File')
    fileroute=FileDialog.askopenfilename(title='Open a file', initialdir='.',
                                        filetypes=(("Text files","*.txt"), 
                                        ) )
    if fileroute != "":
        file_r=open(fileroute, 'r')
        text=file_r.read()
        textbox.delete(1.0, 'end')
        textbox.insert('insert', text)
        file_r.close()
        root.title(fileroute + " - My Text Editor")

def savef():
    mssg.set('Save File')
    if fileroute != "":
        text=textbox.get(1.0, 'end-1c')
        file_w=open(fileroute, 'w+')
        file_w.write(text)
        file_w.close()
        mssg.set('Saved')
    else:
        savef_as()
    
def savef_as():
    global fileroute
    mssg.set('Save File As...')
    f=FileDialog.asksaveasfile(title='Save as ...', mode='w', defaultextension=".txt") #en formato write
    if f is not None:
        fileroute=f.name
        text=textbox.get(1.0, 'end-1c')
        f=open(fileroute, 'w+')
        f.write(text)
        f.close()
        mssg.set('Saved As'+ f.name)
    else:
        mssg.set('Saved Canceled')
        fileroute=""


root=Tk()
root.title('My Text Editor')
root.iconbitmap('pencil.ico')

    


########Menu
menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label='New File', command=newf)
filemenu.add_command(label='Open File', command=openf)
filemenu.add_command(label='Save', command=savef)
filemenu.add_command(label='Save As', command=savef_as)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=exit)


editmenu=Menu(menubar, tearoff=0)
editmenu.add_command(label='Change bckgd color', command=bg_color)
editmenu.add_command(label='Change font color', command=font_color)



helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label='Welcome')
helpmenu.add_command(label='Help me', command=help)
helpmenu.add_separator()
helpmenu.add_command(label='About Us', command=aboutus)


menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)
menubar.add_cascade(label='Help', menu=helpmenu)
###########################################################
#Textbox

textbox=Text(root)
textbox.pack (fill= 'both', expand=1)
textbox.config(bd=0, padx=5, pady=3, font=('Consolas', 12), fg='white', bg='black')

mssg=StringVar()
mssg.set('Welcome!')
btmmessage=Label(root, textvar=mssg, justify='left')
btmmessage.pack(side='left')


root.mainloop()