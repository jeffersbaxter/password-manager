from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

from default import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_text = website_input.get()
    email_text = email_input.get()
    password_text = password_input.get()
    print(website_text == "")
    if website_text == "" or email_text == "" or password_text == "":
        messagebox.showinfo(message="Please don't leave any fields empty!")
        return

    validation_msg = f"These are the details entered: \nEmail: {email_text}\nPassword: {password_text}\n Is it OK to save?"
    is_ok = messagebox.askokcancel(title=website_text, message=validation_msg)

    if is_ok:
        with open("data.txt", "a") as data:
            data.write(f"{website_text} | {email_text} | {password_text}\n")
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=35)
email_input.insert(0, EMAIL)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_psw_btn = Button(text="Generate Password", command=generate_password)
generate_psw_btn.grid(row=3, column=2)

add_psw_btn = Button(text="Add", width=36, command=save)
add_psw_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
