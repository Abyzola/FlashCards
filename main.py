from tkinter import messagebox
from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# I want to add more features here like for example... it should be able to select the language you want to learn

# Spanish or French and also change the graphics
# Also inform the user the total number of word they've learnt so far using a messagebox
# And also inform the user how many words they've learnt in a row without missing with a messagbox pop up


# ------------------------------ RIGHT OR WRONG FUNCTION ---------------------------------

# Because there is no word_to_learn file when you first run the code
try:
    # Reading the csv files with pandas
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # Converting the csv file to a dictionary
    to_learn = data.to_dict(orient="records")

# Removing know words from to_learn dict


def is_known():
    to_learn.remove(current_card)
    dataa = pandas.DataFrame(to_learn)
    dataa.to_csv("data/words_to_learn.csv", index=False)
    length = len(dataa)
    learnt = 107 - length
    if learnt % 10 == 0:
        messagebox.showinfo(title="Congratulations", message=f"You have successfully learnt {learnt} words")
    right()


# records is a parameter for the keyword orient and what it does is to make your many row
# and columned dictionary readable so you could read it line by line (dictionaries inside a list)
# print(to_learn)


def right():
    global current_card, flip_timer
    flash_card.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(title, text="Spanish", fill="black")
    canvas.itemconfig(word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    flip_timer = flash_card.after(3000, func=switch)
#
# def french():
#     global current_card, flip_timer
#     flash_card.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     # print(current_card["French"])
#     canvas.itemconfig(title, text="French", fill="blue")
#     canvas.itemconfig(word, text=current_card["French"], fill="blue")
#     canvas.itemconfig(canvas_image, image=front_card)
#     flip_timer = flash_card.after(3000, func=switch)

# ------------------------------ DELAY AND SWITCH ---------------------------------
# Grammatically: While 3 seconds of showing French word call  on the switch function
def switch():
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(title, fill="red", text="English")
    canvas.itemconfig(word, fill="gold", text=current_card["English"])
   # messagebox.askyesno(Title="French or Spanish", message="What would you like to learn?")

# ------------------------------ UI SETUP ---------------------------------

flash_card = Tk()
flash_card.title("Flashy")
flash_card.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = flash_card.after(3000, func=switch)

canvas = Canvas(height=526, width=800)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=right)
wrong_button.grid(row=1, column=0)

title = canvas.create_text(400, 150, text="Title", font=["Ariel", 40, "italic"])
word = canvas.create_text(400, 263, text="Word", font=["Ariel", 60, "bold"])
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# spanish_label = Label(text="Spanish", font=["Ariel", 40, "italic"], bg="white")
# spanish_label.place(x=300, y=150)
# word_label = Label(text="Word", font=["Ariel", 60, "bold"], bg="white")
# word_label.place(x=300, y=263)

# Calling the right function so it does not show the title and word placeholders when the code is ran
right()


flash_card.mainloop()
