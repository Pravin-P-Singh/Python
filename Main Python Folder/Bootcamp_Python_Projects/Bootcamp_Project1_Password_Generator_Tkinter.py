#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import string
import random

# function to generate password
def generate_password():
    length=int(length_entry.get())
    uppercase=uppercase_var.get()
    lowercase=lowercase_var.get()
    digits=digits_var.get()
    symbols=symbols_var.get()
    
    # define the character sets
    uppercase_letters=string.ascii_uppercase
    lowercase_letters=string.ascii_lowercase
    digits_characters=string.digits
    symbols_characters=string.punctuation
    
    # create the character set for password
    password_characters=' '
    if uppercase:
        password_characters+=uppercase_letters
    if lowercase:
        password_characters+=lowercase_letters
    if digits:
        password_characters+=digits_characters
    if symbols:
        password_characters+=symbols_characters
    
    # generate the password
    password="".join(random.choice(password_characters) for i in range(length))
    
    # display the password
    password_label.config(text=password)

# Create the GUI
root = tk.Tk()
root.title("Password Generator")

# Create the widgets
length_label = tk.Label(root,text="Password length : ")
length_entry=tk.Entry(root)
uppercase_var=tk.BooleanVar()
uppercase_checkbutton=tk.Checkbutton(root,text="Uppercase",variable=uppercase_var)
lowercase_var=tk.BooleanVar()
lowercase_checkbutton=tk.Checkbutton(root,text="Lowercase",variable=lowercase_var)
digits_var=tk.BooleanVar()
digits_checkbutton=tk.Checkbutton(root,text="Digits",variable=digits_var)
symbols_var=tk.BooleanVar()
symbols_checkbutton=tk.Checkbutton(root,text="Symbols",variable=symbols_var)
generate_button=tk.Button(root,text="Generate Password",command=generate_password)
password_label=tk.Label(root,text="")

# Grid the widgets
length_label.grid(row=0,column=0)
length_entry.grid(row=0,column=1)
uppercase_checkbutton.grid(row=1,column=0)
lowercase_checkbutton.grid(row=2,column=0)
digits_checkbutton.grid(row=3,column=0)
symbols_checkbutton.grid(row=4,column=0)
generate_button.grid(row=5,column=0)
password_label.grid(row=6,column=0)

#start the GUI
root.mainloop() 


# In[ ]:




