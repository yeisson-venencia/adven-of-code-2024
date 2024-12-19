def load_data():
    with open("input_19.txt") as file:
        parts = file.read().split("\n\n")
        towels = parts[0].split(", ")
        designs = parts[1].splitlines()
    return towels, designs

def analyse_design(design,towels):
    if design in towels:
        return True, []

    sub_versions = []
    for i in range(1,len(design)):
        design_start = design[:i]
        design_end = design[i:]
        if design_start in towels:
            sub_versions.append(design_end)

    if len(sub_versions) == 0:
        return False, []

    return False, sub_versions

def is_design_possible(design,towels, possibilities_dict):
    if design in possibilities_dict:
        return possibilities_dict[design]

    is_possible, alternatives = analyse_design(design, towels)
    if is_possible:
        possibilities_dict[design] = True
        return True

    if len(alternatives) == 0:
        possibilities_dict[design] = False
        return False

    is_current_possible = False
    for alternative in alternatives:
        is_alternative_possible = is_design_possible(alternative,towels,possibilities_dict)
        if is_alternative_possible:
            is_current_possible = True
            break
    possibilities_dict[design] = is_current_possible
    return is_current_possible

def main():
    towels, designs = load_data()
    possible_design = 0
    possibilities_dict = dict()
    for design in designs:
        possible_design += 1 if is_design_possible(design,towels,possibilities_dict) else 0
    print(possible_design)

main()