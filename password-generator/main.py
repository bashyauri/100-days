import json
import os
from random import *
from tkinter import *
import pyperclip
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    letters = [choice(letters) for _ in range(1, nr_letters + 1)]
    symbols = [choice(symbols) for _ in range(1, nr_symbols+1)]
    numbers = [choice(numbers) for _ in range(1, nr_numbers + 1)]

    password_list = letters + symbols + numbers
    shuffle(password_list)
    password = "".join(password_list)

    enter_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_empty(*kwargs):
    for k in kwargs:
        if len(k) == 0:
            return True
        return False


def find_password():
    website = enter_website.get().title()
    is_empty = check_empty(website)
    if is_empty:
        messagebox.showerror(
            title="Oops", message="One of the fields is empty")
    else:
        try:
            with open(os.path.join(path, "password-generator", "data.json"), 'r') as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showinfo(title="Info", message="No Data file found")
        else:
            try:
                website_details = data[website]

            except KeyError:
                messagebox.showinfo(
                    title="Info", message="No details for the website exist ")

            else:
                messagebox.showinfo(
                    title="Info", message=f"website:{website}\nPassword:{website_details['password']}")
                pyperclip.copy(website_details['password'])


def save_password():
    website = enter_website.get().title()
    password = enter_password.get()
    email = enter_username.get()

    new_data = {website: {
        "email": email,
        "password": password,
    }}
    is_empty = check_empty(website, password, email)
    if is_empty:
        messagebox.showerror(
            title="Oops", message="One of the fields is empty")
    else:
        try:
            with open(os.path.join(path, "password-generator", "data.json"), 'r') as f:
                # Reading old data
                data = json.load(f)

        except FileNotFoundError:
            with open(os.path.join(path, "password-generator", "data.json"), 'w') as f:
               # Saving the updated data
                json.dump(new_data, f, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open(os.path.join(path, "password-generator", "data.json"), 'w') as f:
                # Saving the updated data
                json.dump(data, f, indent=4)
        finally:
            enter_website.delete(0, END)
            enter_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas

canvas = Canvas(width=200, height=200)

path = os.getcwd()
key_img = PhotoImage(file=os.path.join(path, "password-generator", "key.png"))
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=2, column=2)
# label
website_label = Label(text="Website:")
website_label.grid(row=3, column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=4, column=1)


password_label = Label(text="Password:")
password_label.grid(row=5, column=1)
# Enter
enter_website = Entry(width=35)
enter_website.grid(row=3, column=2, columnspan=2)
enter_website.focus()

enter_username = Entry(width=35)
enter_username.grid(row=4, column=2, columnspan=2)
enter_username.insert(0, "basharu83@gmail.com")

enter_password = Entry(width=17)
enter_password.grid(row=5, column=2)
# buttons
button_search = Button(text="Search", width=10, command=find_password)
button_search.grid(row=3, column=5)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=5, column=3)


button_add = Button(text="Add", width=44, command=save_password)
button_add.grid(row=6, column=2, columnspan=2)


window.mainloop()
