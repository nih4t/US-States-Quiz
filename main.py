import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Quiz")

screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

turtle.hideturtle()
turtle.penup()
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_answers:
                missing_states.append(state)
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in states and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        state_data = data[data.state == answer_state]
        turtle.goto(state_data.x.item(), state_data.y.item())
        turtle.write(answer_state)



