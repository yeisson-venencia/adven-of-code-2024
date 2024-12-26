def load_data():
    with open("input_24.txt") as file:
        values, equations = file.read().split("\n\n")
        values_dict = dict()
        for item in values.split("\n"):
            variable,value = item.split(":")
            values_dict[variable] = True if value.strip() == '1' else False

        equations_list = list()
        for equation in equations.split("\n"):
            left,operation,right,_,result = equation.split(" ")
            equations_list.append((left,operation,right,result))
    return values_dict, equations_list

def main():
    values_dict, equations_list = load_data()
    operate = True
    while operate:
        operate = False
        for equation in equations_list:
            left, operation, right, result = equation
            if result in values_dict:
                continue
            if left not in values_dict or right not in values_dict:
                continue
            operation_result = False
            if operation == "OR":
                operation_result = values_dict[left] or values_dict[right]
            elif operation == "AND":
                operation_result = values_dict[left] and values_dict[right]
            elif operation == "XOR":
                operation_result = values_dict[left] ^ values_dict[right]
            values_dict[result] = operation_result
            operate = True

    word_parts = []
    for key in values_dict.keys():
        if key[0] == 'z':
            word_parts.append(key)

    word_parts.sort()
    print(word_parts)
    print([1 if values_dict[x] else 0 for x in word_parts])
    total = 0
    for i in range(len(word_parts)):
        total += 2**i if values_dict[word_parts[i]] else 0
    print(total)


main()