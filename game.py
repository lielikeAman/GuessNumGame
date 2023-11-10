import random
import PySimpleGUI as sg

graph_elem = None 

def show_message(message):
    sg.popup(message, title='Congratulations!', auto_close=True, auto_close_duration=3, non_blocking=True, modal=True)

def draw_color_indicator(graph_elem, guess, secret_number):
    diff = abs(secret_number - guess)
    color = 'green' if diff <= 10 else 'red'
    graph_elem.draw_rectangle((5, 5), (95, 95), fill_color=color, line_color='black')

def guess_the_number():
    global graph_elem 

    secret_number = random.randint(1, 100)
    attempts = 0

    layout = [
        [sg.Text("Guess the number from 1 to 100:")],
        [sg.InputText(key='input', focus=True)],
        [sg.Button('Guess', bind_return_key=True), sg.Button('Exit')],
        [sg.Graph(canvas_size=(100, 100), graph_bottom_left=(0, 100), graph_top_right=(100, 0), background_color='white', key='graph')],
        [sg.Text('', size=(20, 1), key='output')]
    ]

    window = sg.Window('Guess the Number', layout, element_justification='c')

    graph_elem = window['graph'] 

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        try:
            guess = int(values['input'])
            attempts += 1
            draw_color_indicator(graph_elem, guess, secret_number)

            if guess < secret_number:
                window['output'].update('The secret number is higher.')
            elif guess > secret_number:
                window['output'].update('The secret number is lower.')
            else:
                window['output'].update(f'Congratulations! You guessed the number {secret_number} in {attempts} attempts.')
                show_message(f'Congratulations! You guessed the number {secret_number} in {attempts} attempts.')
                break
        except ValueError:
            window['output'].update('Please enter an integer.')

    window.close()

if __name__ == "__main__":
    while True:
        guess_the_number()
