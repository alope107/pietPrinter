from typing import List

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