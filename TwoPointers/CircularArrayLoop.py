# We are given a circular array of non-zero integers, nums, where each integer
#   represents the number of steps to be taken either forward or backward from its
#   current index. Positive values indicate forward movement, while negative
#   values imply backward movement. When reaching either end of the array, the
#   traversal wraps around to the opposite end.
#
# The input array may contain a cycle, which is a sequence of indexes characterized
#   by the following:
#       The sequence starts and ends at the same index.
#       The length of the sequence is at least two.
#       The loop must be in a single direction, forward or backward.
#
# Note: A cycle in the array does not have to originate at the beginning. It may
#   begin from any point in the array.
#
# Your task is to determine if nums has a cycle. Return TRUE if there is a cycle.
# Otherwise, return FALSE.
def circular_array_loop(nums):
    n = len(nums)
    for i in range(n):
        slow, fast, direction = i, i, nums[i] > 0
        while True:
            slow, fast = next_index(nums, slow, n), next_index(nums, fast, n)
            if fast != -1:
                fast = next_index(nums, fast, n)
            if slow == -1 or fast == -1 or slow == fast:
                break
            if (nums[slow] > 0) != direction or (nums[fast] > 0) != direction:
                break
        if slow == fast and slow != -1:
            return True
    return False


def next_index(nums, current_index, n):
    if current_index is None:
        return -1

    next_idx = (current_index + nums[current_index]) % n
    if next_idx < 0:
        next_idx += n

    # Handle the case where next_idx is the same as current_index
    if next_idx == current_index:
        return -1

    return next_idx


def test_circular_array_loop():
    assert circular_array_loop([2, -1, 1, 2, 2]) == True
    assert circular_array_loop([-1, 2]) == False
    assert circular_array_loop([-2, 1, -1, -2, -2]) == False
    assert circular_array_loop([1, 1, 2]) == True
    assert circular_array_loop([-1, -2, -3, -4, -5]) == False


test_circular_array_loop()
print("All test cases passed")
