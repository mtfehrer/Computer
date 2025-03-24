# InstructionBuilder class might be a good idea

# opcode: 4 bits
# I: 1 bit
# dest: 4 bits
# src: 7 bits
# total = 16 bits

#import this from file
opcode_string_to_binary = {"mov": "0000", "add": "0001"}

file = open("program1.my_asm", "r")
lines = file.readlines()
output = ""

for line in lines:
    split_line = line.split()
    opcode = split_line[0]
    destination = None
    source = None
    if len(split_line) == 2:
        destination = split_line[1]
    if len(split_line) == 3:
        source = split_line[2]
    
    instruction_values = {"opcode": "0000", "i": "0", "destination": "0000", "source": "0000000"}
    instruction_values["opcode"] = opcode_string_to_binary[opcode]
    if destination:
        instruction_values["destination"] = bin(int(destination[1:]))[2:]
    if source:
        if source[0] == "r":
            instruction_values["i"] = "1"
            source = source[1:]
        instruction_values["source"] = bin(int(source))[2:]
    
    print(instruction_values)
    output += instruction_values["opcode"] + instruction_values["i"] + instruction_values["destination"] + instruction_values["source"]

print(output)