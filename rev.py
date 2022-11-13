def reverse_list(list):
    ans = []
    for x in list:
        ans.insert(0, x)
    list = ans
    print(list)
    return list


reverse_list([0.9])
