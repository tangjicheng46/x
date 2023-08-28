def gen1():
    r = -1
    while True:
        n = yield r
        r = n * 2
        if r > 10:
            r = 10

g = gen1()

def test1():
    a = g.send(None)
    for i in range(10):
        a = g.send(i)
        print(a)

if __name__ == "__main__":
    test1()
