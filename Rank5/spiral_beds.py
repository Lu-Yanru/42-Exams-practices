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


def spiral_beds2(n: int) -> list[list[int]]:
    # No garden for zero or negative size.
    if n <= 0:
        return []

    # Pre-allocate an n x n grid of placeholders to fill in as we spiral.
    grid = [[0] * n for _ in range(n)]

    # Four boundaries that shrink inward as each ring of the spiral completes.
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    num = 1
    while top <= bottom and left <= right:
        # Walk right across the top row.
        for col in range(left, right + 1):
            grid[top][col] = num
            num += 1
        top += 1  # that row is done, shrink the top boundary down

        # Walk down the right column.
        for row in range(top, bottom + 1):
            grid[row][right] = num
            num += 1
        right -= 1  # that column is done, shrink the right boundary left

        # Walk left across the bottom row — but only if a bottom row still
        # remains (guards against re-walking a row already filled when n is odd
        # and we're down to a single middle row).
        if top <= bottom:
            for col in range(right, left - 1, -1):
                grid[bottom][col] = num
                num += 1
            bottom -= 1

        # Walk up the left column — same guard, needed when n is odd and we're
        # down to a single middle column.
        if left <= right:
            for row in range(bottom, top - 1, -1):
                grid[row][left] = num
                num += 1
            left += 1

    return grid


print(spiral_beds(3))
print(spiral_beds(2))
print(spiral_beds(1))
print(spiral_beds(0))
