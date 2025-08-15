import pandas
import turtle

screen=turtle.Screen()
screen.title("U.S. Game")
img='./blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

end_title=turtle.Turtle()
end_title.hideturtle()

answer_state_list=[]

while len(answer_state_list)<50:
    answer_state=screen.textinput(title=f'{len(answer_state_list)}/50 Guess the state',prompt='What\'s the state name ?')
    # print(answer_state_list)
    # Convert the entered state into TITLE case.
    answer_state=answer_state.title()
    # check if the entered state in 50 states


    # get file and read it
    data=pandas.read_csv('50_states.csv')
    full_states=data.state.to_list()
    # print(full_states)
    # print(data)
    if answer_state=='Exit':
        states_to_learn=[state for state in full_states if state not in answer_state_list]
        # states_to_learn=[]
        # for state in full_states:
        #     if state not in answer_state_list:
        #         states_to_learn.append(state)
        print(states_to_learn)
        learning_states=pandas.DataFrame(states_to_learn)
        learning_states.to_csv('states_to_learn.csv')
        break

    # get the column data with matched state

    guess_state=data[data['state']==answer_state]
    # print(guess_state)
    if len(guess_state)==0:
        continue
    # get X and Y from that data
    x=guess_state.x
    y=guess_state.y

    # print(x)
    # print(y)
    y_cors=y.iloc[0]
    x_cors=x.iloc[0]

    state_name=turtle.Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.goto(x_cors,y_cors)
    state_name.write(answer_state)


    # Record correct guesses into the list
    if answer_state not in answer_state_list:
        answer_state_list.append(answer_state)

    # keep track of score
end_title.write("GAME OVER")
end_title.goto(0,0)

# screen.exitonclick()