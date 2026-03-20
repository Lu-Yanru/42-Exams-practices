def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def group_anagrams(strs: list[str]) -> list[list[str]]:
    res = []
    
    for i in range(len(strs)):
        anagram = False
        for j in range(i + 1, len(strs)):
            if is_anagram(strs[i], strs[j]):
                res.append([strs[i], strs[j]])
                # strs.remove(strs[j])
                anagram = True
        if not anagram:
            res.append([strs[i]])
    return res

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams(strs))
