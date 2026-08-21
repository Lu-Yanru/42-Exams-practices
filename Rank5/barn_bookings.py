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


print(plan_barn_days([[1, 4], [2, 5], [6, 8]]))
print(plan_barn_days([[1, 3], [3, 5], [5, 7]]))
print(plan_barn_days([[9, 10], [4, 9], [3, 8]]))
print(plan_barn_days([[1, 5], [1, 3]]))
print(plan_barn_days([]))
