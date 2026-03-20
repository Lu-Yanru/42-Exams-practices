def check_base(base: str) -> bool:
    if len(base) < 2:
        return False
    if "+" in base or "-" in base or " " in base:
        return False
    return len(set(base)) == len(base)


def ft_atoi_base(num: str, base: str) -> int:
    n = 0
    space = 0
    sign = 1
    while num[space].isspace():
        space += 1
    if num[space] == "-" or num[space] == "+":
        if num[space] == "-":
            sign = -1
        space += 1
    num = num[space:]
    nbase = len(base)
    for digit in num:
        if digit not in base:
            return n * sign
        
        digit_value = base.index(digit)
        n = n * nbase + digit_value
    
    return n * sign


def ft_itoa_base(num: int, base: str) -> str:
    neg = False
    if num < 0:
        neg = True
        num = -num
    
    if num == 0:
        return base[0]
    
    res = []
    nbase = len(base)
    while num != 0:
        remainder = num % nbase
        res.append(base[remainder])
        num = num // nbase
    
    converted = "".join(reversed(res))
    if neg:
       converted = "-" + converted
    return converted


def ft_convert_base(num: str, base_from: str, base_to: str) -> str:
    if not check_base(base_from) or not check_base(base_to):
        return ""

    n = ft_atoi_base(num, base_from)
    res = ft_itoa_base(n, base_to)
    
    return res


print(ft_convert_base("    -8", "0123456789", "01"))

