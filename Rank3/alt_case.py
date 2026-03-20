def alt_case(orig: str) -> str:
    res = []
    i = 0
    while i < len(orig):
        if i % 2 == 0:
            res.append(orig[i].upper())
        else:
            res.append(orig[i].lower())
        i += 1
    return "".join(res)
    
print(alt_case("abCD"))

