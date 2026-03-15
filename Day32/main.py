from tkinter import *
import pandas
import random

main_font = "Ariel",40,"italic"
down_font = "Ariel",60,"bold"
BACKGROUND_COLOR = "#B1E8CA"
#-----------------------------BACKEND------------------------
current_card= {}
to_learn ={}

try:
    data = pandas.read_csv("Day32/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day32/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    current_card = data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_front,image=front_c)
    flip_timer = window.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_front,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data =pandas.DataFrame(to_learn)
    data.to_csv("Day32/data/words_to_learn")
    next_card()




#-----------------------------------UI SetUP-----------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
front_c = PhotoImage(file="Day32/images/card_front.png")
card_back_img = PhotoImage(file="Day32/images/card_back.png")
canvas_front = canvas.create_image(400,263,image = front_c )
canvas.grid(row=0,column=0,columnspan=2)
card_title = canvas.create_text(400,150,text="",font=main_font)
card_word = canvas.create_text(400,263,text="",font=down_font)


wrong_image = PhotoImage(file="Day32/images/wrong.png")
button = Button(image=wrong_image,highlightthickness=0,command=next_card)
button.grid(row=1,column=0)

new_image = PhotoImage(file="Day32/images/right.png")
button = Button(image=new_image, highlightthickness=0,command=is_known)
button.grid(row=1,column=1)


next_card()



window.mainloop()