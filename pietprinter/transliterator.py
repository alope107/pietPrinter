from typing import List, Tuple
import numpy as np
from PIL import Image

TRANS = {
    'push': (1, 0),
    'pop': (2, 0),
    'add': (0, 1), 
    'subtract': (1, 1),
    'multiply': (2, 1),
    'divide': (0, 2),
    'mod': (1, 2),
    'not': (2, 2), 
    'greater': (0, 3), 
    'pointer': (1, 3), 
    'switch': (2, 3), 
    'duplicate': (0, 4), 
    'roll': (1, 4), 
    'inI': (2, 4), 
    'inC': (0, 5), 
    'outI': (1, 5), 
    'outC': (2, 5)
}

COLORS = [[(255, 192, 192),
  (255, 255, 192),
  (192, 255, 192),
  (192, 255, 255),
  (192, 192, 255),
  (255, 192, 255)],
 [(255, 0, 0),
  (255, 255, 0),
  (0, 255, 0),
  (0, 255, 255),
  (0, 0, 255),
  (255, 0, 255)],
 [(192, 0, 0),
  (192, 192, 0),
  (0, 192, 0),
  (0, 192, 192),
  (0, 0, 192),
  (192, 0, 192)]]

def next_color(current_color: Tuple[int], command: str) -> Tuple[int]:
    dLight, dHue = TRANS[command]
    nextLight = (current_color[0] + dLight) % 3
    nextHue = (current_color[1] + dHue) % 6
    return (nextLight, nextHue)


def color_to_rgb(color: Tuple[int]) -> Tuple[int]:
    return COLORS[color[0]][color[1]]


def colors_to_array(colors: List[Tuple]):
    pixels = np.zeros((2, len(colors)+2, 3), dtype=np.uint8)
    pixels[0, 0:len(colors), :] = colors
    pixels[-2:, -2:, :] = 255
    return pixels


def program_to_image(program: List[str], starting_color: Tuple[int]) -> Image:
    current_color = starting_color

    colors = [color_to_rgb(starting_color)]
    for command in program:
        current_color = next_color(current_color, command)
        colors.append(color_to_rgb(current_color))

    return Image.fromarray(colors_to_array(colors), mode="RGB")
    

