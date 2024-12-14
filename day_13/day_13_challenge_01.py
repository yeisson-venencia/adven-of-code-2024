class Machine:
    def __init__(self, a_instructions, b_instructions, prize):
        self.a_instructions = a_instructions
        self.b_instructions = b_instructions
        self.prize = prize

    def is_under_price_moves(self, a_moves,b_moves):
        x_position = a_moves * self.a_instructions[0] + b_moves * self.b_instructions[0]
        y_position = a_moves * self.a_instructions[1] + b_moves * self.b_instructions[1]
        return x_position < self.prize[0] and y_position < self.prize[1]

    def is_solution(self, a_moves,b_moves):
        x_position = a_moves * self.a_instructions[0] + b_moves * self.b_instructions[0]
        y_position = a_moves * self.a_instructions[1] + b_moves * self.b_instructions[1]
        return x_position == self.prize[0] and y_position == self.prize[1]

    @staticmethod
    def solution_cost(a_moves,b_moves):
        return 3 * a_moves + b_moves

    def get_minimum_tokens(self):
        print(f"A: {self.a_instructions}, B: {self.b_instructions}, Prize: {self.prize}")
        solutions = []
        for a_moves in range(101):
            for b_moves in range(101):
                if self.is_under_price_moves(a_moves,b_moves):
                    continue
                if self.is_solution(a_moves,b_moves):
                    solutions.append((a_moves,b_moves))
                    break
        print(f"Solutions: {solutions}")
        if len(solutions) == 0:
            return 0

        cost = 1000
        for a_moves,b_moves in solutions:
            solution_cost = cost = self.solution_cost(a_moves,b_moves)
            if solution_cost < cost:
                cost = solution_cost
        return cost

def get_button_data(line):
    x = int(line.split(',')[0].split('X+')[1])
    y = int(line.split(',')[1].split('Y+')[1])
    return x,y

def get_prize_data(line):
    x = int(line.split(',')[0].split('X=')[1])
    y = int(line.split(',')[1].split('Y=')[1])
    return x, y

def load_machines():
    with open('input_13.txt') as file:
        lines = file.read().splitlines()
        lines = [x for x in lines if x != '']
    i = 0
    total_lines = len(lines)
    machines = []
    while i < total_lines:
        a_instructions = get_button_data(lines[i])
        i += 1
        b_instructions = get_button_data(lines[i])
        i += 1
        prize = get_prize_data(lines[i])
        machine = Machine(a_instructions, b_instructions, prize)
        machines.append(machine)
        i += 1
    return machines

def main():
    machines = load_machines()
    total_tokens = 0
    for machine in machines:
        total_tokens += machine.get_minimum_tokens()
    print(total_tokens)

main()