from tkinter import *
from tkinter import ttk
from bot.youtube import youtube_bot_path


def graphical_interface():

    # Style of display
    menu_initial = Tk()
    menu_initial.title("You_Play")
    menu_initial.geometry("160x150")
    menu_initial.iconbitmap('images/you_play.ico')

    # Style of button
    frm = ttk.Frame(menu_initial, padding=10)
    frm.grid()

    # Button start
    cmd = Button(frm, text="Start Music", command=youtube_bot_path)
    cmd.grid(column=0, row=1)

    # Button end
    cmd2 = Button(frm, text="End Music", command=menu_initial.destroy)
    cmd2.grid(column=1, row=1)


    # Begin the user view
    menu_initial.mainloop()


if __name__ == "__main__":
    graphical_interface()
