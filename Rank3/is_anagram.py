def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(is_anagram("racecar", "carrace"))
print(is_anagram("jar", "jam"))

