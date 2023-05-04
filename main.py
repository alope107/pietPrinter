from pietprinter.generator import gen_string
from pietprinter.transliterator import program_to_image

prog = gen_string("Hello, World!")
print(prog)
img = program_to_image(prog, (0, 0))
img.save("output.png")
