from math import ceil, floor


def swap_list(list):
    length = len(list)
    mid = int((length-1)/2)
    temp = list[mid]
    list[mid] = list[length-1]
    list[length-1] = temp
