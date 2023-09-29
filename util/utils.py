import random

from typing import Tuple

def randon_point(upper_left: Tuple[int, int], lower_right: Tuple[int, int]) -> Tuple[int, int]:
    rand_x = random.randint(upper_left[0], lower_right[0])
    rand_y = random.randint(upper_left[1], lower_right[1])
    return rand_x, rand_y