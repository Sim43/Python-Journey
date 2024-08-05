from tkinter import *
import pandas
import json
import random
BACKGROUND_COLOR = "#B1DDC6"

curr_card = {}
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    odf = pandas.read_csv("data/french_words.csv")
    data_list = odf.to_dict(orient="records")
else:
    data_list = df.to_dict(orient="records")


def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(data_list)
    french_word = curr_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global curr_card
    english_word = curr_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_word, text=english_word, fill="white")


def is_known():
    data_list.remove(curr_card)
    words_to_learn = pandas.DataFrame(data_list)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, fill="black", text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)
next_card()

window.mainloop()
