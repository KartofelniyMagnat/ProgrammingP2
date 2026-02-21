import json
import sys


def tokenize(query: str):
    # tokens: ("key", str) or ("idx", int)
    tokens = []
    i = 0
    n = len(query)

    while i < n:
        ch = query[i]

        if ch == ".":
            i += 1
            continue

        if ch == "[":
            j = i + 1
            if j >= n:
                return None

            # parse integer index
            sign = 1
            if query[j] == "-":
                sign = -1
                j += 1

            if j >= n or not query[j].isdigit():
                return None

            num = 0
            while j < n and query[j].isdigit():
                num = num * 10 + (ord(query[j]) - 48)
                j += 1

            if j >= n or query[j] != "]":
                return None

            tokens.append(("idx", sign * num))
            i = j + 1
            continue

        # parse key until '.' or '['
        j = i
        while j < n and query[j] not in ".[":
            j += 1
        key = query[i:j]
        if key == "":
            return None
        tokens.append(("key", key))
        i = j

    return tokens


def resolve(root, query: str):
    tokens = tokenize(query)
    if tokens is None:
        return None, False

    cur = root
    for typ, val in tokens:
        if typ == "key":
            if isinstance(cur, dict) and val in cur:
                cur = cur[val]
            else:
                return None, False
        else:  # idx
            if isinstance(cur, list) and 0 <= val < len(cur):
                cur = cur[val]
            else:
                return None, False

    return cur, True


def compact_json(v):
    return json.dumps(v, ensure_ascii=False, separators=(",", ":"))


def main():
    root = json.loads(sys.stdin.readline().strip())
    q = int(sys.stdin.readline().strip())

    for _ in range(q):
        query = sys.stdin.readline().rstrip("\n")
        value, ok = resolve(root, query)
        print(compact_json(value) if ok else "NOT_FOUND")


if __name__ == "__main__":
    main()