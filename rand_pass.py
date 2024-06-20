from tkinter import *
import random
import time
import string
import pyperclip

def cpy_to_clpbrd():
    pyperclip.copy(gen_pass.get())
    copy_status.set("Copied to Clipboard")
    copy_btn.update()
    time.sleep(1)
    copy_status.set("Copy to Clipboard")

def generate_password():
    length = len_sel.get()
    include_special = incl_splc.get()
    include_numbers = incl_num.get()
    include_letters = incl_ltrs.get()
    include_capital = incl_cptl.get()

    characters = ""
    if include_letters:
        characters += string.ascii_lowercase
    if include_capital:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        gen_pass.set(password)
    else:
        gen_pass.set("****")

def update_letters():
    if incl_cptl.get():
        incl_ltrs.set(1)

def update_capital():
    if incl_ltrs.get()==0:
        incl_cptl.set(0)

root = Tk()

root.geometry("500x600")
root.title("Random Password Generator")


gen_pass = StringVar()
copy_status = StringVar()
copy_status.set("Copy to Clipboard")

incl_splc = IntVar(value=1)
incl_num = IntVar(value=1)
incl_ltrs = IntVar(value=1)
incl_cptl = IntVar(value=1)

f_upper = Frame(root, bg="#2D3250")

h1 = Label(f_upper, text="Random Password Generator", font="Poppins 20 bold", bg="#2D3250", fg="#F6B17A", pady=15)
h1.pack()
f_upper.pack(side=TOP, fill=X)

f_2 = Frame(root, pady=15, bg="#424769")
t1 = Label(f_2, text="Generate a Randomized Password", pady=10, font="Poppins 15", fg="#F6B17A", bg="#424769")
t1.pack(anchor="n")
f_2.pack(fill=X)

f_3 = Frame(root, bg="#424769")
gen_pass.set("****")
pass_lab = Label(f_3, textvariable=gen_pass, font="Consolas 20 bold", bg="#2D3250", fg="white", width=20)
pass_lab.pack(anchor="center")

f_3_btns = Frame(f_3, bg="#424769")

copy_btn = Button(f_3_btns, textvariable=copy_status, font="Poppins 12 bold", fg="white", bg="#2D3250", command=cpy_to_clpbrd)
copy_btn.grid(row=0, column=0, padx=10, pady=10)

generate_btn = Button(f_3_btns, text="Generate Password", font="Poppins 12 bold", fg="white", bg="#2D3250", command=generate_password)
generate_btn.grid(row=0, column=1, padx=10, pady=10)

f_3_btns.pack()

f_3a = Frame(f_3, pady=30, bg="#424769")
len_sel = Scale(f_3a, from_=4, to=16, orient=HORIZONTAL, bg="#424769", fg="white", font="Poppins 15", length=250, label="Select the Length", troughcolor="#7077A1")
len_sel.pack(anchor="n")
f_3a.pack(fill=X)


f_3b = Frame(f_3, pady=10, bg="#424769")

Label(f_3b,text="Include: ", font="Poppins 16 bold",fg="white", bg="#424769", padx=5,pady=5).grid(row=0, column=0, sticky="w")
c1 = Checkbutton(f_3b, variable=incl_splc, text="Special Characters", font="Poppins 13 bold", fg="white", bg="#424769")
c1.grid(row=1, column=0, sticky="w", padx=10, pady=5)

c2 = Checkbutton(f_3b, variable=incl_ltrs, text="Letters", font="Poppins 13 bold", fg="white", bg="#424769")
c2.grid(row=1, column=1, sticky="e", padx=10, pady=5)

c3 = Checkbutton(f_3b, variable=incl_num, text="Numbers", font="Poppins 13 bold", fg="white", bg="#424769", command=update_capital)
c3.grid(row=2, column=0, sticky="w", padx=10, pady=5)

c4 = Checkbutton(f_3b, variable=incl_cptl, text="Capital", font="Poppins 13 bold", fg="white", bg="#424769", command=update_letters)
c4.grid(row=2, column=1, sticky="e", padx=10, pady=5)

f_3b.pack()
f_3.pack(fill=X)

root.configure(bg="#424769")

root.mainloop()

