#a program that will make user to take a break after every two hour by playing his fav song

import time
import webbrowser

#replace thhe link with your fav song
favSong = 'https://www.youtube.com/watch?v=-S1IhJ_DHjw'
totalBreaks = 3
counter = 0

print("The program is running from "+ time.ctime())
while (counter < totalBreaks):
    time.sleep(2*60*60)
    webbrowser.open(favSong)
    counter += 1