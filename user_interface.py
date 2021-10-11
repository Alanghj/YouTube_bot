from tkinter import *
from tkinter import ttk
from bot.youtube import youtube_bot_path


def graphical_interface():

    # Style of display
    menu_initial = Tk()
    frm = ttk.Frame(menu_initial, padding=10)
    frm.grid()
    menu_initial.title("You_Play")
    menu_initial.geometry("155x150")
    menu_initial.iconbitmap('images/you_play.ico')

    # Button start
    cmd = Button(frm, text="Start Music", command=youtube_bot_path)
    cmd.grid(column=1, row=0)

    # Button end
    cmd2 = Button(frm, text="End Music", command=menu_initial.destroy)
    cmd2.grid(column=2, row=0)

    # Begin the user view
    menu_initial.mainloop()


if __name__ == "__main__":
    graphical_interface()
