import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.title("States game")
image = "Day25&26&27/india_map_game/india_map.gif"
screen.addshape(image)
map_turtle = turtle.Turtle()
map_turtle.shape(image)
data = pandas.read_csv('Day25&26&27/india_map_game/map_coor.csv')
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 31:

    screen_input = screen.textinput(title=f"{len(guessed_states)}/30 State Correct",prompt="What's another state's name").title()

    if screen_input == "Exit" or len(guessed_states) > 31:
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day25&26&27/india_map_game/states_to_learn.csv")
        break

    if screen_input in all_states:
        guessed_states.append(screen_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == screen_input]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(screen_input)












