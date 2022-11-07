
def main():

    win = GraphWin("Button Example", 500, 500)
    B = Button(win, Point(300, 100), Point(400, 175), "cyan", "Click Me")
    Quit = Button(win, Point(300, 200), Point(400, 275), "red", "Quit")

    i = 0
    while True:
        m = win.getMouse()

        if B.isClicked(m):
            C = Circle(Point(250, 250), 50 + i*20)
            C.draw(win)
            # What happens >> Anything that the button should do

        if Quit.isClicked(m):
            break

        i = i + 1

    win.close()


if __name__ == "__main__":
    main()
