from compoundEffect import CompoundEffect
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


Window = Tk()
Window.title("Compound Effect Calculator")
Window.geometry("500x300+300+115")
Window.resizable(True, True)

f1 = Frame(Window, width=300, height=100)
f2 = Frame(Window, width=300, height=100)
f3 = Frame(Window, width=300, height=100)
f4 = Frame(Window, width=300, height=100)
f5 = Frame(Window, width=300, height=100)
f1.pack(side=TOP)
f2.pack(side=TOP)
f3.pack(side=TOP)
f4.pack(side=TOP)
f5.pack(side=TOP)


Font = "Arial"
asset = IntVar()
percent = IntVar()
step = IntVar()
Txt_Output = StringVar()


def cacl():
    # print(f"asset:{float(asset.get())} percent:{float(percent.get())} step:{float(step.get())}")
    Outbox.config(state="normal")
    Outbox.delete("1.0", "end-1c")
    # res = f"asset:{float(asset.get())} percent:{float(percent.get())} step:{float(step.get())}"
    res = CompoundEffect(float(asset.get()), float(percent.get()), int(step.get()))
    print(f"asset:{float(asset.get())} percent:{float(percent.get())} step:{float(step.get())} res:{res}")
    Outbox.insert(END, res)
    Outbox.config(state="disabled")

#! © Esfandiar Kiani - 2022

Title = Label(
    f1, text="Welcome To My Compound Effect Calculator For Trading", font=(24))

asset_Lbl = Label(f2, text="Base Asset")
asset_Inp = Entry(f3, width=12, textvariable=asset, bd=3, font=(Font, 15))

percent_Lbl = Label(f2, text="%")
percent_Inp = Entry(f3, width=8, textvariable=percent, bd=3, font=(Font, 15))

step_Lbl = Label(f2, text="Step")
step_Inp = Entry(f3, width=6, textvariable=step, bd=3, font=(Font, 15))

Cacl_Btn = ttk.Button(f4, text="Calculate", cursor="hand2", command=cacl)
Outbox = Text(f4, width=15, height=1, bd=1.5, font=(Font, 15))

CopyRight = Label(f5, text="""
©2022 Esfandiar Kiani, All rights reserved.
""")

Title.pack(side=LEFT)

asset_Lbl.pack(side=LEFT,   padx=(15, 85), pady=(35, 0))
percent_Lbl.pack(side=LEFT, padx=(50, 40), pady=(35, 0))
step_Lbl.pack(side=LEFT,    padx=(75, 0), pady=(35, 0))

asset_Inp.pack(side=LEFT,   padx=(0, 60), pady=(0, 45))
percent_Inp.pack(side=LEFT, padx=(0, 50), pady=(0, 45))
step_Inp.pack(side=LEFT,    padx=(0, 0), pady=(0, 45))

Cacl_Btn.pack(side=LEFT, padx=(35, 85), pady=(25, 50))
Outbox.pack(side=LEFT, padx=(85, 35), pady=(25, 50))
CopyRight.pack(side=LEFT)

Window.mainloop()
