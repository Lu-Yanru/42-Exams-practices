def is_palindron(string: str) -> bool:
    if len(string) == 0:
        return False

    clean_text = []
    for c in string:
        if c.isalpha():
            clean_text.append(c.lower())
    
    if len(clean_text) == 0:
        return False

    i = 0
    j = len(clean_text) - 1
    while i < len(clean_text) // 2:
        if clean_text[i] != clean_text[j]:
            return False
        i += 1
        j -= 1
    return True

print(is_palindron("ab c cba "))
print(is_palindron("ab c a bcba "))
