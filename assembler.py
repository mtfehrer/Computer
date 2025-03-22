file = open("program1.asm", "r")
lines = file.readlines()
output = ""

# opcode: 4 bits
# I: 1 bit
# dest: 4 bits
# src: 7 bits
# total = 16 bits

for line in lines:
