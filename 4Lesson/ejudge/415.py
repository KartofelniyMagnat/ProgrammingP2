

import sys
from datetime import datetime, timezone, timedelta


def parse_line(line: str):
    # Format: YYYY-MM-DD UTC±HH:MM
    line = line.strip()
    date_part, tz_part = line.split()
    y, m, d = map(int, date_part.split("-"))

    off = tz_part[3:]  # +HH:MM or -HH:MM
    sign = 1 if off[0] == "+" else -1
    hh, mm = map(int, off[1:].split(":"))
    tz = timezone(timedelta(hours=sign * hh, minutes=sign * mm))

    return y, m, d, tz


def is_leap(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def birthday_day(month: int, day: int, year: int) -> int:
    # Feb 29 rule
    if month == 2 and day == 29 and not is_leap(year):
        return 28
    return day


def birthday_moment_utc(target_year: int, b_month: int, b_day: int, b_tz: timezone) -> datetime:
    d = birthday_day(b_month, b_day, target_year)
    local = datetime(target_year, b_month, d, 0, 0, 0, tzinfo=b_tz)
    return local.astimezone(timezone.utc)


def main():
    b_line = sys.stdin.readline()
    c_line = sys.stdin.readline()
    if not b_line or not c_line:
        return

    by, bm, bd, btz = parse_line(b_line)
    cy, cm, cd, ctz = parse_line(c_line)

    current_utc = datetime(cy, cm, cd, 0, 0, 0, tzinfo=ctz).astimezone(timezone.utc)

    cand_utc = birthday_moment_utc(cy, bm, bd, btz)
    if cand_utc < current_utc:
        cand_utc = birthday_moment_utc(cy + 1, bm, bd, btz)

    t = int((cand_utc - current_utc).total_seconds())

    if t <= 0:
        print(0)
    else:
        # ceil(t / 86400)
        print((t + 86400 - 1) // 86400)


if __name__ == "__main__":
    main()