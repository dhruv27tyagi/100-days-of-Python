import pandas as pd 
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25 - States name challenge/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("Day 25 - States name challenge/50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="WHat's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())


