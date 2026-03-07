import sys


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    ax, ay = float(data[0]), float(data[1])
    bx, by = float(data[2]), float(data[3])

    # Reflect B across the x-axis: B' = (bx, -by)
    bpx, bpy = bx, -by

    # Line from A to B' intersects y=0 at the reflection point.
    # A + t*(B' - A), solve ay + t*(bpy - ay) = 0
    denom = ay + by  # ay - bpy == ay + by
    eps = 1e-12

    if abs(denom) < eps:
        # Degenerate/undefined in typical reflection setting.
        # If both points are on the mirror, any point on the mirror works.
        if abs(ay) < eps and abs(by) < eps:
            rx = ax
        else:
            # Fallback: choose midpoint projection on the mirror.
            rx = (ax + bx) / 2.0
    else:
        t = ay / denom
        rx = ax + t * (bpx - ax)

    print(f"{rx:.10f} 0.0000000000")


if __name__ == "__main__":
    main()