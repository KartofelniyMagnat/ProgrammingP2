import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    q = int(data[0])
    g = 0
    n = 0

    idx = 1
    for _ in range(q):
        scope = data[idx]
        val = int(data[idx + 1])
        idx += 2

        if scope == "global":
            g += val
        elif scope == "nonlocal":
            n += val
        # local -> ignore

    print(g, n)

if __name__ == "__main__":
    main()