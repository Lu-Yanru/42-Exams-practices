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
