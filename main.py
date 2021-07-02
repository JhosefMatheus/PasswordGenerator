from tkinter import *
import PasswordGenerator

passwordGenerator = PasswordGenerator.PasswordGenerator()

window = Tk()

window['bg'] = '#808080'

w = 300
h = 300

w_screen = window.winfo_screenwidth()
h_screen = window.winfo_screenheight()

position_x = int(w_screen/2) - int(w/2)
position_y = int(h_screen/2) - int(h/2)

window.geometry(f'{w}x{h}+{position_x}+{position_y}')
window.resizable(False, False)

label_password = Label(
    window,
    text='Senha:',
    font='Arial 12',
    background='#808080'
).place(x=125, y=100)

label_show_password = Label(
    window,
    font='Arial 12',
    width=25
)

label_show_password.place(x=35, y=125)

button_password_generator = Button(
    window,
    text='Gerar Senha',
    command=lambda:passwordGenerator.generate_password(label_show_password)
).place(x=115, y=155)

button_copy = Button(
    window,
    text='Copiar',
    command=lambda:passwordGenerator.copy_password(label_show_password)
).place(x=130, y=185)

window.mainloop()
