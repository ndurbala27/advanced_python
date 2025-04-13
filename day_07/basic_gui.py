import tkinter as tk

clicks = 1
def btn_click(event):
    global clicks
    # print(f"{clicks}")
    msg4.config(text=clicks)
    clicks += 1

# Window geometry
wd = '300'
ht = '200'
x = '+100'
y = '+100'

mainwin = tk.Tk()
mainwin.geometry(f"{wd}x{ht}{x}{y}")
mainwin.title("Hello")


msg = tk.Label(text="Hello, World!")
msg.grid(row=0, column=0)
msg2 = tk.Label(text="Hello, World!")
msg2.grid(row=1, column=1)
msg3 = tk.Label(text="Hello, World!")
msg3.grid(row=2, column=2)
msg4 = tk.Label()
msg4.grid(row=4, column=0)

btn = tk.Button(mainwin, text="Click Me")
btn.bind("<Button>", btn_click)
btn.grid(row=3, column=0)



mainwin.mainloop()

