def simple_gen():
    r = 0
    while True:
        n = yield r
        print(type(n), n)
        r += 1

g = simple_gen()
r1 = g.send(None)
print("start r1:", r1)

for i in range(10):
    r1 = g.send(i)
    print(r1)