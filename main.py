from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, columnspan=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, columnspan=1)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, columnspan=1)


# Entries
website_input = Entry()
website_input.config(width=41)
website_input.grid(row=1, column=1, columnspan=2, sticky="w")

username_input = Entry()
username_input.config(width=41)
username_input.grid(row=2, column=1, columnspan=1, sticky="w")

password_input = Entry(width=23)
password_input.grid(row=3, column=1, columnspan=1, sticky="w")


#Button
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=1,sticky="e")

add_button = Button(text="Add")
add_button.config(width=35)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()
