def count_vowels(string: str) -> int:
    count = 0
    for letter in string.lower():
        if letter in "aeiou":
            count += 1
    return count


def sort_strings(input: list[str]) -> list[str]:
    res = sorted(input,
                 key=lambda x: (
                                len(x),
                                x.lower(),
                                count_vowels(x)
                 )
          )
    return res


words1 = ["apple", "pie", "banana", "Cat", "dog", "elephant", "ant", "bee"]
print(sort_strings(words1))
words2 = ["aaa", "bbb", "AAA", "BBB"]
print(sort_strings(words2))
words3 = ["algorithm", "Algorithm", "ALGORITHM"]
print(sort_strings(words3))
words4 = ["", "Algorithm", "ALGORITHM"]
print(sort_strings(words4))
print(sort_strings([]))
