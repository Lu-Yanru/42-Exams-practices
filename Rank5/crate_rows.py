def crate_rows(items: list, n: int) -> list[list]:
    if n <= 0 or not items:
        return []

    res: list[list[str | int | None]] = []
    item_idx = 0
    j = 0
    num_of_items = len(items)
    num_of_rows = num_of_items // n if num_of_items % n == 0 else num_of_items // n + 1
    while j < num_of_rows:
        i = 0
        res.append([])
        while i < n:
            if item_idx < len(items):
                item = items[item_idx]
            else:
                item = None
            res[j].append(item)
            i += 1
            item_idx += 1
        j += 1

    return res


print(crate_rows([1, 2, 4, 5], 2))
print(crate_rows(["seeds", "pots", "soil", "tools", "rope"], 3))
print(crate_rows([1, 2, 3], 0))
print(crate_rows([], 4))
