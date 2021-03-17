==============
**PlaySongs**
==============

Overview
--------

Play MP3s from a specified directory.

Prerequisites
-------------

- *Python >= 3.6*
- *playsound >= 1.2.2* (installed as a dependency)
- *pyobjc >+ 7.1* (installed as a dependency)
- **CAVEAT**: Due to *playsound* limitations, directory and filenames with spaces are not allowed.

Required (Positional) Arguments
-------------------------------

- Position 1: /path/to/mp3/files

Optional (Keyword) Arguments
----------------------------

- repeat
    - Description: Number of times to repeat the whole collection.
    - Type: Integer
    - Default: 0
- shuffle
    - Description: Select whether to shuffle the list of songs being played.
    - Type: Boolean
    - Default: False

Usage
-----

Installation:

.. code-block:: BASH

   pip3 install playsongs
   # or
   python3 -m pip install playsongs

In Python3:

.. code-block:: BASH

   from playsongs.playsongs import PlaySongs
   PlaySongs('/home/username/Music', repeat = 10000000, shuffle = True)

In BASH:

.. code-block:: BASH

   python3 -c "from playsongs.playsongs import PlaySongs; PlaySongs('/home/username/Music', repeat = 10000000, shuffle = True)"

Changelog
---------

2021.1.3.0

- Used *multiprocessing* to start *playsound* to enable skipping and non-Python-killing keyboard interrupt.

2021.1.2.0

- Added pyobcj as a dependency.
- Reverted keyboard interrupt to exit as return doesn't actually stop playbacks.

2021.1.0.7

- Moved build and publish process to GitHub Actions.

2021.1.0.6

- Updated README.

2021.1.0.5

- Updated code to return instead of exit in case of exceptions.

2021.1.0.4

- Updated typo in README (this file).
- No code change.

2021.1.0.3

- Removed system exit at the end of the playlist so it won't kill Python runtime.
- CTRL+C will still kill Python runtime.

2021.1.0.1

- Initial release.

*Current version: 2021.1.3.0*
