import tkinter as tk


def add():
    pass









window = tk.Tk()
window.title('Калькулятор =')
window.geometry('350x350')
window.resizable(False, False)

button_add = tk.Button(window, text='+', width=3, height=3)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=3, height=3)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width=3, height=3)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/', width=3, height=3)
button_div.place(x=250, y=200)

number1_entry = tk.Entry(window, width=32)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=32)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=32)
answer_entry.place(x=100, y=300)

number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=100, y=125)
number3 = tk.Label(window, text='Ответ')
number3.place(x=100, y=275)
window.mainloop()
