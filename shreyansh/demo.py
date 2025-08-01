# from asciimatics.effects import Matrix, Stars, Cycle
# from asciimatics.renderers import FigletText
# from asciimatics.scene import Scene
# from asciimatics.screen import Screen

# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("Gaurav", font='big'),
#             int(screen.height / 2 - 8)),
#         Cycle(
#             screen,
#             FigletText("Singh Vashistha!", font='small'),
#             int(screen.height / 2 + 3)),
#         Stars(screen, 200)
#     ]
#     screen.play([Scene(effects, 500)])

# Screen.wrapper(demo)

# from asciimatics.screen import Screen
# from asciimatics.scene import Scene
# from asciimatics.effects import Cycle, Stars
# from asciimatics.renderers import FigletText

# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("ASCIIMATICS", font='big'),
#             screen.height // 2 - 8),
#         Cycle(
#             screen,
#             FigletText("ROCKS!", font='big'),
#             screen.height // 2 + 3),
#         Stars(screen, (screen.width + screen.height) // 2)
#     ]
#     screen.play([Scene(effects, 500)])

# Screen.wrapper(demo)

# from random import randint
# from asciimatics.screen import Screen

# def hello(screen: Screen):
#     while True:
#         screen.print_at("Hello from ASCIIMatics",
#                         randint(0, screen.width), randint(0, screen.height),
#                         colour=randint(0, screen.colours - 1),
#                         bg=randint(0, screen.colours - 1)
#                         )
#         key = screen.get_key()
#         if key in (ord("Q"), ord("q")):
#             return
#         screen.refresh()

# Screen.wrapper(hello)

# from random import randint
# from asciimatics.screen import Screen

# def hello(screen: Screen):
#     while True:
#         screen.print_at("Hello from ASCIIMatics",
#                         randint(0, screen.width), randint(0, screen.height),
#                         colour=randint(0, screen.colours - 1),
#                         bg=randint(0, screen.colours - 1)
#                         )
#         key = screen.get_key()
#         if key in (ord("Q"), ord("q")):
#             return
#         screen.refresh()

# Screen.wrapper(hello)

#!/usr/bin/env python3

from __future__ import division
import argparse
import os
import signal, tempfile
import subprocess
import sys
import time
from random import randint, choice
from pyfiglet import Figlet

from asciimatics.effects import Scroll, Mirage, Wipe, Cycle, Matrix, \
    BannerText, Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import FigletText, Rainbow, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError


