from pathlib import Path

import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from customtkinter import CTkEntry
import os
import functions as f


def GUI():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("286x429")
    window.title("Calculator")
    window.configure(bg = "#1E1E1E")


    canvas = Canvas(
        window,
        bg = "#1E1E1E",
        height = 429,
        width = 286,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    entry_1 = CTkEntry(
        canvas,
        border_width=0,
        justify="right",
        fg_color="transparent",
        width=282.0,
        height=65.0,
        selectborderwidth=0,
        font = ("Courier New", 50)
    )
    entry_1.place(
        x=2.0,
        y=2.0,
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: f.equate_OP(entry_1),
        relief="flat"
    )
    button_1.place(
        x=216.0,
        y=287.0,
        width=70.0,
        height=142.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '%'),
        relief="flat"
    )
    button_2.place(
        x=144.0,
        y=359.0,
        width=70.0,
        height=70.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '0'),
        relief="flat"
    )
    button_3.place(
        x=72.0,
        y=359.0,
        width=70.0,
        height=70.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '.'),
        relief="flat"
    )
    button_4.place(
        x=0.0,
        y=359.0,
        width=70.0,
        height=70.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '3'),
        relief="flat"
    )
    button_5.place(
        x=144.0,
        y=287.0,
        width=70.0,
        height=70.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '2'),
        relief="flat"
    )
    button_6.place(
        x=72.0,
        y=287.0,
        width=70.0,
        height=70.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '1'),
        relief="flat"
    )
    button_7.place(
        x=0.0,
        y=287.0,
        width=70.0,
        height=70.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '+'),
        relief="flat"
    )
    button_8.place(
        x=216.0,
        y=215.0,
        width=70.0,
        height=70.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '6'),
        relief="flat"
    )
    button_9.place(
        x=144.0,
        y=215.0,
        width=70.0,
        height=70.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '5'),
        relief="flat"
    )
    button_10.place(
        x=72.0,
        y=215.0,
        width=70.0,
        height=70.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '4'),
        relief="flat"
    )
    button_11.place(
        x=0.0,
        y=215.0,
        width=70.0,
        height=70.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '-'),
        relief="flat"
    )
    button_12.place(
        x=216.0,
        y=143.0,
        width=70.0,
        height=70.0
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '9'),
        relief="flat"
    )
    button_13.place(
        x=144.0,
        y=143.0,
        width=70.0,
        height=70.0
    )

    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '8'),
        relief="flat"
    )
    button_14.place(
        x=72.0,
        y=143.0,
        width=70.0,
        height=70.0
    )

    button_image_15 = PhotoImage(
        file=relative_to_assets("button_15.png"))
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '7'),
        relief="flat"
    )
    button_15.place(
        x=0.0,
        y=143.0,
        width=70.0,
        height=70.0
    )

    button_image_16 = PhotoImage(
        file=relative_to_assets("button_16.png"))
    button_16 = Button(
        image=button_image_16,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.delete(len(entry_1.get())-1, tk.END),
        relief="flat"
    )
    button_16.place(
        x=216.0,
        y=71.0,
        width=70.0,
        height=70.0
    )

    button_image_17 = PhotoImage(
        file=relative_to_assets("button_17.png"))
    button_17 = Button(
        image=button_image_17,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, 'X'),
        relief="flat"
    )
    button_17.place(
        x=144.0,
        y=71.0,
        width=70.0,
        height=70.0
    )

    button_image_18 = PhotoImage(
        file=relative_to_assets("button_18.png"))
    button_18 = Button(
        image=button_image_18,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.insert(tk.END, '/'),
        relief="flat"
    )
    button_18.place(
        x=72.0,
        y=71.0,
        width=70.0,
        height=70.0
    )

    button_image_19 = PhotoImage(
        file=relative_to_assets("button_19.png"))
    button_19 = Button(
        image=button_image_19,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: entry_1.delete(0, tk.END),
        relief="flat"
    )
    button_19.place(
        x=0.0,
        y=71.0,
        width=70.0,
        height=70.0
    )
    window.resizable(False, False)
    window.mainloop()
    return window

if __name__ == "__main__":
    GUI()
