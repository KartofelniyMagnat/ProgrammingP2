import json

p = json.loads(input().strip())
o = json.loads(input().strip())



for a, b in p.items():
    for c, d in o.items():
        if p[a] != o[c]:
            