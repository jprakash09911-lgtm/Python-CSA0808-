
# TASK 5 - Single Script

def read_attendance():
    return [("101", "P"), ("102", "A"), ("103", "P")]


def calculate_percentage(records):
    total = len(records)
    present = sum(1 for r in records if r[1] == "P")

    if total == 0:
        return 0

    return (present / total) * 100


def write_report(records):
    print("Attendance Report")

    for reg, status in records:
        print(reg, status)

    print("Attendance Percentage:",
          calculate_percentage(records))


def main():
    records = read_attendance()
    write_report(records)


if __name__ == "__main__":
    main()
