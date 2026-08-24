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


def crate_rows2(items: list, n: int) -> list[list]:
    # Guard: n <= 0 means no valid row size — refuse and return nothing.
    # This also implicitly covers "empty item list" when combined with the loop
    # below, but we still need this explicit check since an empty list with a
    # valid n > 0 should return [] too (no rows to build), not error out.
    if n <= 0:
        return []

    # Work on a shallow copy so the caller's original list is never mutated,
    # per the "must not be modified" rule.
    items = list(items)

    rows = []
    # Step through items n at a time. range(0, len(items), n) gives the start
    # index of each row; slicing past the end is safe in Python (just shorter).
    for i in range(0, len(items), n):
        chunk = items[i:i + n]
        # Pad the final chunk with None until it reaches length n, if it's short.
        if len(chunk) < n:
            chunk = chunk + [None] * (n - len(chunk))
        rows.append(chunk)

    return rows


print(crate_rows([1, 2, 4, 5], 2))
print(crate_rows(["seeds", "pots", "soil", "tools", "rope"], 3))
print(crate_rows([1, 2, 3], 0))
print(crate_rows([], 4))
