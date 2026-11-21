# Q6 - Nested Data: Railway Timetable

timetable = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Katpadi", "08:20", "08:25"),
            ("Bengaluru", "11:00", "11:10"),
        ],
        "days": {"Mon", "Wed", "Fri"},
    },
    "12602": {
        "name": "City Express",
        "stops": [
            ("Chennai", "07:00", "07:10"),
            ("Arakkonam", "08:00", "08:05"),
            ("Katpadi", "09:30", "09:35"),
        ],
        "days": {"Tue", "Thu", "Sat"},
    },
    "12603": {
        "name": "Southern Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Katpadi", "11:30", "11:35"),
            ("Salem", "14:00", "14:10"),
        ],
        "days": {"Mon", "Tue", "Thu"},
    },
    "12604": {
        "name": "Western Express",
        "stops": [
            ("Chennai", "10:00", "10:10"),
            ("Jolarpettai", "12:00", "12:05"),
            ("Bengaluru", "14:30", "14:40"),
        ],
        "days": {"Wed", "Fri", "Sun"},
    },
    "12605": {
        "name": "Delta Express",
        "stops": [
            ("Chennai", "12:00", "12:10"),
            ("Salem", "15:00", "15:10"),
            ("Coimbatore", "17:30", "17:40"),
        ],
        "days": {"Mon", "Wed", "Sat"},
    },
}


def find_trains(station, day):
    result = []
    for number, train in timetable.items():
        if day in train["days"]:
            for stop in train["stops"]:
                if stop[0] == station:
                    result.append((number, train["name"], stop[2]))
    return sorted(result, key=lambda x: x[2])


if __name__ == "__main__":
    print("Trains at Katpadi on Mon:", find_trains("Katpadi", "Mon"))
    print("3rd station departure of 12601:", timetable["12601"]["stops"][2][2])
