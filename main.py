from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(letters) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear():
    website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oooops",
            message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"There are the details entered: "
                    f"\nEmail{email} "
                    f"\nPassword: {password} "
                    f"\nIs it ok to save? "
        )
        if is_ok:
            try:
                with open("data.txt", "a") as datafile:
                    datafile.write(f"{website} | {email} | {password}\n")
                clear()
            except Exception as e:
                print(f"An exception occurred {e}")


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
website_entry = Entry()
website_entry.config(width=41)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry()
email_entry.config(width=41)
email_entry.grid(row=2, column=1, columnspan=1, sticky="w")
email_entry.insert(0, "krm.sp.08@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, columnspan=1, sticky="w")

#Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=1, sticky="e")

add_button = Button(text="Add")
add_button.config(width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
