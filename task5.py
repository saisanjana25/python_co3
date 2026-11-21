# Q5 - List Comprehension: Cleaning Sensor Readings

def clean_loop(readings):
    celsius = []
    for c in readings:
        if -50 <= c <= 50:
            celsius.append(c)
    return celsius


def clean_comp(readings):
    return [c for c in readings if -50 <= c <= 50]


def clean_map_filter(readings):
    return list(filter(lambda c: -50 <= c <= 50, readings))


def fahrenheit(readings):
    return [(c * 9 / 5) + 32 for c in readings if -50 <= c <= 50]


def alarm_minutes(readings):
    return [i for i, c in enumerate(readings) if -50 <= c <= 50 and not (2 <= c <= 8)]


if __name__ == "__main__":
    sample_readings = [4.5, 6.0, -999, 10.2, 3.8, 75.0, 1.5]
    temps_dict = {i: c for i, c in enumerate(sample_readings) if -50 <= c <= 50}
    temps_set = {c for c in sample_readings if -50 <= c <= 50}

    print("Cleaned (comp):", clean_comp(sample_readings))
    print("Fahrenheit:", fahrenheit(sample_readings))
    print("Alarm minutes:", alarm_minutes(sample_readings))
    print("Valid dict:", temps_dict)
    print("Valid set:", temps_set)
