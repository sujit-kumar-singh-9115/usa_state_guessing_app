import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('u. s. states game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
df = pd.read_csv('50_states.csv')
all_states = df['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guessed state', prompt='What the next state name')
    answer_state = str(answer_state).title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
              missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("State_for_Learning")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df['state'] == answer_state]
        print(state_data)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




screen.exitonclick()

