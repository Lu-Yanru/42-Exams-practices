def check_base(base: int) -> bool:
    if base < 2 or base > 36:
        return False
    return True


def check_number(number: str, from_base: int, base: str) -> bool:
    for c in number:
        if c not in base[:from_base]:
            return False
    return True


def atoi(number: str, from_base: int, base: str) -> int:
    n = 0
    for c in number:
        digit_value = base.index(c)
        n = n * from_base + digit_value
    return n


def itoa(n: int, to_base: int, base: str) -> str:
    if n == 0:
        return base[0]
    
    res = []
    while n != 0:
        digit_index = n % to_base
        res.append(base[digit_index])
        n = n // to_base

    return "".join(reversed(res))


def number_convert_base(number: str, from_base: int, to_base: int) -> str:
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not check_base(from_base) or not check_base(to_base) \
        or not check_number(number, from_base, base):
        return "ERROR"

    n = atoi(number, from_base, base)
    res = itoa(n, to_base, base)

    return res


print(number_convert_base("1000", 2, 10))
print(number_convert_base("G", 16, 10))
