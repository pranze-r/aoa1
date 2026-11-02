def activity_selection(start, finish):
    n = len(start)

    activities = []

    for i in range(n):
        activities.append((start[i], finish[i], i + 1))

    activities.sort(key=lambda x: x[1])

    selected = []

    selected.append(activities[0])

    last_finish = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

result = activity_selection(start, finish)

print("Selected Activities:")

for activity in result:
    print("Activity", activity[2],
          "Start:", activity[0],
          "Finish:", activity[1])

print("Maximum Activities:", len(result))