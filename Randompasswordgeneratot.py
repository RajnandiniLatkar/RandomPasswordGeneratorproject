from tkinter import*
import string
import random
import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    password=random.sample(all,password_length)
    passwordField.insert(0,password)


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

    
root=Tk()
root.config(bg="gray20")
choice=IntVar()
font=("arial",13,"bold")

passwordLabel=Label(root,text="Password Genreator",font=("times new roman",20,"bold"),bg="gray20")
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root,text="Weak",value=1,variable=choice)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text="Medium",value=2,variable=choice)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text="Strong",value=3,variable=choice)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text="Password Length",font=font,bg="gray20",fg="white")
lengthLabel.grid()

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=font)
length_Box.grid()

generateButton=Button(root,text="Generate",font=font,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=font)
passwordField.grid()

copyButton=Button(root,text="Copy",font=font,command=copy)
copyButton.grid(pady=5)

root.mainloop()
