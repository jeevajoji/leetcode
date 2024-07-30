# leetcode premium que
def encode(strs): 
    res = ""
    for s in strs:
        res += "#" + s
    return res
s=encode(["neet","code","love","you"])
def decode(s):
    res=s.split("#")
    return res[1:]
print(decode(s))