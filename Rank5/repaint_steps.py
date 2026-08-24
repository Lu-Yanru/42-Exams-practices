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


def repaint_steps2(start: str, end: str, wordbook: list[str]) -> int:
    from collections import deque

    # Gate 1: every wordbook word must be lowercase-only. A word "has an
    # uppercase letter" if it differs from its own .lower() version.
    for word in wordbook:
        if word != word.lower():
            return 0

    # Gate 2: start, end, and every wordbook word must share the same length.
    # Use start's length as the reference; if start and end mismatch, or any
    # wordbook word mismatches, the whole job is off.
    required_len = len(start)
    if len(end) != required_len:
        return 0
    for word in wordbook:
        if len(word) != required_len:
            return 0

    # Both gates passed. Now the start == end shortcut applies unconditionally,
    # even with an empty wordbook, per the explicit example.
    if start == end:
        return 1

    # Build a lookup set for O(1) membership checks. A set naturally dedupes,
    # which is harmless since duplicate wordbook entries don't add new edges.
    words = set(wordbook)

    # If the end word never appears in the wordbook, no chain can reach it
    # (start != end was already established above).
    if end not in words:
        return 0

    # Standard BFS over the implicit "differs by one letter" graph.
    # Each queue entry is (current_word, steps_taken_so_far_including_start).
    queue = deque([(start, 1)])
    visited = {start}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while queue:
        word, steps = queue.popleft()

        # Try changing each position to each other lowercase letter.
        for i in range(required_len):
            original_char = word[i]
            for c in alphabet:
                if c == original_char:
                    continue
                candidate = word[:i] + c + word[i + 1:]

                # Only a candidate that's an actual wordbook word (or the end
                # word itself) counts as a valid intermediate/final step.
                if candidate == end:
                    return steps + 1
                if candidate in words and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, steps + 1))

    # Queue exhausted with no path found.
    return 0


print(repaint_steps("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(repaint_steps("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(repaint_steps("a", "c", ["a", "b", "c"]))
print(repaint_steps("same", "same", []))
