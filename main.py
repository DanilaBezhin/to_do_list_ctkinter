import customtkinter as ctk
from todo_list import TodoListApp

if __name__ == '__main__':
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    app = TodoListApp()
    app.mainloop()