import curses

iron = 10
copper = 2
titanium = 1
ice = 25
gold = 20
resin = 4
glue = 10
flextape = 1
water = 40
hydrogen  = 510
helium = 420
nitrogen = 35
argon = 200
cotwo = 130
methane = 95
food_pack = 43
food_berry = 0
food_cream = 0
food_bread = 0
food_fish = 0
food_cheese = 0
food_meat = 0
food_citris = 0
food_noodles = 0
food_broth = 0
def start():
  
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)

if __name__ == '__main__':
    curses.wrapper(main)