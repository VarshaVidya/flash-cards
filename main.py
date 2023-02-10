
BACKGROUND_COLOR = "#B1DDC6"
FONT=("Ariel",40,"italic")
import pandas
import random
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError :
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')
current_card={}

def next_card():
    global current_card,timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(background_img, image=card_front_image)
    canvas.itemconfig(card_title,text="French",fill="Black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="Black")
    timer = window.after(3000, func=eng_card)
def eng_card():
    canvas.itemconfig(background_img,image=card_back)
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(card_word,text=current_card["English"],fill="White")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()
from tkinter import *
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer=window.after(3000,func=eng_card)
canvas = Canvas(width=800,height=526,bg =BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
#card back

card_back = PhotoImage(file="images/card_back.png")

# card_front
card_front_image= PhotoImage(file="images/card_front.png")
background_img =canvas.create_image(400,263,image = card_front_image)

#wrong_button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

#right_button
#alignment is still not right
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

# fonts
card_title = canvas.create_text(400,150,text="Title",font=FONT)

card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
next_card()
#english translation

window.mainloop()
