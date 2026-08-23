def spiral_beds(n: int) -> list[list[int]]:
    if n <= 0:
        return []

    # Initalize matrix
    res: list[list[int]] = []
    i = 0
    while i < n:
        j = 0
        res.append([])
        while j < n:
            res[i].append(0)
            j += 1
        i += 1

    i = 0
    num = 1
    offset = 0
    while i < n - offset:
        j = offset
        while j < n - offset:
            res[i][j] = num
            num += 1
            j += 1
        j -= 1
        i += 1
        while i < n - offset:
            res[i][j] = num
            num += 1
            i += 1
        i -= 1
        j -= 1
        while j >= offset:
            res[i][j] = num
            num += 1
            j -= 1
        j += 1
        i -= 1
        while i > offset:
            res[i][j] = num
            num += 1
            i -= 1
        offset += 1
        i = offset

    return res


print(spiral_beds(3))
print(spiral_beds(2))
print(spiral_beds(1))
print(spiral_beds(0))
