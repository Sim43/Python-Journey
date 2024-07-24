import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=750, height=600)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_description = data[data.state == answer_state]
        state_pos = (state_description.x.item(), state_description.y.item())
        t.goto(state_pos)
        t.write(answer_state)
        guessed_states.append(answer_state)
        all_states.remove(answer_state)

new_data = pandas.Series(all_states)
new_data.to_csv("states_to_learn.csv")

turtle.mainloop()
