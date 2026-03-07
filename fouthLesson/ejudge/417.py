import math
import sys

def dot(ax, ay, bx, by):
    return ax * bx + ay * by

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    r = float(data[0])
    ax, ay = float(data[1]), float(data[2])
    bx, by = float(data[3]), float(data[4])

    dx, dy = bx - ax, by - ay
    seg_len = math.hypot(dx, dy)

    # Degenerate segment
    if seg_len == 0.0:
        inside = (ax * ax + ay * ay) <= r * r + 1e-12
        print(f"{0.0:.10f}")
        return

    # Solve |A + t d|^2 = r^2 for t
    a = dot(dx, dy, dx, dy)
    b = 2.0 * dot(ax, ay, dx, dy)
    c = dot(ax, ay, ax, ay) - r * r

    disc = b * b - 4.0 * a * c

    # No intersection with circle boundary
    if disc < 0.0:
        if c <= 0.0:  # A is inside and never leaves
            print(f"{seg_len:.10f}")
        else:
            print(f"{0.0:.10f}")
        return

    sqrtD = math.sqrt(disc)
    t1 = (-b - sqrtD) / (2.0 * a)
    t2 = (-b + sqrtD) / (2.0 * a)
    if t1 > t2:
        t1, t2 = t2, t1

    # Inside part is t in [t1, t2], intersect with segment [0, 1]
    left = max(0.0, t1)
    right = min(1.0, t2)
    inside_param_len = max(0.0, right - left)

    ans = seg_len * inside_param_len
    print(f"{ans:.10f}")

if __name__ == "__main__":
    main()