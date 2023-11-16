
import re

patterns = [
    #Shows the patterns which I will add
    #Credit to Stack overflow and youtube for these patterns
    (r"CHEESEBURGER", "CHEESEBURGER"), #r is for raw code
    (r"Cheeseborger", "Cheeseborger"),
    (r"Cheesebigger", "Cheesebigger"),
    (r"Lettuceburger", "Lettuceburger"),
    (r"bigburger", "bigburger"),
    (r"INPUT", "INPUT"),
]

#Instruction set for anything you can code in
instruction_set = {
    #The world cheeseburger is used as a placeholder for now to simplify things
    "CHEESEBURGER": lambda memory, pointer: memory.__setitem__(pointer[0], memory[pointer[0]] + 1),
    "Cheeseborger": lambda memory, pointer: memory.__setitem__(pointer[0], memory[pointer[0]] - 1),
    "Cheesebigger": lambda memory, pointer: pointer.__setitem__(0, pointer[0] + 1),
    "Lettuceburger": lambda memory, pointer: pointer.__setitem__(0, pointer[0] - 1),
    "bigburger": lambda memory, pointer: print(chr(memory[pointer[0]]), end=""),
    "INPUT": lambda memory, pointer: memory.__setitem__(pointer[0], ord(input("Enter a character: "))),
}
#My lexer
def lex(input_string):
    tokens = []
    while input_string:
        for pattern, token_type in patterns:
            match = re.match(pattern, input_string)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                input_string = input_string[len(value):]
                break
        else:
            print(f"Lexer error: Unrecognized token at: {input_string}")
            break
    return tokens

#My interpreter
def interpret(filename):
    try:
        with open(filename, 'r') as file:
            code = file.read()

        tokens = lex(code)
        memory = [0] * 30000  #Memory tape with 30000 cells
        pointer = [0]

        for token_type, value in tokens:
            if token_type in instruction_set:
                instruction_set[token_type](memory, pointer)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    filename = "test.schizo" #Input file
    interpret(filename)
