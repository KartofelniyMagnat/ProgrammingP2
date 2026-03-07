import math
import sys

EPS = 1e-12

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def dist_origin_to_segment(A, B):
    ax, ay = A
    bx, by = B
    dx, dy = bx - ax, by - ay
    denom = dx*dx + dy*dy
    if denom < EPS:
        return math.hypot(ax, ay)
    t = -(ax*dx + ay*dy) / denom  # projection of origin onto AB
    t = max(0.0, min(1.0, t))
    px, py = ax + t*dx, ay + t*dy
    return math.hypot(px, py)

def norm_angle(a):
    a %= (2.0 * math.pi)
    if a < 0:
        a += 2.0 * math.pi
    return a

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    r = float(data[0])
    A = (float(data[1]), float(data[2]))
    B = (float(data[3]), float(data[4]))

    # If straight segment doesn't enter the circle interior, answer is straight distance
    dmin = dist_origin_to_segment(A, B)
    if dmin >= r - 1e-10:
        print(f"{dist(A, B):.10f}")
        return

    # Otherwise: tangents + arc on circle
    def tangents(P):
        x, y = P
        d = math.hypot(x, y)
        theta = math.atan2(y, x)
        if d <= r + EPS:  # on boundary (or extremely close)
            return [(norm_angle(theta), 0.0)]
        alpha = math.acos(r / d)
        tlen = math.sqrt(max(0.0, d*d - r*r))
        return [(norm_angle(theta + alpha), tlen),
                (norm_angle(theta - alpha), tlen)]

    ta = tangents(A)
    tb = tangents(B)

    best = float("inf")
    for angA, lenA in ta:
        for angB, lenB in tb:
            delta = abs(angA - angB)
            delta = min(delta, 2.0*math.pi - delta)
            total = lenA + lenB + r * delta
            if total < best:
                best = total

    print(f"{best:.10f}")

if __name__ == "__main__":
    main()