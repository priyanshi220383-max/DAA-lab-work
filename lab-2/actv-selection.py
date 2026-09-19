def select_meeting_activities(activities):

    # Sort activities by:
    # 1. Earliest finish time
    # 2. Smaller start time
    # 3. Lexicographically smaller activity ID
    activities.sort(key=lambda x: (int(x[2]), int(x[1]), x[0]))

    selected = []
    last_finish = -1

    # Greedy selection
    for activity in activities:

        activity_id = activity[0]
        start = int(activity[1])
        finish = int(activity[2])

        # Activity is compatible with the last selected activity
        if start >= last_finish:

            if len(selected) == 0:
                reason = "Selected first because it finishes earliest"
            else:
                reason = "Selected because start time is compatible"

            selected.append(
                f"{activity_id} {start} {finish} {reason}"
            )

            last_finish = finish

    # Build the required output
    result = []

    result.append("Activity Selection Report")
    result.append("Selected Activities")
    result.append("Activity Start Finish Reason")

    # Add selected activities
    for activity in selected:
        result.append(activity)

    # Total count
    result.append(f"Total Selected: {len(selected)}")

    # Greedy justification
    result.append(
        "Justification: Greedy selection by earliest finish time maximizes compatible activities"
    )

    return result