# Q1 - Lists and Slicing: Daily Rainfall Records

def moving_average_naive(readings):
    if len(readings) < 7:
        return []
    result = []
    for i in range(len(readings) - 6):
        total = sum(readings[i:i + 7])
        result.append(total / 7)
    return result


def moving_average_running(readings):
    if len(readings) < 7:
        return []
    window = sum(readings[:7])
    result = [window / 7]
    for i in range(7, len(readings)):
        window += readings[i] - readings[i - 7]
        result.append(window / 7)
    return result


if __name__ == "__main__":
    sample_readings = [12, 0, 5, 18, 22, 4, 0, 9, 14, 3, 0, 7, 11, 2]
    print("Second week (readings[7:14]):", sample_readings[7:14])
    print("Last 7 days (readings[-7:]):", sample_readings[-7:])
    print("Every 7th day (readings[::7]):", sample_readings[::7])
    print("7-day moving average (running):", moving_average_running(sample_readings))
    print("Empty list test:", moving_average_running([]))
    print("Short list (<7) test:", moving_average_running([10, 20, 30]))
