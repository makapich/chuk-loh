from graphics import GraphWin, Line
from Dice import Dice
import random

class Horse:
    def __init__(self, speed, y_position, image_file):
        self.x_position = 50  # Initial x position
        self.y_position = y_position
        self.image = image_file
        self.dice = Dice(speed)

    def move(self):
        roll_value = self.dice.roll()
        self.x_position += roll_value

    def draw(self, window):
        self.image.draw_at_pos(window, self.x_position, self.y_position)

    def crossed_finish_line(self, finish_line_x):
        return self.x_position >= finish_line_x


def Image(param):
    pass


def main():
    # Set up the window
    window_width = 700
    window_height = 350
    win = GraphWin("Horse Race", window_width, window_height)

    # Load images for the two horses (replace with your image files)
    horse_image1 = Image("horse1.gif")
    horse_image2 = Image("horse2.gif")

    # Create two Horse objects
    horse1 = Horse(5, 50, horse_image1)
    horse2 = Horse(5, 150, horse_image2)

    # Set up the finish line
    finish_line_x = window_width - 50
    finish_line = Line(Point(finish_line_x, 0), Point(finish_line_x, window_height))
    finish_line.draw(win)

    # Draw the horses
    horse1.draw(win)
    horse2.draw(win)

    # Wait for a mouse click to start the race
    win.getMouse()

    # Race loop
    while not (horse1.crossed_finish_line(finish_line_x) or horse2.crossed_finish_line(finish_line_x)):
        horse1.move()
        horse2.move()

        # Clear the window and update
        win.delete("all")
        finish_line.draw(win)
        horse1.draw(win)
        horse2.draw(win)
        win.update()

    # Determine the winner
    if horse1.crossed_finish_line(finish_line_x) and horse2.crossed_finish_line(finish_line_x):
        print("Tie")
    elif horse1.crossed_finish_line(finish_line_x):
        print("Horse 1 is the winner")
    else:
        print("Horse 2 is the winner")

    # Wait for a mouse click before ending the program
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
