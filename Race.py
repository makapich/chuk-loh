from graphics import *
from Dice import Dice

FINISH_LINE_X = 600

class Horse:
    def __init__(self, speed, y_position, image):
        self.speed = speed
        self.y_position = y_position
        self.x_position = 0
        self.image = image
        self.dice = Dice(speed)

    def move(self):
        roll = self.dice.roll()
        self.x_position += roll * self.speed

    def draw(self, window):
        self.image.move(self.x_position, self.y_position)
        self.image.draw(window)

    def undraw(self):
        self.image.undraw()

    def crossed_finish_line(self):
        return self.x_position >= FINISH_LINE_X

def clear_objects(horses, window):
    for horse in horses:
        horse.undraw()
    window.update()


def main():
    win = GraphWin("Horse Race", 700, 350)

    horse_image1 = Image(Point(0, 0), "Knight.gif")
    horse_image2 = Image(Point(0, 0), "Wizard.gif")

    horse1 = Horse(6, 100, horse_image1)
    horse2 = Horse(5, 200, horse_image2)

    finish_line = Line(Point(FINISH_LINE_X, 0), Point(FINISH_LINE_X, 350))
    finish_line.draw(win)

    horses = [horse1, horse2]

    for horse in horses:
        horse.draw(win)

    win.getMouse()

    while True:
        for horse in horses:
            horse.move()

        win.update()  # Update the window to show the new positions

        winners = [horse for horse in horses if horse.crossed_finish_line()]

        if winners:
            if len(winners) == 2:
                print("Tie")
            else:
                winning_horse = max(winners, key=lambda horse: horse.x_position)
                print(f"Horse {horses.index(winning_horse) + 1} is the winner")
            break

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()