import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.setup(700, 450)
screen.title("U.S. States Game")
turtle.hideturtle()
image = "blank_states_img.gif"
screen.bgpic(image)

'''
For finding the coordinates
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
'''
guesses = []

while len(guesses) < 50:
    answer_state = screen.textinput(
        title=f"{len(guesses)}/50 States Correct",
        prompt="What's another state's name? "
    )

    if not answer_state:
        break  # exit the game if Cancel is pressed

    answer_state = answer_state.strip().title()

    count = 0
    for i in data["state"]:
        if answer_state != i:
            count += 1
        else:
            if answer_state in guesses:
                print("You've already guessed this.")
                continue  # skip if already guessed

            x_cordinates, y_cordinates = data["x"][count], data["y"][count]
            turtle.penup()
            turtle.goto(x_cordinates, y_cordinates)
            turtle.write(answer_state)
            guesses.append(answer_state)
            score = len(guesses)
            break  # stop searching once match is found

# --- Save the states you missed into a CSV ---
missing_states = [state for state in data["state"] if state not in guesses]
pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")

screen.exitonclick()
