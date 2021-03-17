#!/usr/bin/env python3

import os
import sys
import random
import multiprocessing
from playsound import playsound

def PlaySongs(path, repeat = 0, shuffle = False):

    # Create song list.
    try:
        # Create the list of files from a directory of songs.
        file_list = os.listdir(path)
        # Filter list to only include MP3 files.
        song_list = [i for i in file_list if i.endswith('.mp3')]
    except Exception as e:
        return str(e)

    # Initialize repeat counter.
    counter = 0
    play = True

    print('Press ENTER to skip')

    # Play all songs and repeat as necessary.
    while counter <= repeat and play == True:

        try:

            # Shuffle list if necessary.
            if shuffle is True:
                random.shuffle(song_list)

            # Play songs.
            for song in song_list:
                print('Playing: {}/{}...'.format(path, song))
                p = multiprocessing.Process(target=playsound, args = ('{}/{}'.format(path, song), ))
                p.start()
                # Skip to next song on Enter.
                input()
                p.terminate()
        
        # Stop playback on Ctrl+C.
        except KeyboardInterrupt:
            p.terminate()
            play = False
            return 'Stopped'
        
        except Exception as e:
            try:
                p.terminate()
            except:
                pass
            play = False
            return str(e)
        
        # Increment counter.
        counter += 1

    return 'Done'
