import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Progress
from pytube import YouTube
from pytube.cli import on_progress


sg.theme('Reddit')


def Download(link, dir):
    youtube = YouTube(link, on_progress_callback=on_progress)
    video = youtube.streams.get_highest_resolution()
    video.download(f'/{dir or "Downloads"}')


layout = [
    [sg.Text('Coloque aqui o link:'), sg.InputText(key='link',)],
    [sg.Text('Escolha a pasta: '), sg.InputText(key='dir')],
    [sg.Button('Baixar')]
]

window = sg.Window('YoutubeDownloader', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'cancel'):
        break
    if event == 'Baixar':
        Download(values['link'], values['dir'])

window.close()
