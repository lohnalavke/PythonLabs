print("Списки")
#a
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("а)")
print(a)
print(b)

#b
print("b)", a[1])

#c
b[10] = 200
print("c)", b)

#d
c = a+b
print("d)", c)

#e
d = c[5:18]
print("e)", d)

#f
d.append(300)
d.append(400)
print("f)", d)

#g
print("g)")
print(min(d))
print(max(d))