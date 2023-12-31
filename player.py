import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer, USEREVENT

root = Tk()
root.title("Simpli Music Player")
root.geometry("485x700+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()

current_track_index = 0

def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = [song for song in os.listdir(path) if song.endswith(".mp3")]
        Playlist.delete(0, END)
        for song in songs:
            Playlist.insert(END, song)

def play_music():
    global current_track_index
    if Playlist.size() > 0:
        mixer.music.load(Playlist.get(current_track_index))
        mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def next_track():
    global current_track_index
    stop_music()  # Stop the current playing music
    current_track_index = (current_track_index + 1) % Playlist.size()
    Playlist.selection_clear(0, END)
    Playlist.selection_set(current_track_index)
    play_music()

def prev_track():
    global current_track_index
    stop_music()
    current_track_index = (current_track_index - 1) % Playlist.size()
    Playlist.selection_clear(0, END)
    Playlist.selection_set(current_track_index)
    play_music()

def on_music_end(event):
    # When the music ends, play the next track
    next_track()

def volume_up():
    current_volume = mixer.music.get_volume()
    if current_volume < 1:
        mixer.music.set_volume(current_volume + 0.1)

def volume_down():
    current_volume = mixer.music.get_volume()
    if current_volume > 0:
        mixer.music.set_volume(current_volume - 0.1)

# Set an end event for the mixer
mixer.music.set_endevent(USEREVENT)

# Bind the end event to the function
root.bind(USEREVENT, on_music_end)

lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0, y=400)

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

frameCnt = 30
frames = [PhotoImage(file='aa1.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

Button(root, text="Play", command=play_music).place(x=150, y=487)
Button(root, text="Stop", command=stop_music).place(x=90, y=487)
Button(root, text="Next", command=next_track).place(x=20, y=487)
Button(root, text="Pause", command=pause_music).place(x=240, y=487)
Button(root, text="Unpause", command=unpause_music).place(x=300, y=487)
Button(root, text="Previous", command=prev_track).place(x=380, y=487)

# Volume control buttons
Button(root, text="Volume Up", command=volume_up).place(x=20, y=517)
Button(root, text="Volume Down", command=volume_down).place(x=120, y=517)

Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="Black", bg="#FFFFFF",
       command=add_music).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()
