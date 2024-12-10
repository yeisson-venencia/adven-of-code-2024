def load_rules():
    with open("input_05_rules.txt", "r") as f:
        lines = f.read().splitlines()
        rules = []
        for line in lines:
            values = line.split('|')
            rules.append((int(values[0]), int(values[1])))
    return rules

def load_updates():
    with open("input_05_updates.txt", "r") as f:
        lines = f.read().splitlines()
        updates = []
        for line in lines:
            updates.append([int(x) for x in line.split(',')])
    return updates

def get_interesting_rules(page,rules):
    return [x for x in rules if x[0] == page]

def is_valid_update(update,rules):
    checked_pages = []
    for page in update:
        interesting_rules = get_interesting_rules(page,rules)
        interesting_pages = [x[1] for x in interesting_rules]
        problematic_rule = [x for x in checked_pages if x in interesting_pages]
        if len(problematic_rule) > 0:
            return False
        checked_pages.append(page)
    return True


def get_middle_page_from_update(update):
    middle_index = len(update) // 2
    return update[middle_index]

def main():
    rules = load_rules()
    updates = load_updates()
    total = 0
    for update in updates:
        if is_valid_update(update,rules):
            total += get_middle_page_from_update(update)
    print(total)

main()