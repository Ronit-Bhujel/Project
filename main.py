
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
# import sqlite3



root = Tk()
# root.state('zoomed')
root.geometry('1277x746')
root.resizable(False,False)
root.title('Library Management System')
# my_image = Image.open("book.jpg")
# resized_image = my_image.resize((1277,746))
# converted_image = ImageTk.PhotoImage(resized_image)
# mylabel = Label(root, image=converted_image)
# mylabel.pack()

# conn = sqlite3.connect('database.db')
# c = conn.cursor()

# c.execute(""" CREATE TABLE user(
#     username text,
#     password text
# )""")
# print('Tabel created successfully')

# def submit():
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO user VALUES (:username, :password)",{
#         'username':user_entry.get(),
#         'password':psw_entry.get(),
#     })

#     messagebox.showinfo("user", "Inserted Successfully")
#     conn.commit()
#     conn.close()

#     user_entry.delete(0,END)
#     psw_entry.delete(0,END)

def login_acc():
    login_frame.pack(fill=BOTH, expand=1)
    register_frame.forget()


def register_acc():
    register_frame.pack(fill='both', expand=1)
    login_frame.forget()


frame = Frame(root)
register_frame = (root)
frame.pack(fill='both', expand=1)
login_frame = Frame(frame)
login_frame.configure(height=1277, width=746)
login_frame.pack(side=LEFT)

my_image = Image.open("book.jpg")
resized_image = my_image.resize((1277,746))
converted_image = ImageTk.PhotoImage(resized_image)
mylabel = Label(login_frame, image=converted_image)
mylabel.pack()


log = Label(login_frame, text="Log In", font="arial 40 bold")
log.place(x=550,y=10)

user_entry = Entry(login_frame, font=15, width=23, borderwidth=2)
user_entry.place(x=500, y=250)
user_entry.insert(0, 'Username')

psw_entry = Entry(login_frame, font=15, width=23, borderwidth=2)
psw_entry.place(x=500, y=330)
psw_entry.insert(0, 'Password')

log_btn = Button(login_frame, text="Log In", font=5, width=10, bd=0)
log_btn.place(x=575, y=400)


def on_click(event):
    user_entry.configure(state=NORMAL)
    user_entry.delete(0, END)

on_click_id = user_entry.bind('<Button-1>', on_click)

def on_click(event):
    psw_entry.configure(state=NORMAL)
    psw_entry.configure(show='*')
    psw_entry.delete(0, END)

on_click_id = psw_entry.bind('<Button-1>', on_click)

forgot_password_button = Button(login_frame, text='Forgot Password?', bd=0, cursor='hand2')
forgot_password_button.place(x=583, y=440)

text_label = Button(login_frame, text="Don't have an account, Signup", font=7, bd=0, command=register_acc)
text_label.place(x=535, y=520)

register_submit_frame = Frame(register_frame)
register_submit_frame.configure(height=1277, width=746)
register_submit_frame.pack(side=LEFT)


sign = Label(register_submit_frame, text="Sign Up Form", font="arial 40 bold")
sign.place(x=450,y=10)

f_name_label = Label(register_submit_frame, text="First Name", font="arial 15 bold")
f_name_label.place(x=80,y=170)
f_name_entry = Text(register_submit_frame, font=15, width=25, height=1, borderwidth=2)
f_name_entry.place(x=80, y=200)

user_name_label = Label(register_submit_frame, text="Username", font="arial 15 bold")
user_name_label.place(x=80,y=280)
user_name_entry = Text(register_submit_frame, font=15, width=25, height=1, borderwidth=2)
user_name_entry.place(x=80, y=310)

password_label = Label(register_submit_frame, text="Password", font="arial 15 bold")
password_label.place(x=80,y=390)
password_entry = Text(register_submit_frame, font=15, width=25, height=1, borderwidth=2)
password_entry.place(x=80, y=420)

l_name_label = Label(register_submit_frame, text="Last Name", font="arial 15 bold")
l_name_label.place(x=870,y=170)
l_name_entry = Text(register_submit_frame, font=15, width=25, height=1, borderwidth=2)
l_name_entry.place(x=870, y=200)

email_label = Label(register_submit_frame, text="E-mail", font="arial 15 bold")
email_label.place(x=870,y=280)
email_entry = Text(register_submit_frame, font=15, width=25, height=1, borderwidth=2)
email_entry.place(x=870, y=310)

conf_password_label = Label(register_submit_frame, text="Confirm Password", font="arial 15 bold")
conf_password_label.place(x=870,y=390)
conf_password_entry = Text(register_submit_frame, font=15, width=25, height=1, borderwidth=2)
conf_password_entry.place(x=870, y=420)

checkButton = Checkbutton(register_submit_frame, text="Accept to all terms and conditions.", font=5, onvalue="On", offvalue="Off")
checkButton.place(x=450, y=550)

sign_up = Button(register_submit_frame, text="Sign Up", font=5)
sign_up.place(x=570, y=600)

label_log = Button(register_submit_frame, text='Already have an account? Login', bd=0, cursor='hand2', command=login_acc)
label_log.place(x=530, y=650)


# conn.commit()
# conn.close()

root.mainloop()



