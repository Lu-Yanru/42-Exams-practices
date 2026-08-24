def plan_barn_days(bookings: list[list[int]]) -> dict:
    current_barn: int = 0
    schedules: dict[int, list[list[int]]] = {}

    for booking in sorted(bookings, key=lambda x: x[0]):
        current_barn = 0
        prev_time = schedules.get(current_barn)
        if prev_time is None:
            schedules[current_barn] = []
            schedules[current_barn].append(booking)
            continue
        while current_barn < len(schedules) + 1:
            prev_time = schedules.get(current_barn)
            if prev_time is None:
                schedules[current_barn] = []
                schedules[current_barn].append(booking)
                break
            elif (prev_time[-1][1]) <= booking[0]:
                schedules[current_barn].append(booking)
                break
            else:
                current_barn += 1

    return {"barns": len(schedules), "schedules": schedules}


def plan_barn_days2(bookings: list[list[int]]) -> dict:
    # Empty input → no barns opened, per the spec's explicit example
    if not bookings:
        return {"barns": 0, "schedules": {}}

    # Sort by start time only. sorted() is stable, so equal-start bookings
    # keep their original arrival order without needing a manual tie-break key.
    ordered = sorted(bookings, key=lambda b: b[0])

    barn_last_end = []   # barn_last_end[i] = end time of barn i's most recent booking
    schedules = {}        # barn_id -> list of [start, end] bookings, in booking order

    for start, end in ordered:
        assigned = None
        # Scan barns in opening order (list order == open order), take the FIRST
        # barn whose last booking ends at or before this booking's start.
        for barn_id, last_end in enumerate(barn_last_end):
            if last_end <= start:
                assigned = barn_id
                break

        if assigned is None:
            # No barn fits — open a new one (index = current barn count)
            assigned = len(barn_last_end)
            barn_last_end.append(end)
            schedules[assigned] = []
        else:
            # Reuse existing barn — update its last-end time
            barn_last_end[assigned] = end

        schedules[assigned].append([start, end])

    return {"barns": len(barn_last_end), "schedules": schedules}


print(plan_barn_days([[1, 4], [2, 5], [6, 8]]))
print(plan_barn_days([[1, 3], [3, 5], [5, 7]]))
print(plan_barn_days([[9, 10], [4, 9], [3, 8]]))
print(plan_barn_days([[1, 5], [1, 3]]))
print(plan_barn_days([]))
