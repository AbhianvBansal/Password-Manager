from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    no = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '/', '?', ',']

    pass_letter = [choice(letter) for _ in range(randint(8, 10))]
    pass_sym = [choice(symbol) for _ in range(randint(2, 4))]
    pass_no = [choice(no) for _ in range(randint(2, 4))]

    pass_lst = pass_no + pass_letter + pass_sym
    shuffle(pass_lst)

    final_pass = "".join(pass_lst)
    pass_txt_box.insert(0, final_pass)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_txt_box.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email:"]
            password = data[website]["password:"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_data = web_txt_box.get()
    email_data = email_txt_box.get()
    pass_data = pass_txt_box.get()
    new_data = {
        web_data: {
            "email:": email_data,
            "password:": pass_data,
        }
    }
    if len(web_data) == 0 or len(email_data) == 0 or len(pass_data) == 0:
        messagebox.showinfo(title="Oops!", message="Please Fill the Empty fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            web_txt_box.delete(0, END)
            pass_txt_box.delete(0, END)
            web_txt_box.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# creating canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# input website name
web_txt = Label(text="Website:")
web_txt.grid(row=1, column=0)

web_txt_box = Entry(width=33)
web_txt_box.focus()
web_txt_box.grid(row=1, column=1)

# input email or username
email_txt = Label(text="Email/Username:")
email_txt.grid(row=2, column=0)

email_txt_box = Entry(width=52)
email_txt_box.insert(0, "abhinavbansal12@gmail.com")
email_txt_box.grid(row=2, column=1, columnspan=2)

# input the password
pass_txt = Label(text="Password:")
pass_txt.grid(row=3, column=0)

pass_txt_box = Entry(width=33)
pass_txt_box.grid(row=3, column=1)

# generating password
gen_pass = Button(text="Generate Password", width=15, command=gen_password)
gen_pass.grid(row=3, column=2)

# search button for searching if a particular website is stored or not
search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)
 
# add or saving the password
add = Button(text="Add", width=44, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
