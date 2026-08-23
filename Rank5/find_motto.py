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


print(find_motto(["abc", "def", "ghi"], "aei"))
print(find_motto(["abc", "def", "ghi"], "cfi"))
print(find_motto(["abc", "def", "ghi"], "ihg"))
print(find_motto(["abc", "def", "ghi"], "xyz"))
print(find_motto(["bob", "obo", "bob"], "bob"))
