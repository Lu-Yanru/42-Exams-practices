def pack_tally(tally: str) -> str:
    if not tally:
        return ""

    res = ""
    prev_letter = tally[0]
    res += prev_letter
    count = 0
    for letter in tally:
        if letter == prev_letter:
            count += 1
        else:
            if count > 1:
                if count <= 9:
                    res += str(count)
                else:
                    repeat = count // 9
                    last_digit = count % 9
                    i = 0
                    while i < repeat:
                        res += "9"
                        if last_digit > 0 or (last_digit == 0 and i < repeat - 1):
                            res += str(prev_letter)
                        i += 1
                    if last_digit > 1:
                        res += str(last_digit)
            count = 1
            prev_letter = letter
            res += letter

    # For the last letter
    if count > 1:
        if count <= 9:
            res += str(count)
        else:
            repeat = count // 9
            last_digit = count % 9
            i = 0
            while i < repeat:
                res += "9"
                if last_digit > 0 or (last_digit == 0 and i < repeat - 1):
                    res += str(prev_letter)
                i += 1
            if last_digit > 1:
                res += str(last_digit)

    return res


def unpack_tally(packed: str) -> str:
    if not packed:
        return ""

    res = ""
    prev_letter = "1"
    count = 1
    for letter in packed:
        try:
            count = int(letter)
            res += prev_letter * count
        except ValueError:
            count = 1
            try:
                count = int(prev_letter)
            except ValueError:
                res += prev_letter
        prev_letter = letter

    try:
        count = int(prev_letter)
    except ValueError:
        res += prev_letter
    return res


def pack_tally2(tally: str) -> str:
    if not tally:
        return ""

    result = []
    i = 0
    n = len(tally)

    while i < n:
        letter = tally[i]
        # Count how far this run of identical letters extends.
        run_len = 1
        while i + run_len < n and tally[i + run_len] == letter:
            run_len += 1

        # Emit the run in blocks of at most 9, since shorthand only allows
        # single-digit counts. Each block is fully consumed before moving on.
        remaining = run_len
        while remaining > 0:
            block = min(remaining, 9)
            if block == 1:
                # Rule: a run of exactly 1 skips the number entirely.
                result.append(letter)
            else:
                result.append(letter + str(block))
            remaining -= block

        i += run_len  # jump past the whole run, not just one character

    return "".join(result)


def unpack_tally2(packed: str) -> str:
    if not packed:
        return ""

    result = []
    i = 0
    n = len(packed)

    while i < n:
        letter = packed[i]
        i += 1
        # Peek at the next character: if it's a single digit, it's the count
        # for this letter; otherwise the letter is implicitly a lone occurrence.
        if i < n and packed[i].isdigit():
            count = int(packed[i])
            i += 1
        else:
            count = 1
        result.append(letter * count)

    return "".join(result)


def unpack_tally3(packed: str) -> str:
    if not packed:
        return ""

    res = ""
    i = 0
    while i < len(packed):
        if packed[i].isdigit():
            res += packed[i - 1] * int(packed[i])
        else:
            if i + 1 < len(packed) and packed[i + 1].isdigit():
                i += 1
                continue
            else:
                res += packed[i]
        i += 1

    return res


print("====pack====")
print(pack_tally("aabccca"))
print(pack_tally("abc"))
print(pack_tally("aaaaaaaaaa"))
print(pack_tally("aaaaaaaaaaaaaaaaaaaa"))
print(pack_tally(""))

print("====unpack====")
print(unpack_tally("a2bc3a"))
print(unpack_tally("a9ab"))
print(unpack_tally("abc"))
