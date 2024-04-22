


ids = []

for number in input("\nTo choose, put a [space] between every number(ex: 1 2 5 6):\n").split(" "):

    ids.append(int(number))
    print(ids[-1])
    print(type(ids[-1]))