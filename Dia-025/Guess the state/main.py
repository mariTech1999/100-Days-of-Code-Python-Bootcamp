import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
states_count = 0
guess_state = []
while states_count<50:
    answer_state = screen.textinput(title=f"{states_count}/50 States Correct", prompt="Enter a state: ").title()

    if answer_state == 'Exit':
        study_state = []

        for state in all_states:
            if state not in guess_state:
                study_state.append(state)
        df = pd.DataFrame(study_state)
        df.to_csv("states_study.csv")
        break

    if answer_state in all_states:
        if answer_state not in guess_state:
            state_data = data[data.state == answer_state]
            guess_state.append(answer_state)
            x_cor = int(state_data.x.item())
            y_cor = int(state_data.y.item())
            state = turtle.Turtle()
            state.hideturtle()
            state.penup()
            state.goto(x_cor,y_cor)
            state.write(answer_state,align="center",font=("Arial",8,"bold"))
            states_count += 1


turtle.mainloop()