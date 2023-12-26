from tools import *
from tkinter import ttk
frm =form()
num1 =inboxnum("enter Number1:",True)
num2 =inboxnum("enter Number1:",True)
r = int(num1) + int(num2)
msgbox(str(r))
ttk.Button(frm,text="adding").pack(pady=10)
frm.mainloop()
