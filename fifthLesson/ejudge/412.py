import json

left = json.loads(input().strip())
right = json.loads(input().strip())

MISSING = object()

def jdump(v):

    return json.dumps(v, ensure_ascii=False, separators=(",", ":"))


diffs = []  # list of (path, old_value_or_MISSING, new_value_or_MISSING)


def walk(a, b, path=""):
    # If both are dicts, compare by union of keys
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            new_path = f"{path}.{k}" if path else str(k)
            av = a.get(k, MISSING)
            bv = b.get(k, MISSING)
            if av is MISSING or bv is MISSING:
                diffs.append((new_path, av, bv))
            else:
                walk(av, bv, new_path)
        return

    if a != b:
        diffs.append((path, a, b))


walk(left, right)

diffs.sort(key=lambda x: x[0])

if not diffs:
    print("No differences")
else:
    for pth, oldv, newv in diffs:
        old_s = "<missing>" if oldv is MISSING else jdump(oldv)
        new_s = "<missing>" if newv is MISSING else jdump(newv)
        print(f"{pth} : {old_s} -> {new_s}")
