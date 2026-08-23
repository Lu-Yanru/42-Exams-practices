def one_letter_diff(word: str, current: str) -> bool:
    count = 0
    for i, letter_w in enumerate(word):
        if current[i] != letter_w:
            count += 1

    return count == 1


def find_possible_next(current: str, queue: list[str],
                       map: dict[str, str | None],
                       used: list[str], wordbook: list[str]) -> None:
    for word in wordbook:
        if word in used:
            continue
        if one_letter_diff(word, current):
            queue.append(word)
            used.append(word)
            map[word] = current


def reconstruct_path(map: dict[str, str | None], end: str) -> int:
    steps: list[str] = [end]

    current = end
    while map[current] is not None:
        prev_word = map[current]
        steps.append(prev_word)
        current = prev_word

    return len(steps)


def repaint_steps(start: str, end: str, wordbook: list[str]) -> int:
    if start == end:
        return 1
    if len(start) != len(end):
        return 0
    if end not in wordbook:
        return 0
    for word in wordbook:
        if len(word) != len(start):
            return 0
        if not word.islower():
            return 0

    map: dict[str, str | None] = {start: None}
    queue: list[str] = [start]
    used: list[str] = [start]

    while queue:
        current = queue.pop(0)
        if current == end:
            return reconstruct_path(map, end)
        find_possible_next(current, queue, map, used, wordbook)

    return 0


print(repaint_steps("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(repaint_steps("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(repaint_steps("a", "c", ["a", "b", "c"]))
print(repaint_steps("same", "same", []))
