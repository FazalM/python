from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle


def save_to_file():
    get_username = username_entry.get()
    get_email = email_entry.get()
    get_password = auto_generate_password_entry.get()

    if get_password != "" and get_email != "" and get_password != "":

        accept = messagebox.askokcancel(title="save to file", message=f"Your data is about to be saved.\n Your username is {get_username} \n Your email is {get_email} \n Your password is {get_password}")
        if accept == True:
            with open("save_data", "a") as save_file:
                save_file.write(f"{get_username} | {get_email} | {get_password}\n")       
    else:
        messagebox.showerror(title="Error", message="Some fields are empty")

def password_geenrator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    auto_generate_password_entry.delete(0,END)
    auto_generate_password_entry.insert(0, password)

window = Tk()
window.minsize(width=750, height=600)
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(height=300, width=300)
image_one = PhotoImage(file="logo.png")
canvas.create_image(200,200, image=image_one)
canvas.grid(column=1, row=0)

username_label = Label()
username_label.config(text="Website:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=48)
username_entry.grid(column=1, row=2, columnspan=2)

email_label = Label()
email_label.config(text="Email:")
email_label.grid(column=0, row=3)

email_entry = Entry(width=48)
email_entry.insert(END,"test@gmail.com")
email_entry.grid(column=1, row=3, columnspan=2)

auto_generate_password_label = Label()
auto_generate_password_label.config(text="Generated Password:")
auto_generate_password_label.grid(column=0, row=4)

auto_generate_password_entry = Entry(width=34)
auto_generate_password_entry.grid(column=1, row=4)

auto_generate_password_button = Button(width=10, text="Generate", command=password_geenrator)
auto_generate_password_button.grid(column=2,row=4)

add_button = Button(text="Save", width=10, command=save_to_file)
add_button.grid(column=2, row=5, columnspan=2)



window.mainloop()
