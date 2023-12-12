import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

green = "green"
blue = "blue"
white = "white"
red = "red"
orange = "orange"
yellow = "yellow"

music_player = tkr.Tk()

music_player.title("^(-(oo)-)^")

music_player.geometry("600x400")

directory = askdirectory()

os.chdir(directory)

song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12", bg=white, selectmode = tkr.SINGLE)

for item in song_list:
    pos=0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

my_width = 5
my_height = 3

def play():
    pygame.mixer.music.load(play_list.get(tkr.active))
    song.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

button_play = tkr.Button(music_player, width = my_width, height = my_height, font = "Roboto", text = "Play", command=play, bg = green, fg = white)
button_stop = tkr.Button(music_player, width = my_width, height = my_height, font = "Roboto", text = "Stop", command=stop, bg = red, fg = white)
button_pause = tkr.Button(music_player, width = my_width, height = my_height, font = "Roboto", text = "Pause", command=pause, bg = yellow, fg = white)
button_unpause = tkr.Button(music_player, width = my_width, height = my_height, font = "Roboto", text = "Unpause", command=unpause, bg = orange, fg = white)

song = tkr.Stringvar()
song_title = tkr.Label(music_player, font="Roboto", textvariable=song)

song_title.pack()
button_play.pack(fill="x")
button_stop.pack(fill="x")
button_pause.pack(fill="x")
button_unpause.pack(fill="x")


music_player.mainloop()