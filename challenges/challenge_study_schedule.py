def study_schedule(permanence_period, target_time):
    students_online = 0
    if not target_time:
        return None
    for start_time, end_time in permanence_period:
        if type(start_time) != int:
            return None
        if type(end_time) != int:
            return None
        if start_time <= target_time <= end_time:
            students_online += 1
    return students_online
