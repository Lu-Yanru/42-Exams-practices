def sliding_window_max(nums: list[int], k: int) -> list[int]:
    res: list[int] = []

    if len(nums) == 0 or k <= 0 or k > len(nums):
        return res

    for i in range(len(nums) - k + 1):
        tmp = []
        for j in range(k):
            tmp.append(nums[i + j])
        res.append(max(tmp))

    return res


print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sliding_window_max([1, 2, 3, 4, 5], 2))
print(sliding_window_max([5, 4, 3, 2, 1], 1))
print(sliding_window_max([1, 2, 3], 3))
print(sliding_window_max([1, 2, 3], 4))
print(sliding_window_max([], 2))
print(sliding_window_max([1, 2, 3], 0))
