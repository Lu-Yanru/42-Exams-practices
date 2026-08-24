def find_motto(quilt: list[str], motto: str) -> list[tuple[int, int, str]]:
    if not motto:
        return []

    res: list[tuple[int, int, str]] = []

    row = 0
    while row < len(quilt):
        col = 0
        while col < len(quilt[row]):
            # H: left to right
            i = 0
            j = col
            while i < len(motto) and j < len(quilt[row]) and quilt[row][j] == motto[i]:
                i += 1
                j += 1
            if i == len(motto):
                res.append((row, col, "H"))
            # H- right to left
            i = 0
            j = col
            while i < len(motto) and j >= 0 and quilt[row][j] == motto[i]:
                i += 1
                j -= 1
            if i == len(motto):
                res.append((row, col, "H-"))
            # V top to bottom
            i = 0
            j = row
            while i < len(motto) and j < len(quilt) and quilt[j][col] == motto[i]:
                i += 1
                j += 1
            if i == len(motto):
                res.append((row, col, "V"))
            # V- bottom to top
            i = 0
            j = row
            while i < len(motto) and j >= 0 and quilt[j][col] == motto[i]:
                i += 1
                j -= 1
            if i == len(motto):
                res.append((row, col, "V-"))
            # D1 down right diagnal
            i = 0
            j = col
            k = row
            while i < len(motto) and k < len(quilt) and j < len(quilt[k]) and quilt[k][j] == motto[i]:
                i += 1
                j += 1
                k += 1
            if i == len(motto):
                res.append((row, col, "D1"))
            # D1- up right diagnal
            i = 0
            j = col
            k = row
            while i < len(motto) and j >= 0 and k >= 0 and quilt[k][j] == motto[i]:
                i += 1
                j -= 1
                k -= 1
            if i == len(motto):
                res.append((row, col, "D1-"))
            # D2 down left diagnal
            i = 0
            j = col
            k = row
            while i < len(motto) and j >= 0 and k < len(quilt) and quilt[k][j] == motto[i]:
                i += 1
                j -= 1
                k += 1
            if i == len(motto):
                res.append((row, col, "D2"))
            # D2- up right diagnal
            i = 0
            j = col
            k = row
            while i < len(motto) and k >= 0 and j < len(quilt[k]) and quilt[k][j] == motto[i]:
                i += 1
                j += 1
                k -= 1
            if i == len(motto):
                res.append((row, col, "D2-"))
            col += 1
        row += 1

    return res


def find_motto2(quilt: list[str], motto: str) -> list[tuple[int, int, str]]:
    # No quilt or no motto means nothing to find, per the rules.
    if not quilt or not motto:
        return []

    height = len(quilt)
    width = len(quilt[0])
    m_len = len(motto)

    # Direction codes paired with their (dy, dx) step vectors, in the exact
    # order the rules specify they must be tried at each starting square.
    directions = [
        ('H',   (0, 1)),    # left-to-right
        ('H-',  (0, -1)),   # right-to-left
        ('V',   (1, 0)),    # top-to-bottom
        ('V-',  (-1, 0)),   # bottom-to-top
        ('D1',  (1, 1)),    # down-right
        ('D1-', (-1, -1)),  # up-left
        ('D2',  (1, -1)),   # down-left
        ('D2-', (-1, 1)),   # up-right
    ]

    matches = []

    # Scan row by row, then column by column, as specified.
    for y in range(height):
        for x in range(width):
            # Try every direction from this starting square, in fixed order.
            for code, (dy, dx) in directions:
                # Compute where the LAST letter of the motto would land if it
                # started here and ran in this direction.
                end_y = y + dy * (m_len - 1)
                end_x = x + dx * (m_len - 1)

                # Skip directions that would run the motto off the quilt.
                if not (0 <= end_y < height and 0 <= end_x < width):
                    continue

                # Build the candidate string by walking the direction vector
                # letter by letter, then compare it to the motto in one shot.
                candidate = "".join(
                    quilt[y + dy * i][x + dx * i] for i in range(m_len)
                )
                if candidate == motto:
                    matches.append((y, x, code))

    return matches


print(find_motto(["abc", "def", "ghi"], "aei"))
print(find_motto(["abc", "def", "ghi"], "cfi"))
print(find_motto(["abc", "def", "ghi"], "ihg"))
print(find_motto(["abc", "def", "ghi"], "xyz"))
print(find_motto(["bob", "obo", "bob"], "bob"))
