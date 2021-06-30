import PySimpleGUI as gui
import os
from playsound import playsound





musicas = []

path = (r'C:\Users\8864-adm\Desktop\Dani\Musicas')

for x in os.listdir(path):
    musicas.append(x)

tamanho_music = len(musicas)

for y in range(tamanho_music):
    print("As musicas são: " + musicas[y])

nome_musica = input(r"Escreva o nome da Musica que você deseja Tocar: ")

nome_total = ("{}\{}".format(path , nome_musica))

print(nome_total)

playsound(nome_total)