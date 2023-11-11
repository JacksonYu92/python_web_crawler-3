import json

d = {
    "k1": "v1",
    "k2": "v2"
}
ret = json.dumps(d, separators=(",", ":"))
print(repr(ret))
