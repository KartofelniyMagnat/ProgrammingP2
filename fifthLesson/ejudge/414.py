import sys
from datetime import datetime, timezone, timedelta


def parse_moment(line: str) -> datetime:
    # Format: YYYY-MM-DD UTC±HH:MM
    line = line.strip()
    if not line:
        raise ValueError("empty line")

    date_part, tz_part = line.split()
    y, m, d = map(int, date_part.split("-"))

    if not tz_part.startswith("UTC") or len(tz_part) < 4:
        raise ValueError("bad timezone")

    off = tz_part[3:]  # like +03:00 or -05:30
    sign = 1
    if off[0] == '+':
        sign = 1
    elif off[0] == '-':
        sign = -1
    else:
        raise ValueError("bad offset sign")

    hh, mm = map(int, off[1:].split(":"))
    offset = timedelta(hours=sign * hh, minutes=sign * mm)
    tz = timezone(offset)

    # local midnight in its own timezone
    return datetime(y, m, d, 0, 0, 0, tzinfo=tz)


def main():
    l1 = sys.stdin.readline()
    l2 = sys.stdin.readline()
    if not l1 or not l2:
        return

    t1 = parse_moment(l1).astimezone(timezone.utc)
    t2 = parse_moment(l2).astimezone(timezone.utc)

    delta = t1 - t2
    days = int(abs(delta.total_seconds()) // 86400)
    print(days)


if __name__ == "__main__":
    main()
