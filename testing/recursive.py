def add_one(num):

    if num >= 9:
        print("in here")
        return num + 1

    print("Out here")
    total = num + 1
    print(total)
    print("after print")

    return add_one(total)


add_one(0)
