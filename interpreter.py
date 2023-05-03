from typing import Deque, List, Callable
from collections import deque

commands = frozenset({
    "push",
    "add",
    "multiply",
    "duplicate",
    "outC",
    "outI",
})

def operate(command: str, stack: Deque[int]) -> str | int | None:
    match command:
        case "push":
            stack.append(1)
        case "add":
            if len(stack) >= 2:
                stack.append(stack.pop() + stack.pop())
        case "multiply":
            if len(stack) >= 2:
                stack.append(stack.pop() * stack.pop())
        case "duplicate":
            if stack:
                stack.append(stack[-1])
        case "outC":
            if stack:
                return chr(stack.pop())
        case "outI":
            if stack:
                return stack.pop()
        

def interpret(program: List[str], out: Callable=print):
    stack = deque()
    for command in program:
        result = operate(command, stack)
        #print(command, stack)
        if result is not None:
            out(result)


#interpret(["push", "push", "add", "duplicate", "add", "duplicate", "multiply", "outI"])

'''DOES NOT WORK FOR NULL CHARACTER'''
def gen_letter(letter: str) -> List[str]:
    target = ord(letter)

    # Get a mask of what values we need
    # Removes the first 3 characters from the string (always 0b1)
    # Reverses so we can iterate over the mask
    binstr = bin(target)[-1:2:-1]

    one_count = 0

    prog = ["push"]
    for digit in binstr:
        prog.append("duplicate")
        # Make an extra duplicate for the values we want to add
        if int(digit):
            prog.append("duplicate")
            one_count += 1
        prog.append("add")

    prog.extend(["add"] * one_count)

    prog.append("outC")
    return prog

def gen_string(to_output: str) -> List[str]:
    prog = []
    for letter in to_output:
        prog.extend(gen_letter(letter))
    return prog


prog = gen_string("Hello, World!")
print(len(prog))
interpret(prog, lambda x: print(f"OUTPUT: {x}"))

