def is_validate_difference(difference):
    return not (difference < 1 or difference > 3)

def is_valid_direction(directions):
    total_increases = directions.count('+')
    return total_increases == 0 or total_increases == len(directions)

def is_valid_check_report(report):
    values = report.split()
    direction = []
    for i in range(len(values) - 1):
        difference = int(values[i + 1]) - int(values[i])
        direction.append('+' if difference > 0 else '-')
        if not is_validate_difference(abs(difference)):
            return False
        if not is_valid_direction(direction):
            return False
    return True

with open('input_02.txt') as file:
    lines = file.read().splitlines()
    valid_reports_count = 0
    for line in lines:
        if is_valid_check_report(line):
            valid_reports_count += 1

    print(valid_reports_count)