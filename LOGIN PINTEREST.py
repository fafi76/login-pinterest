from tkinter import *
from tkinter import messagebox
import ast
import time



root=Tk()
root.title("Sgin in")
root.geometry("925x500+300+200")
root.configure(bg= "#fff")
root.resizable(False,False)

img1 = PhotoImage(file="background.png")
lblimg=Label(root,image=img1,bg="white")
lblimg.place(height=900,width=925,x=0, y=0)

bg2 = PhotoImage(file="app.png")
root.iconphoto(False,bg2)

def sginin() :
    username=user.get()
    password=code.get()

    # file=open("datasheet.txt","r")
    # d=file.read()
    # r=ast.literal_eval(d)
    # file.close()

    # # print(r.keys())
    # # print(r.values())

    # if username in r.keys() and password == r[username] :

    if username == "fatemeh" and password == "1234" :
        screen= Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        Label(screen,text="hello world", bg="#fff", font=("calibri(body)",50,"bold")).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror("invalid","invalid username or password")

def sginup_command():
    window=Toplevel(root)
 #######################################################################################################       
    window.title("Sgin up")
    window.geometry("925x500+300+200")
    window.configure(bg= "#fff")
    window.resizable(False,False)

    bg2 = PhotoImage(file="app.png")
    window.iconphoto(False,bg2)

    img4 = PhotoImage(file="background2.png")
    lblimg4= Label(window,image=img4,bg="white")
    lblimg4.place(height=900, width=925, x=0, y=0)

    def sginup() :
        username=user.get()
        password=code.get()
        concorm_password=conform_code.get()

        if password == concorm_password :

            try:
                file=open("dateeshe.txt",'r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open("dateeshe.txt","w")
                W=file.write(str(r))

                messagebox.showinfo("sginup","sucessfully sgin up")
                window.destroy()
            except:
                file=open("dateeshe.txt","w")
                pp=str({"username" :"password"})
                file.write(pp)
                file.close()
                window.destroy()
            # else:
            #     messagebox.showerror("invalid","both password should match")    

    def sgin():
        window.destroy()

  
    framew= Frame(window, height=455, width=880,bg="white" )
    framew.place(x=20, y=20)

    img2 = PhotoImage(file="icon.png")
    lblimg=Label(framew,image=img2,bg="white")
    lblimg.place(height=455,width=530,x=0, y=0)


    frame2=Frame(framew,height=455, width=350, bg="white")
    frame2.place(x=550, y=20)

    imgp = PhotoImage(file="pinterest1.png")
    lblimgp=Label(frame2,image=imgp,bg="white")
    lblimgp.place(height=100,width=300,x=15, y=0)

    #user

    def on_enter(e) :
        user.delete(0,"end")

    def on_leave(e) :
        name=user.get()
        if name=="" :
            user.insert(0, 'user name')

    user=Entry(frame2,width=25, fg="black", border=0, bg="white", font=("microsoft yahei UI light",11))
    user.place(x=25, y=123)
    user.insert(0,"user name")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame(frame2,width=275, height=1, bg="black").place(x=25,y=150)

    #code

    def on_enter(e) :
        code.delete(0,"end")

    def on_leave(e) :
        name=code.get()
        if name=="" :
            code.insert(0, 'password')

    code=Entry(frame2,width=25, fg="black", border=0, bg="white", font=("microsoft yahei UI light",11))
    code.place(x=25, y=173)
    code.insert(0,"password")
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)

    Frame(frame2,width=275, height=1, bg="black").place(x=25,y=200)

    ###########################

    def on_enter(e) :
        conform_code.delete(0,"end")

    def on_leave(e) :
        name=conform_code.get()
        if name=="" :
            conform_code.insert(0, 'conform password')

    conform_code=Entry(frame2,width=39, fg="black", border=0, bg="white", font=("microsoft yahei UI light",11))
    conform_code.place(x=25, y=223)
    conform_code.insert(0,"conform password")
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",on_leave)

    Frame(frame2,width=275, height=1, bg="black").place(x=25,y=250)

    ###############################

    Button(frame2,width=39, pady=7, text="Sgin up", bg="#57a1f8", fg="white", border=0,command=sginup).place(x=25,y=290)

    label=Label(frame2,text="I have an account?", fg="black", bg="white",font=("m,crosoft yahei UI light", 9))
    label.place(x=75, y=350)

    sginin= Button(frame2,width=6, text="sgin in", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sgin)
    sginin.place(x=200, y=350)


    window.mainloop()
###########################################################################################################################

frame1= Frame(root, height=455, width=880,bg="white" )
frame1.place(x=20, y=20)

img2 = PhotoImage(file="icon.png")
lblimg=Label(frame1,image=img2,bg="white")
lblimg.place(height=455,width=530,x=0, y=0)

####################

frame=Frame(root,height=455, width=350, bg="white")
frame.place(x=550, y=20)

img = PhotoImage(file="pinterest.png")
lblimg=Label(frame,image=img,bg="white")
lblimg.place(height=100,width=300,x=15, y=30)

#user

def on_enter(e) :
    user.delete(0,"end")

def on_leave(e) :
    name=user.get()
    if name=="" :
        user.insert(0, 'user name')

user=Entry(frame,width=39, fg="black", border=0, bg="white", font=("microsoft yahei UI light",11))
user.place(x=35, y=153)
user.insert(0,"user name")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=275, height=1, bg="black").place(x=35,y=180)

#code

def on_enter(e) :
    code.delete(0,"end")

def on_leave(e) :
    name=code.get()
    if name=="" :
        code.insert(0, 'password')

code=Entry(frame,width=39, fg="black", border=0, bg="white", font=("microsoft yahei UI light",11))
code.place(x=35, y=203)
code.insert(0,"password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=275, height=1, bg="black").place(x=35,y=230)

def showpassword():
    if code.cget("show")== "*" :
        code.config(show='')
    else :
        code.config(show="*")


chek_button= Checkbutton(frame,border=0, bg="white", fg="black" ,text="show password",command=showpassword)

chek_button.place(x=200, y=240)

###########################

Button(frame,width=39, pady=7, text="Sgin in", bg="#57a1f8", fg="white", border=0,command=sginin).place(x=35,y=290)

label=Label(frame,text="don't have an account?", fg="black", bg="white",font=("m,crosoft yahei UI light", 9))
label.place(x=75, y=350)

sgin_up= Button(frame,width=6, text="sgin up", border=0, bg="white", cursor="hand2", fg="#57a1f8",command=sginup_command)
sgin_up.place(x=215, y=350)


root.mainloop()