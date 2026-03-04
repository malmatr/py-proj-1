import math


def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height * width) / coverage)
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)