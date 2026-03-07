import sys
import importlib


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    q = int(data[0])
    out = []
    idx = 1

    for _ in range(q):
        module_path = data[idx]
        attr_name = data[idx + 1]
        idx += 2

        try:
            mod = importlib.import_module(module_path)
        except Exception:
            out.append("MODULE_NOT_FOUND")
            continue

        if not hasattr(mod, attr_name):
            out.append("ATTRIBUTE_NOT_FOUND")
            continue

        attr = getattr(mod, attr_name)
        out.append("CALLABLE" if callable(attr) else "VALUE")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()