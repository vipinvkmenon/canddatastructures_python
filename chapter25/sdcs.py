b = [0,1,2,3,4,5]
c = b
c[0] = 10
print(b)

print("ids a of a and b")
print(id(b[2])),
print(id(c[3]))