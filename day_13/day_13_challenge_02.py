class Machine:
    def __init__(self, a_instructions, b_instructions, prize):
        self.a_instructions = a_instructions
        self.b_instructions = b_instructions
        self.prize = prize

    def is_solution(self, a_moves,b_moves):
        x_position = a_moves * self.a_instructions[0] + b_moves * self.b_instructions[0]
        y_position = a_moves * self.a_instructions[1] + b_moves * self.b_instructions[1]
        return x_position == self.prize[0] and y_position == self.prize[1]

    @staticmethod
    def solution_cost(a_moves,b_moves):
        return 3 * a_moves + b_moves

    def get_minimum_tokens(self):
        print(f"A: {self.a_instructions}, B: {self.b_instructions}, Prize: {self.prize}")
        x_a, y_a = self.a_instructions
        x_b, y_b = self.b_instructions
        x_c, y_c = self.prize

        a_moves = int((x_c * y_b - y_c * x_b) / ( x_a * y_b - y_a * x_b))
        b_moves = int((x_c - x_a * a_moves)/ x_b)

        if self.is_solution(a_moves,b_moves):
            return self.solution_cost(a_moves,b_moves)
        return 0

def get_button_data(line):
    x = int(line.split(',')[0].split('X+')[1])
    y = int(line.split(',')[1].split('Y+')[1])
    return x,y

def get_prize_data(line):
    x = int(line.split(',')[0].split('X=')[1]) + 10000000000000
    y = int(line.split(',')[1].split('Y=')[1]) + 10000000000000
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