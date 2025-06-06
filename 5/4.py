def modify_string(s):
    if s.startswith("abc"):
        s = "www" + s[3:]
    else:
        s = s + "zzz"
    return s

print(modify_string("abcdef"))
print(modify_string("hello"))   