
class Computer:
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.instruction_pointer = 0
        self.program = program
        self.out = []

    def run(self):
        while self.instruction_pointer < len(self.program):
            self.execute_instruction()

    def execute_instruction(self):
        operand = self.program[self.instruction_pointer + 1]
        opcode = self.program[self.instruction_pointer]
        
        if opcode == 0:
            self.adv(operand)
        elif opcode == 1:
            self.bxl(operand)
        elif opcode == 2:
            self.bst(operand)
        elif opcode == 3:
            self.jnz(operand)
        elif opcode == 4:
            self.bxc()
        elif opcode == 5:
            self.out_instruction(operand)
        elif opcode == 6:
            self.bdv(operand)
        elif opcode == 7:
            self.cdv(operand)
        else:
            raise ValueError("opcode greater than 7")

    def combo_operand(self, operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        else:
            raise ValueError("combo operand greater than 6")

    def adv(self, operand):
        operand = self.combo_operand(operand)
        self.a >>= operand
        self.instruction_pointer += 2

    def bxl(self, operand):
        self.b ^= operand
        self.instruction_pointer += 2

    def bst(self, operand):
        operand = self.combo_operand(operand)
        self.b = operand & 7
        self.instruction_pointer += 2

    def jnz(self, operand):
        if self.a != 0:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2

    def bxc(self):
        self.b ^= self.c
        self.instruction_pointer += 2

    def out_instruction(self, operand):
        operand = self.combo_operand(operand)
        self.out.append(operand & 7)
        self.instruction_pointer += 2

    def bdv(self, operand):
        operand = self.combo_operand(operand)
        self.b = self.a >> operand
        self.instruction_pointer += 2

    def cdv(self, operand):
        operand = self.combo_operand(operand)
        self.c = self.a >> operand
        self.instruction_pointer += 2

def parse_input(input_text):
    lines = input_text.strip().split('\n')
    a = int(lines[0].split(':')[1].strip())
    b = int(lines[1].split(':')[1].strip())
    c = int(lines[2].split(':')[1].strip())
    program = list(map(int, lines[4].split(':')[1].strip().split(',')))
    
    return Computer(a, b, c, program)

def main():
    # Read input file
    with open("input.txt", "r") as file:
        input_text = file.read()

    # Parse input
    computer = parse_input(input_text)
    
    # Run the program
    computer.run()
    
    # Print the output as a comma-separated string
    print(",".join(map(str, computer.out)))

if __name__ == "__main__":
    main()

# answer is 6,5,7,4,5,7,3,1,0