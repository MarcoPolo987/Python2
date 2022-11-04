import collections


import _collections_abc


def sort_dictionary(dict):
    keys = dict.keys()
    tlist = []
    for x in keys:
        tlist.append(dict[x][1])
        # tlist.append(temp)
    tlist.sort()
    for y in keys:
        for x in (0, len(tlist)-1, 1):
            print(dict.get(y, x))
    print(dict)
    print(tlist)


sort_dictionary({"Tom": (5464512, 24), "Sara": (
    5446987, 32), "Mary": (1557896, 20)})
