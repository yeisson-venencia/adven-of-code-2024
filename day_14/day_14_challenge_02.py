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

    def get_location(self):
        return self.px, self.py

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
    robots = load_data()
    all_shown = []
    for seconds in range(grid_wide*grid_tall):
        locations = set()
        for robot in robots:
            robot.move(1, grid_wide,grid_tall)
            locations.add(robot.get_location())
        if len(locations) == len(robots):
            all_shown.append(seconds + 1)

    print(all_shown)

def show_xmas_tree():
    grid_wide = 101
    grid_tall = 103
    robots = load_data()
    locations = set()
    for robot in robots:
        robot.move(7412, grid_wide,grid_tall)
        locations.add(robot.get_location())

    matrix = [["#" if (x,y) in locations else ' '  for x in range(grid_wide) ] for y in range(grid_tall)]
    for row in matrix:
        print("".join(row))

main()
# show_xmas_tree()