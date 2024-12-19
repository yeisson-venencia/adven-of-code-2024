def load_data():
    with open("input_19.txt") as file:
        parts = file.read().split("\n\n")
        towels = parts[0].split(", ")
        designs = parts[1].splitlines()
    return towels, designs

def analyse_design(design,towels):
    sub_versions = []
    for i in range(1,len(design)):
        design_start = design[:i]
        design_end = design[i:]
        if design_start in towels:
            sub_versions.append(design_end)

    return design in towels, sub_versions

def get_design_possibilities(design,towels,possibilities_dict):
    if design in possibilities_dict:
        return possibilities_dict[design]
    is_current_possible, alternatives = analyse_design(design, towels)
    possibilities = 1 if is_current_possible else 0
    for alternative in alternatives:
        possibilities += get_design_possibilities(alternative,towels,possibilities_dict)
    possibilities_dict[design] = possibilities
    return possibilities

def main():
    towels, designs = load_data()
    possible_design = 0
    possibilities_dict = dict()
    for design in designs:
        possible_design += get_design_possibilities(design,towels,possibilities_dict)
    print(possible_design)

main()