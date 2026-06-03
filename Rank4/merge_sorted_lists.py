def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    res: list[int] = []

    for lst in lists:
        res += lst

    res.sort()
    return res
