# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas

canvas = Canvas(width=200, height=200)


key_img = PhotoImage(file="key.png")
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

enter_username = Entry(width=35)
enter_username.grid(row=4, column=2, columnspan=2)

enter_password = Entry(width=17)
enter_password.grid(row=5, column=2)
# buttons
button_generate = Button(text="Generate Password")
button_generate.grid(row=5, column=3)

button_add = Button(text="Add", width=44)
button_add.grid(row=6, column=2, columnspan=2)


window.mainloop()
