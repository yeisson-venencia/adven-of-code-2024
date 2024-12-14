import re

class Robot:
    def __init__(self, px,py,vx,vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self, frames, width, height):
        self.px += self.vx * frames
        self.px %= width
        self.py += self.vy * frames
        self.py %= height

    def get_current_quadrant(self, width, height):
        x_threshold = width // 2
        y_threshold = height // 2

        if self.px == x_threshold or self.py == y_threshold:
            return 0

        if self.px in range(x_threshold):
            return 1 if self.py in range(y_threshold) else 2

        return 3 if self.py in range(y_threshold) else 4

    @classmethod
    def get_from_line(cls, line):
        pattern = r'-*\d+'
        values = re.findall(pattern, line)
        return cls(*map(int,values))

def load_data():
    with open('input_14.txt') as file:
        lines = file.read().splitlines()
    return [Robot.get_from_line(line) for line in lines]

def main():
    grid_wide = 101
    grid_tall = 103
    frames = 100
    robots = load_data()
    robot_inventory = { 1: 0, 2: 0, 3: 0, 4: 0}
    for robot in robots:
        robot.move(frames, grid_wide,grid_tall)
        robot_quadrant = robot.get_current_quadrant(grid_wide, grid_tall)
        if robot_quadrant in robot_inventory:
            robot_inventory[robot_quadrant] += 1

    print(robot_inventory)
    total = 1
    for quadrant in robot_inventory.keys():
        total *= robot_inventory[quadrant]

    print(f"total: {total}")

main()