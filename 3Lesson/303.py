import sys

triplet_to_digit = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9",
}

digit_to_triplet = {v: k for k, v in triplet_to_digit.items()}

def decode_num(s: str) -> int:
    # s length is multiple of 3
    digits = []
    for i in range(0, len(s), 3):
        tri = s[i:i+3]
        digits.append(triplet_to_digit[tri])
    return int("".join(digits)) if digits else 0

def encode_num(x: int) -> str:
    if x == 0:
        return "ZER"
    out = []
    for ch in str(x):
        out.append(digit_to_triplet[ch])
    return "".join(out)

def main():
    expr = sys.stdin.readline().strip()

    op_pos = -1
    op = None
    for candidate in ("+", "-", "*"):
        p = expr.find(candidate)
        if p != -1:
            op_pos = p
            op = candidate
            break

    left = expr[:op_pos]
    right = expr[op_pos+1:]

    a = decode_num(left)
    b = decode_num(right)

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    else:
        res = a * b

    # Problem statements like this usually guarantee non-negative results
    print(encode_num(res))

if __name__ == "__main__":
    main()