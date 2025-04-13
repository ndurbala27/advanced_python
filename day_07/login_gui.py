import login
from tkinter.messagebox import showinfo
import tkinter as tk

clicks = 1
def btn_click(event):
    usr = uname.get()
    pwd = pword.get()
    rslt = login.auth(usr, pwd)
    uname.set("")
    pword.set("")
    showinfo(title="Result", message=rslt)

# Window geometry
wd = '300'
ht = '200'
x = '+100'
y = '+100'

mainwin = tk.Tk()
mainwin.geometry(f"{wd}x{ht}{x}{y}")
mainwin.title("Login")

uname = tk.StringVar()
usr_lbl = tk.Label(text="Username: ")
usr_lbl.grid(row=0, column=0)
usr_box = tk.Entry(textvariable=uname)
usr_box.grid(row=0, column=1)

pword = tk.StringVar()
pwd_lbl = tk.Label(text="Password: ")
pwd_lbl.grid(row=1, column=0)
pwd_box = tk.Entry(textvariable=pword, show="*")
pwd_box.grid(row=1, column=1)




btn = tk.Button(mainwin, text="Login")
btn.bind("<Button>", btn_click)
btn.grid(row=3, column=1)



mainwin.mainloop()

