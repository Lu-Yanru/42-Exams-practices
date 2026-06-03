def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    lst: list[list[str]] = []

    for i in range(size):
        tmp = []
        for j in range(size):
            tmp.append(".")
        lst.append(tmp)

    for x, y in set(stars):
        if x < 0 or y < 0 or x >= size or y >= size:
            continue
        lst[x][y] = "*"

    res: list[str] = []
    for row in lst:
        tmp2 = "".join(row)
        res.append(tmp2)

    return res


print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
print(constellation_mapper([], 2))
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
print(constellation_mapper([(0, 0), (5, 5)], 3))
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))
