# Given an array, colors, which contains a combination
#   of the following three elements:
#
#   0 (representing red)
#   1 (representing white)
#   2 (representing blue)
#
# Sort the array in place so that the elements of the
#   same color are adjacent, with the colors in the order
#   of red, white, and blue. To improve your problem-solving
#   skills, do not utilize the built-in sort function.

def sort_colors(colors):
    left, right, i = 0, len(colors) - 1, 0

    while i <= right:
        if colors[i] == 0:
            colors[i], colors[left] = colors[left], colors[i]
            left += 1
            i += 1
        elif colors[i] == 2:
            colors[i], colors[right] = colors[right], colors[i]
            right -= 1
        else:
            i += 1

    return colors


def test_sort_colors():
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([], []),
        ([1, 1, 2, 0, 2, 0, 1, 0], [0, 0, 0, 1, 1, 1, 2, 2]),
        ([2, 2, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 2, 2]),

    ]

    for input_arr, expected_arr in test_cases:
        assert sort_colors(input_arr) == expected_arr


test_sort_colors()
print("All test cases passed!")
