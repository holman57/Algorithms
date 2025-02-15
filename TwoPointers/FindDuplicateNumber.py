# Given an array of positive numbers, nums, such that the
#   values lie in the range [1,n], inclusive, and that there are
#   n + 1 numbers in the array, find and return the duplicate
#   number present in nums. There is only one repeated number
#   in nums, but it may appear more than once in the array.

def find_duplicate(nums):
    slow, fast = nums[0], nums[nums[0]]

    while slow != fast:
        slow, fast = nums[slow], nums[nums[fast]]

    fast = 0
    while slow != fast:
        slow, fast = nums[slow], nums[fast]

    return slow


def test_find_duplicate():
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    assert find_duplicate([3, 1, 3, 4, 2]) == 3
    assert find_duplicate([1, 1]) == 1
    assert find_duplicate([1, 1, 2]) == 1
    assert find_duplicate([2, 2, 2, 2, 2]) == 2


test_find_duplicate()
print("All test cases passed!")
