import re

def load_data():
    with open('input_17.txt') as file:
        lines = file.read().split('\n\n')
        regex = r'\d+'
        registers = re.findall(regex, lines[0])
        instructions = re.findall(regex, lines[1])
    return registers, instructions

def transform_instructions_to_string(instructions):
    return ','.join([str(x) for x in instructions])

class Program:
    def __init__(self, registers, instructions):
        self.A = int(registers[0])
        self.B = int(registers[1])
        self.C = int(registers[2])
        self.instructions = [int(x) for x in instructions]
        self.pointer = 0
        self.output = []
        self.out_executed = 0

    def get_combo_value(self, operand):
        if operand in range(4):
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        return 0

    def adv(self, operand):
        result = self.A / 2 ** self.get_combo_value(operand)
        self.A = int(result)

    def bxl(self, operand):
        result = self.B ^ operand
        self.B = result

    def bst(self, operand):
        result = self.get_combo_value(operand) % 8
        self.B = result

    def jnz(self,operand):
        if self.A != 0:
            self.pointer = operand

    def bxc(self,operand):
        result = self.B ^ self.C
        self.B = result

    def out(self, operand):
        result = self.get_combo_value(operand) % 8
        self.output.append(result)

    def bdv(self, operand):
        result = self.A / 2 ** self.get_combo_value(operand)
        self.B = int(result)

    def cdv(self, operand):
        result = self.A / 2 ** self.get_combo_value(operand)
        self.C = int(result)

    def get_action(self, instruction):
        instruction_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        return instruction_map[instruction]

    def process_instruction(self):
        instruction = self.instructions[self.pointer]
        self.pointer += 1
        operand = self.instructions[self.pointer]
        self.pointer += 1
        self.get_action(instruction)(operand)

    def execute_program(self):
        while self.pointer in range(len(self.instructions)):
            self.process_instruction()

    def get_output(self):
        return self.output

def main():
    registers, instructions = load_data()
    found = False
    a_value = 0
    reference = 0
    tries = 0
    full_inst_str = transform_instructions_to_string(instructions)
    while not found:
        registers[0] = str(a_value)
        program = Program(registers, instructions)
        program.execute_program()
        output = program.get_output()
        out_str = transform_instructions_to_string(output)
        ins_str = transform_instructions_to_string(instructions[len(instructions) - len(output):])

        if out_str == full_inst_str:
            found = True
        else:
            if out_str == ins_str:
                reference = a_value
                a_value *= 8
                tries = 0
            else:
                tries += 1
                a_value += 1

        if tries == 8:
            a_value  = reference + 1

    print(a_value)

main()