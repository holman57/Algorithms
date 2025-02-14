# Given an integer array nums, find and return all unique triplets
#   [nums[i], nums[j], nums[k]], where the indexes satisfy
#   i != j, i != k, and j != k, and the sum of the elements
#   nums[i] + nums[j] + nums[k] == 0.

# l, r = i + 1, len(N) - 1: Two pointers, `l` and `r`,
#   are initialized. `l` starts from the element after `N[i]`,
#   and `r` starts from the last element of the array. These
#   pointers will move towards each other.

def three_sum(N):
    res = []
    N.sort()
    for i in range(len(N)):
        if i > 0 and N[i] == N[i - 1]:
            continue
        l, r = i + 1, len(N) - 1
        while l < r:
            sum3 = N[i] + N[l] + N[r]
            if sum3 > 0:
                r -= 1
            elif sum3 < 0:
                l += 1
            else:
                res.append([N[i], N[l], N[r]])
                l += 1
                while N[l] == N[l - 1] and l < r:
                    l += 1
    return res

def test():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([]) == []
    assert three_sum([0]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]

test()

