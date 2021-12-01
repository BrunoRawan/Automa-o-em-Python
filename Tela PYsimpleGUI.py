import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('FILTAR DE '), sg.Input(key='FILTRAR DE', size=(20, 1))],
    [sg.Text('           ATÉ'), sg.Input(key='ATÉ', size=(20, 1))],
    [sg.Text('           UNIDADE'), sg.Input(key='UNIDADE', size=(20, 1))],
    [sg.Button('Filtrar')]
]
window = sg.Window('Filtrar Agendamentos', layout)
while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break

