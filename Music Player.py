#biblioteca com as musicas
from playsound import playsound
#biblioteca do prirprio systema do Python
import os

#array/lista onde ficara o nome de todas as musicas no diretorio
all_musics = []

# Declara o caminho para a pasta/diretorio com as musicas
path =(r"")
#Colocar o path do diretorio/pasta que contenha as musicas
for x in os.listdir(path):
    all_musics.append(x)

#declarando o tamanho do array
music_lengh = len(all_musics)
#utilizando um for para ler quantas vezes ele sera executado pelo tamanho do array
for y in range(music_lengh):
    print(all_musics[x])

musica = input("Deseja tocar que musica: ")

#concatena o path com o nome da musica para dar o diretorio da musica
path_music = (path +"\ "+ musica )

#função de tocar musica da biblioteca playsound
playsound(path_music)