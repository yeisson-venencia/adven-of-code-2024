
def are_points_adjacent(point,element):
    dx = abs(point[0] - element[0])
    dy = abs(point[1] - element[1])
    distance = dx + dy
    return distance == 1

def is_point_adjacent_to_line(element,line):
    for point in line:
        if are_points_adjacent(point, element):
            return True
    return False

class Region:
    def __init__(self, point):
        self.elements = [point]

    def add_element(self, element):
        self.elements.append(element)

    def is_adjacent(self, element):
        return is_point_adjacent_to_line(element,self.elements)

    @property
    def calculate_cost(self):
        area = len(self.elements)
        sides_in_perimeter = []
        for point in self.elements:
            x_coordinate,y_coordinate = point[0],point[1]
            # top point
            top_point = x_coordinate, y_coordinate + 1
            if top_point not in self.elements:
                sides_in_perimeter.append(f"T-{x_coordinate}-{y_coordinate}")
            # bottom point
            bottom_point = x_coordinate, y_coordinate - 1
            if bottom_point not in self.elements:
                sides_in_perimeter.append(f"B-{x_coordinate}-{y_coordinate}")
            # left point
            left_point = x_coordinate - 1, y_coordinate
            if left_point not in self.elements:
                sides_in_perimeter.append(f"L-{x_coordinate}-{y_coordinate}")
            # right point
            right_point = x_coordinate + 1, y_coordinate
            if right_point not in self.elements:
                sides_in_perimeter.append(f"R-{x_coordinate}-{y_coordinate}")

        sides = 0
        for side in sides_in_perimeter:
            [s,x,y] = side.split('-')
            delta = -1,0
            if s in ['L','R']:
                delta = 0,-1
            ref_side = f"{s}-{int(x)+delta[0]}-{int(y)+delta[1]}"
            if ref_side not in sides_in_perimeter:
                sides += 1

        return sides * area

    @classmethod
    def merge_regions(cls, reg1, reg2, point):
        new_reg = cls(point)
        for item in reg1.elements:
            new_reg.add_element(item)
        for item in reg2.elements:
            new_reg.add_element(item)
        return new_reg

def load_map():
    with open('input_12.txt') as file:
        lines = file.read().splitlines()
        lines.reverse()
    return lines

def generate_region_dictionary(layout):
    x_limit, y_limit = len(layout[0]), len(layout)
    region_dict = dict()
    for y in range(y_limit):
        for x in range(x_limit):
            letter = layout[y][x]
            if letter not in region_dict.keys():
                region_dict[letter] = [Region((x, y))]
            else:
                letter_regions = region_dict[letter]
                matching_regions = []
                for region in letter_regions:
                    if region.is_adjacent((x, y)):
                        matching_regions.append(region)
                if len(matching_regions) == 0:
                    letter_regions.append(Region((x, y)))
                elif len(matching_regions) == 1:
                    matching_regions[0].add_element((x, y))
                else:
                    new_region = Region.merge_regions(matching_regions[0], matching_regions[1], (x, y))
                    letter_regions.remove(matching_regions[0])
                    letter_regions.remove(matching_regions[1])
                    region_dict[letter].append(new_region)
    return region_dict

def calculate_total_cost(region_dict):
    total_cost = 0
    for letter in region_dict.keys():
        letter_regions = region_dict[letter]
        for region in letter_regions:
            total_cost += region.calculate_cost()
    return total_cost

def main():
    layout = load_map()
    region_dict = generate_region_dictionary(layout)
    total_cost = calculate_total_cost(region_dict)
    print(total_cost)

main()