import re



def load_data():
    with open("input_24.txt") as file:
        values, equations = file.read().split("\n\n")
        values_dict = dict()
        for item in values.split("\n"):
            variable,value = item.split(":")
            values_dict[variable] = True if value.strip() == '1' else False

        equations_list = list()
        results_dict = dict()
        for equation in equations.split("\n"):
            left,operation,right,_,result = equation.split(" ")
            operands  = [left, right]
            operands.sort()
            left, right = operands
            eq_tuple = (left,operation,right,result)
            results_dict[result] = eq_tuple
            equations_list.append(eq_tuple)
    return values_dict, equations_list, results_dict

def find_equation_tree(variable,results_dict,tree_set, deepth):
    if deepth > 3:
        return
    if variable not in results_dict:
        return
    eq = results_dict[variable]
    tree_set.add(eq)
    left,_,right,_ = eq
    find_equation_tree(left,results_dict,tree_set, deepth+1)
    find_equation_tree(right,results_dict,tree_set, deepth+1)

def is_compatible_equations(equation,operands):
    eq1,eq2,eq3,eq4 = equation
    op1,op2,op3 = operands
    return eq1 == op1 and eq2 == op2 and eq3 == op3

def main():
    values_dict, equations_list, results_dict = load_data()
    tree_dict = dict()

    for i in range(46):
        look_value = f"z0{i}" if i < 10 else f"z{i}"
        tree_set = set()
        find_equation_tree(look_value,results_dict,tree_set,0)
        tree_dict[look_value] = tree_set

    errors = []
    for i in range(2,45):
        ci = f"0{i}" if i < 10 else f"{i}"
        pi = f"0{i-1}" if i-1 < 10 else f"{i-1}"
        # ppi = f"0{i - 2}" if i - 2 < 10 else f"{i - 2}"
        cz = f"z{ci}"
        cx = f"x{ci}"
        cy = f"y{ci}"
        # pz = f"z{pi}"
        # ppz = f"z{ppi}"
        px = f"x{pi}"
        py = f"y{pi}"

        t_eq = results_dict[cz]
        if t_eq[0] not in results_dict or t_eq[2] not in results_dict or t_eq[1] != 'XOR':
            errors.append(cz)
            continue

        lte = results_dict[t_eq[0]]
        rte = results_dict[t_eq[2]]
        if is_compatible_equations(lte,(cx,'XOR',cy)):
            to_test = t_eq[2]
        elif is_compatible_equations(rte,(cx,'XOR',cy)):
            to_test = t_eq[0]
        else:
            errors.append(cz)
            continue

        t_eq = results_dict[to_test]
        if t_eq[0] not in results_dict or t_eq[2] not in results_dict:
            errors.append(cz)
            continue
        lte = results_dict[t_eq[0]]
        rte = results_dict[t_eq[2]]
        if is_compatible_equations(lte, (px, 'AND', py)):
            to_test = t_eq[2]
        elif is_compatible_equations(rte, (px, 'AND', py)):
            to_test = t_eq[0]
        else:
            errors.append(cz)
            continue

        t_eq = results_dict[to_test]
        if t_eq[0] not in results_dict or t_eq[2] not in results_dict:
            errors.append(cz)
            continue
        lte = results_dict[t_eq[0]]
        rte = results_dict[t_eq[2]]
        if is_compatible_equations(lte, (px, 'XOR', py)):
            to_test = t_eq[2]
        elif is_compatible_equations(rte, (px, 'XOR', py)):
            to_test = t_eq[0]
        else:
            errors.append(cz)
            continue

    print()
    for item in errors:
        print(item)
        print(tree_dict[item])

main()

solution = ['tpk','wkb','pfn','z23','kcd','z27','shj','z07']
solution.sort()
print(','.join(solution))

