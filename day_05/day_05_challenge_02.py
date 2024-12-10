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

def get_interesting_pages_backward(page,rules):
    return [x[1] for x in rules if x[0] == page]

def get_interesting_pages_forward(page,rules):
    return [x[0] for x in rules if x[1] == page]

def has_problematic_pages(interesting_pages, comparison_pages):
    problematic_pages = [x for x in comparison_pages if x in interesting_pages]
    return len(problematic_pages) > 0

def is_valid_update(update,rules):
    checked_pages = []
    for page in update:
        interesting_pages = get_interesting_pages_backward(page,rules)
        if has_problematic_pages(interesting_pages,checked_pages):
            return False
        checked_pages.append(page)
    return True

def repair_update(update,rules):
    corrected_update = []
    for page in update:
        interesting_pages_backward = get_interesting_pages_backward(page, rules)
        if not has_problematic_pages(interesting_pages_backward,corrected_update):
            corrected_update.append(page)
        else:
            interesting_pages_forward = get_interesting_pages_forward(page, rules)
            for index in range(len(corrected_update) -1, -1, -1):
                subset_backward = corrected_update[:index]
                if has_problematic_pages(interesting_pages_backward, subset_backward):
                    continue
                else:
                    subset_forward = corrected_update[index:]
                    if has_problematic_pages(interesting_pages_forward, subset_forward):
                        return [0,0,0]
                    else:
                        corrected_update.insert(index,page)
                        break
    return corrected_update


def get_middle_page_from_update(update):
    middle_index = len(update) // 2
    return update[middle_index]

def main():
    rules = load_rules()
    updates = load_updates()
    total = 0
    for update in updates:
        if not is_valid_update(update,rules):
            corrected_update = repair_update(update,rules)
            total += get_middle_page_from_update(corrected_update)
    print(total)

main()