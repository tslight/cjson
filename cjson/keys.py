import curses

def keys(div):
    key = div.getch()
    {
        27: quit(),
        ord('q'): quit(),
    }[key]

