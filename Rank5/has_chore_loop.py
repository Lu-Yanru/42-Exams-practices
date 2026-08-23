def has_chore_loop(chores: dict[int, list[int]]) -> bool:
    if not chores:
        return False

    prev_keys = []
    for key, value in chores.items():
        if value:
            prev_keys.append(key)
        for k in prev_keys:
            if k in value:
                return True
    
    return False

print(has_chore_loop({1: [2], 2: [3], 3: []}))
print(has_chore_loop({1: [2], 2: [3], 3: [1]}))
print(has_chore_loop({1: [1]}))
print(has_chore_loop({0: [1, 2], 1: [3], 2: [3], 3: []}))
print(has_chore_loop({}))
