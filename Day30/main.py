from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    #Hard level - Order of characters randomised:
    password_letters=[choice(letters) for char in range(randint(8,10))]
    password_symbols=[choice(numbers) for num in range(randint(2,4))]
    password_numbers=[choice(symbols) for sym in range(randint(2,4))] 

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_ = "".join(password_list)
    t_text_entry.insert(0,password_)
    pyperclip.copy(password_)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    key = f_text_entry.get()
    try:
        with open("Day30/data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if key in data:
            email = data[key]["email"]
            password = data[key]["password"]
            messagebox.showinfo(title={f_text_entry},message=f"Email : {email},\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {f_text_entry} exists.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def submit():
    website = f_text_entry.get()
    email = s_text_entry.get()
    password = t_text_entry.get()
    new_data = {
        website:{
            "email" : email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("Day30/data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Day30/data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("Day30/data.json","w") as data_file:
                json.dump(data,data_file,indent=4)    
        finally:
            f_text_entry.delete(0,END)
            s_text_entry.delete(0,END)
            t_text_entry.delete(0,END)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_ = PhotoImage(file="Day30/logo.png")
canvas.create_image(100,100,image = logo_)
canvas.grid(row=0,column=1)

#Labels
f_text = Label(text="Website:")
f_text.grid(row=1,column=0)
s_text=Label(text="Email/Username:")
s_text.grid(row=2,column=0)
t_text = Label(text="Password:")
t_text.grid(row=3,column=0)

#Entries
f_text_entry = Entry(width=37)
f_text_entry.grid(row=1,column=1)

f_text_entry.focus()
s_text_entry = Entry(width=55)
s_text_entry.grid(row=2,column=1,columnspan=2)
s_text_entry.insert(0,"example123@gmail.com")
t_text_entry = Entry(width=37)
t_text_entry.grid(row=3,column=1)

Gp_button = Button(text="Generate Password",command=generate_password)
Gp_button.grid(row=3,column=2)
search_button = Button(text="Search",width=14,command=find_password)
search_button.grid(row=1,column=2)
add_button = Button(text="Add",width=47,command=submit)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()