def _mpplus(screen):
    scenes = []
    center = (screen.width // 2, screen.height // 2)

    text = Figlet(font="banner", width=200).renderText("Gauravji")
    width = max([len(x) for x in text.split("\n")])

    effects = [
        Print(screen,
              Fire(screen.height, 80, text, 0.4, 40, screen.colours),
              0,
              speed=1,
              transparent=False),
        Print(screen,
              FigletText("Gauravji", "banner"),
              screen.height - 9, x=(screen.width - width) // 2 + 1,
              colour=Screen.COLOUR_BLACK,
              bg=Screen.COLOUR_BLACK,
              speed=1),
        Print(screen,
              FigletText("Gauravji", "banner"),
              screen.height - 9,
              colour=Screen.COLOUR_WHITE,
              bg=Screen.COLOUR_WHITE,
              speed=1),
    ]
    scenes.append(Scene(effects, 100))

    text = Figlet(font="banner", width=200).renderText("Plus!")
    width = max([len(x) for x in text.split("\n")])

    effects = [
        Print(screen,
              Fire(screen.height, 80, text, 0.4, 60, screen.colours),
              0,
              speed=1,
              transparent=False),
        Print(screen,
              FigletText("    Plus!    ", "banner"),
              screen.height - 9, x=(screen.width - width) // 2 + 1,
              colour=Screen.COLOUR_BLACK,
              bg=Screen.COLOUR_BLACK,
              speed=1),
        Print(screen,
              FigletText("    Vasistha bhai    ", "banner"),
              screen.height - 9,
              colour=Screen.COLOUR_WHITE,
              bg=Screen.COLOUR_WHITE,
              speed=1),
    ]
    scenes.append(Scene(effects, 100))

    effects = [
        Matrix(screen, stop_frame=200),
        Mirage(
            screen,
            FigletText("Gaurav ji singh"),
            center[1] - 3,
            Screen.COLOUR_GREEN,
            start_frame=100,
            stop_frame=200),
        Wipe(screen, start_frame=150),
        Cycle(
            screen,
            FigletText("Vasistha rocks"),
            center[1] - 3,
            start_frame=200)
    ]
    scenes.append(Scene(effects, 250, clear=False))

    effects = [
        BannerText(
            screen,
            Rainbow(screen, FigletText(
                "Gaurav don't believe in failure.", font='slant')),
            center[1] - 3,
            Screen.COLOUR_GREEN)
    ]
    scenes.append(Scene(effects))

    effects = [
        Scroll(screen, 3),
        Mirage(
            screen,
            FigletText("Conceived and"),
            screen.height,
            Screen.COLOUR_GREEN),
        Mirage(
            screen,
            FigletText("written by"),
            screen.height + 8,
            Screen.COLOUR_GREEN),
        Mirage(
            screen,
            FigletText("Gaurav Singh Vashishtha"),
            screen.height + 16,
            Screen.COLOUR_GREEN)
    ]
    scenes.append(Scene(effects, (screen.height + 24) * 3))

    effects = [
        BannerText(
            screen,
            Rainbow(screen, FigletText(
                "Music Player Plus", font='banner3-D')),
            center[1] - 3,
            Screen.COLOUR_CYAN),
        Stars(screen, (screen.width + screen.height) // 2, stop_frame=0)
    ]
    scenes.append(Scene(effects))

    effects = [
        BannerText(
            screen,
            Rainbow(screen, FigletText(
                "ASCII MPD Client", font='banner3-D')),
            center[1] - 3,
            Screen.COLOUR_CYAN),
        Stars(screen, (screen.width + screen.height) // 2, stop_frame=0)
    ]
    scenes.append(Scene(effects))

    effects = [
        BannerText(
            screen,
            Rainbow(screen, FigletText(
                "Album Cover Art", font='banner3-D')),
            center[1] - 3,
            Screen.COLOUR_CYAN),
        Stars(screen, (screen.width + screen.height) // 2, stop_frame=0)
    ]
    scenes.append(Scene(effects))

    effects = [
        Mirage(
            screen,
            Rainbow(screen, FigletText("Spectrum")),
            center[1] - 5,
            Screen.COLOUR_GREEN,
            stop_frame=200),
        Mirage(
            screen,
            Rainbow(screen, FigletText("Visualizer")),
            center[1] + 2,
            Screen.COLOUR_GREEN,
            stop_frame=200),
        Wipe(screen, start_frame=150),
        Cycle(
            screen,
            Rainbow(screen, FigletText("Spectrum")),
            center[1] - 5,
            start_frame=200),
        Cycle(
            screen,
            Rainbow(screen, FigletText("Visualizer")),
            center[1] + 2,
            start_frame=200)
    ]

    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(0, 250)))
    scenes.append(Scene(effects))

    effects = [
        Cycle(
            screen,
            FigletText("MusicPlayerPlus", font=font),
            center[1] - 8,
            stop_frame=200),
        Cycle(
            screen,
            FigletText("ROCKS!", font=font),
            center[1] + 3,
            stop_frame=200),
        Stars(screen, (screen.width + screen.height) // 2, stop_frame=200)
    ]
    scenes.append(Scene(effects, 200))

    effects = [
        Stars(screen, screen.width),
    ]
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(0, 250)))

    effects.append(Print(screen,
                         Rainbow(screen, FigletText("MUSIC")),
                         center[1] - 6,
                         speed=1,
                         start_frame=100))
    effects.append(Print(screen,
                         Rainbow(screen, FigletText("PLAYER PLUS!")),
                         center[1] + 1,
                         speed=1,
                         start_frame=100))
    scenes.append(Scene(effects, 300))

    if numcycles is None:
        screen.play(scenes, stop_on_resize=True)
    else:
        screen.play(scenes, stop_on_resize=True, repeat=False)


if __name__ == "__main__":

    def handler(signal_number, frame):
        if debug:
            print("In signal handler with\nsignal number = " + str(signal_number))
            print("frame = " + str(frame))
        if play_song is not None:
            with open(fifo, "w") as mp_fifo:
                if debug:
                    print("Fading volume in signal handler")
                for vol in range(80, 0, -5):
                    print("volume " + str(vol) + " 1", flush=True, file=mp_fifo)
                    time.sleep(0.1)
                if debug:
                    print("Stopping mplayer in signal handler")
                print("stop", flush=True, file=mp_fifo)
                if debug:
                    print("Resetting volume in signl handler")
                print("volume 80 1", flush=True, file=mp_fifo)
                if debug:
                    print("Exiting mplayer in signal handler")
                print("quit", flush=True, file=mp_fifo)
            if debug:
                print("Removing mplayer FIFO in signal handler")
            os.remove(fifo)
        os.rmdir(tmpdir)
        sys.exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--audio", help="audio file to play during effects")
    parser.add_argument("-c", "--cycle", help="number of times to cycle back through effects")
    parser.add_argument("-d", "--debug", default=False, action='store_true', help="Output hopefully useful debugging statements")
    parser.add_argument("-f", "--font", help="Font for FigletText in Cycle effect, default 'small'")
    args = parser.parse_args()

    if args.audio:
        song = args.audio
    else:
        song = None
    if args.cycle:
        numcycles = args.cycle
    else:
        numcycles = None
    if args.debug:
        debug = True
    else:
        debug = False
    if args.font:
        font = args.font
    else:
        font = "small"

    play_song = None
    tmpdir = tempfile.mkdtemp()
    fifo = os.path.join(tmpdir, 'mplayer.fifo')
    signal.signal(signal.SIGINT, handler)
    if song is not None:
        if debug:
            print("Using mplayer FIFO " + fifo)
        os.mkfifo(fifo)
        if debug:
            print("MPlayer starting: mplayer -novideo -volume 80 -really-quiet -nolirc -slave -input file=" + fifo + " " + song)
        play_song = subprocess.Popen(
            ["mplayer", "-novideo", "-volume", "80", "-really-quiet", "-nolirc", "-slave", "-input", "file=" + fifo, song],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT)

    while True:
        try:
            Screen.wrapper(_mpplus)

            if song is not None:
                with open(fifo, "w") as mp_fifo:
                    if debug:
                        print("Fading volume")
                    for vol in range(80, 0, -5):
                        print("volume " + str(vol) + " 1",
                                flush=True, file=mp_fifo)
                        time.sleep(0.1)
                    if debug:
                        print("Stopping mplayer")
                    print("stop", flush=True, file=mp_fifo)
                    if debug:
                        print("Resetting volume")
                    print("volume 80 1", flush=True, file=mp_fifo)
                    if debug:
                        print("Exiting mplayer")
                    print("quit", flush=True, file=mp_fifo)
                os.remove(fifo)

            if debug:
                print("Removing mplayer FIFO")
            os.rmdir(tmpdir)

            if play_song is not None:
                song_status = play_song.poll()
                if song_status is None:
                    os.kill(play_song.pid, signal.SIGTERM)

            sys.exit(0)
        except ResizeScreenError:
            pass