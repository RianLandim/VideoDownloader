import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Coloque aqui o link:'), sg.InputText()],
    [sg.Button('Baixar')]
]

window = sg.Window('YoutubeDownloader', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'cancel'):
        break

window.close()
