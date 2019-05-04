import curses


def footer(screen):
    msg = " [SPC] for fortunes, [h] for help, [w] to save, [q] to quit."
    screen.addstr(curses.LINES - 1, 0, msg)
    screen.chgat(curses.LINES - 1, 1, 5,
                 curses.A_BOLD | curses.color_pair(3))
    screen.chgat(curses.LINES - 1, 21, 3,
                 curses.A_BOLD | curses.color_pair(3))
    screen.chgat(curses.LINES - 1, 35, 3,
                 curses.A_BOLD | curses.color_pair(3))
    screen.chgat(curses.LINES - 1, 48, 3,
                 curses.A_BOLD | curses.color_pair(3))
