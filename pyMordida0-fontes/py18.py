s = "parabens!"
l = list(s)
l2 = [ord(x) for x in l]
l3 = [chr(x) for x in l2]
s2 = "".join(l3)

print(s)
print(l)
print(l2)
print(l3)
print(s2)
