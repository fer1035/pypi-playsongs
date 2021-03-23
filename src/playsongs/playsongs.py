#!/usr/bin/env python3

import os
import sys
import re
import random
import multiprocessing
from playsound import playsound

def PlaySongs(path, repeat = 0, shuffle = False):

    # Create song list.
    try:
        # Create the list of files from a directory of songs.
        file_list = os.listdir(path)
        # Filter list to only include MP3 files.
        song_list = ['{}/{}'.format(path, i) for i in file_list if i.endswith('.mp3')]
    except Exception as e:
        return str(e)

    # Initialize repeat counter.
    counter = 0
    play = True

    print('Press CTRL+C for options')

    # Play all songs and repeat as necessary.
    while counter <= repeat and play == True:

        try:

            # Shuffle list if necessary.
            if shuffle is True:
                random.shuffle(song_list)

            # Play songs.
            for song in song_list:
                print('Playing: {}...'.format(song))
                # Start playing.
                p = multiprocessing.Process(target = playsound, args = (song, ))
                p.start()
                try:
                    while True:
                        if p.exitcode != None:
                            p.terminate()
                            break
                # Invoke controls.
                except KeyboardInterrupt:
                    p.terminate()
                    control = input('Skip() or Exit(x): ')
                    if control == 'x' or control == 'X':
                        p.terminate()
                        play = False
                        return 'Stopped'
                    else:
                        pass
                except Exception as e:
                    p.terminate()
                    play = False
                    return str(e)
        
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
