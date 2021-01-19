import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=720, height=500)
screen.title("Guess U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_state = turtle.Turtle()
us_state.hideturtle()
us_state.penup()


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # states to learn.csv
        learn_state = []
        for state in states:
            if state not in guessed_states:
                learn_state.append(state)

        df = pandas.DataFrame(learn_state)
        df.to_csv("state_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        guess_state_data = data[data.state == answer_state]
        x_coordinates = guess_state_data.x.item()
        y_coordinates = guess_state_data.y.item()
        us_state.setposition(x_coordinates, y_coordinates)
        us_state.write(answer_state, align="center", font=("Arial", 8, "normal"))



# screen.exitonclick()