def has_chore_loop(chores: dict[int, list[int]]) -> bool:
    if not chores:
        return False

    prev_keys = []
    for key, value in chores.items():
        if value:
            prev_keys.append(key)
        for k in prev_keys:
            if k in value:
                return True
    
    return False


def has_chore_loop2(chores: dict[int, list[int]]) -> bool:
    # Three states per node, tracked via two sets instead of an enum for simplicity:
    #   - in `visiting`: currently on the DFS recursion stack (gray) — seeing it
    #     again means we found a back-edge, i.e. a cycle.
    #   - in `done`: fully explored (black) — safe, no need to recheck it.
    # Anything in neither set is "unvisited" (white).
    visiting = set()
    done = set()

    def dfs(node):
        # If this node is already on the current path, we've looped back — cycle found.
        if node in visiting:
            return True
        # Already fully explored from a previous DFS root — no cycle through here.
        if node in done:
            return False

        # Mark as "on the current path" before exploring its neighbors.
        visiting.add(node)

        # A chore may point to a number with no outgoing arrows or that isn't
        # even a key — .get(node, []) treats that as "no neighbors", path ends.
        for neighbor in chores.get(node, []):
            if dfs(neighbor):
                return True

        # Done exploring this node's branch with no cycle found — pop it off
        # the current path and mark it permanently safe.
        visiting.remove(node)
        done.add(node)
        return False

    # Every key is a potential cycle entry point (handles disconnected parts).
    for chore in chores:
        if chore not in done:
            if dfs(chore):
                return True

    return False


print(has_chore_loop({1: [2], 2: [3], 3: []}))
print(has_chore_loop({1: [2], 2: [3], 3: [1]}))
print(has_chore_loop({1: [1]}))
print(has_chore_loop({0: [1, 2], 1: [3], 2: [3], 3: []}))
print(has_chore_loop({}))
