def rot_string(orig: str, shift: int) -> str:
    res = []
    for char in orig:
        if char.isalpha():
            if char.isupper():
                shifted = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            if char.islower():
                shifted = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            res.append(shifted)
        else:
            res.append(char)
            
    return "".join(res)
     
print(rot_string("Abc", 1))

