from typing import Deque, List, Callable
from collections import deque

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
        if result is not None:
            out(result)