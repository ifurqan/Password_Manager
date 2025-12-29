from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', '3', 'K', 'L', 'M', 'N', '0', 'P', '0', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [f"{random.choice(letters)}{random.choice(symbols)}{random.choice(numbers)}" for char in range(random.randint(0, 4)) for char in range(random.randint(0, 4)) for char in range(random.randint(0, 4))]
    random.shuffle(password_list)
    mypassword = "".join(password_list)
    password_entry.insert(0,mypassword)
    pyperclip.copy(mypassword)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    search_query = web_entry.get()
    with open("Credentials.json","r") as file:
        data = json.load(file)
        try:
            messagebox.showinfo(title=search_query,message=f"Email : {data[search_query].get("email")}\nPassword : {data[search_query].get("password")}")
        except FileNotFoundError:
            messagebox.showinfo(title="Oops",message="No Data File Found")
        except KeyError:
            messagebox.showinfo(title="Oops",message="Account not found!\nCheck for spelling mistakes or write a different name.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    myemail = email_entry.get()
    mypass =  password_entry.get()
    new_data = {website:{"email": myemail,"password":mypass}}
    if len(website) < 1 or len(myemail) < 1 or len(mypass) < 1:
        messagebox.showinfo(title="Incomplete Credentials",message="kindly complete all the fields")
    else:
        is_ok = messagebox.askyesno(title=f"{website.capitalize()}",message=f"Do you want to save these credentials?\nEmail/Username: {myemail}\nPassword: {mypass}")
        if is_ok:
            try:
                with open("Credentials.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError or json.JSONDecodeError:
                with open("Credentials.json", "w") as file:
                    json.dump(new_data,file)
            else:
                data.update(new_data)
                with open("Credentials.json", "w") as file2:
                    json.dump(data,file2,indent=4)
    web_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    web_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1,column=1,columnspan=2)
search_button = Button(text="Search",width=15,command=search)
search_button.grid(row=1,column=3)
email = Label(text="Email/Username:")
email.grid(row=2,column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
password = Label(text="Password:")
password.grid(row=3,column=0)
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=1)
gen_button = Button(text="Generate Password",width=15,command=gen_pass)
gen_button.grid(row=3,column=3)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=3)
window.mainloop()
