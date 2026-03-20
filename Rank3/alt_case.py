def alt_case(orig: str) -> str:
    res = []
    i = 0
    for c in orig:
        if c.isalpha():
            if i % 2 == 0:
                res.append(c.upper())
            else:
                res.append(c.lower())
            i += 1
        else:
            res.append(c)

    return "".join(res)
    
print(alt_case("ab123CD"))

