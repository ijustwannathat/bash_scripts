# DOES NOT WORK FOR SOME WAYLAND POWERED GNOME 
# might not work for other systems like fedora, suggest you test that with with X11 running instead of wayland
# there is a workaround for running this script, but it requires writing extensive code which safety is unclear
# it would be cool if you were able to test that :D


import datetime
import os
import subprocess
from getpass import getpass
from time import sleep

user = getpass()
path = f'/home/{user}/.local/share/backgrounds/'

print('default background folder')
print(*os.listdir(path), sep='\n')


hours = int(datetime.datetime.now().time().strftime('%H'))

day_range = range(5, 19)
night_range = list(range(5))
night_range.extend(list(range(19, 24)))


def change_bg(file):
    '''This script wants to change background image based on a time of a day.
       To change background manually use (note, it may not work on gnome due to wayland restrictions): 
       gsettings set org.gnome.desktop.background picture-uri 'file:///home/<path_to_your_wallpaper>/<wallpaper>'
       NOTE: this script may not be the most optimal option out there.
    '''
    command = 'gsettings set org.gnome.desktop.background picture-uri'.split()
    command.append(path+file)
    subprocess.run(command)

#TODO: Make day_bg and night_bg env_variables
day_bg = '2025-07-02-20-37-46-ethan-dow-l7Wb6FXHIOQ-unsplash.jpg'
night_bg = ''
check_interval = 1

# this code needs to be run in while loop 
# since bashrc runs only on startup and we need to change bg based on time
while True:
    sleep((60*60)*check_interval)
    if hours in day_range:
        change_bg(day_bg)
    elif hours in night_range:
        change_bg(night_bg)
    



