import json

def apply_patch(src, patch):
    if isinstance(src, dict) and isinstance(patch, dict):
        res = dict(src)
        for k, v in patch.items():
            if v is None:
                res.pop(k, None)          
            elif k in res and isinstance(res[k], dict) and isinstance(v, dict):
                res[k] = apply_patch(res[k], v)  
            else:
                res[k] = v               
        return res
    return patch

source = json.loads(input().strip())
patch = json.loads(input().strip())

result = apply_patch(source, patch)

print(json.dumps(result, separators=(",", ":"), sort_keys=True))