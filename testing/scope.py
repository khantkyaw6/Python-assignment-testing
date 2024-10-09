name = "Kay"

count = 1


def greeting():

    color = "blue"
    global count
    count += 1
    print(count)
    print(name)
    print(color)

    def another():
        nonlocal color
        color = "red"

        print(color)

    another()
    print(color)


greeting()

print(count)
