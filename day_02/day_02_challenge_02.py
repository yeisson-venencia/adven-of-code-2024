def is_validate_difference(difference):
    return not (difference < 1 or difference > 3)

def is_valid_direction(directions):
    total_increases = directions.count('+')
    return total_increases == 0 or total_increases == len(directions)

def is_valid_report_data(report_data):
    direction = []
    for i in range(len(report_data) - 1):
        difference = int(report_data[i + 1]) - int(report_data[i])
        direction.append('+' if difference > 0 else '-')
        if not is_validate_difference(abs(difference)):
            return False
        if not is_valid_direction(direction):
            return False
    return True

def get_alternative_list(original_list, index):
    if index == 0:
        return original_list[1:]
    if index == len(original_list) - 1:
        return original_list[:-1]
    return original_list[:index] + original_list[index + 1:]

def is_valid_report(report):
    values = report.split()
    if is_valid_report_data(values):
        return True
    for _,index in zip(values,range(len(values))):
        alternative_list = get_alternative_list(values,index)
        if is_valid_report_data(alternative_list):
            return True
    return False


with open('input_02.txt') as file:
    lines = file.read().splitlines()
    valid_reports_count = 0
    for line in lines:
        if is_valid_report(line):
            valid_reports_count += 1

    print(valid_reports_count)