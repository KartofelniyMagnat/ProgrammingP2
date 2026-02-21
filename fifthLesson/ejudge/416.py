import sys
from datetime import datetime, timezone, timedelta


def parse_moment(line: str) -> datetime:
    # Format: YYYY-MM-DD HH:MM:SS UTC±HH:MM
    line = line.strip()
    date_part, time_part, tz_part = line.split()

    y, m, d = map(int, date_part.split("-"))
    hh, mm, ss = map(int, time_part.split(":"))

    off = tz_part[3:]  # +HH:MM or -HH:MM
    sign = 1 if off[0] == "+" else -1
    oh, om = map(int, off[1:].split(":"))
    tz = timezone(timedelta(hours=sign * oh, minutes=sign * om))

    return datetime(y, m, d, hh, mm, ss, tzinfo=tz)


def main():
    s = sys.stdin.readline()
    e = sys.stdin.readline()
    if not s or not e:
        return

    start_utc = parse_moment(s).astimezone(timezone.utc)
    end_utc = parse_moment(e).astimezone(timezone.utc)

    duration = int((end_utc - start_utc).total_seconds())
    print(duration)


if __name__ == "__main__":
    main()