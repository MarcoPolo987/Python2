

import operator


def calculator(string):
    sp = []
    nums = {"-": operator.sub, "+": operator.add, "*": operator.mul,
            "**": operator.pow, "//": operator.floordiv, "/": operator.truediv}
    ans = 0
    num = []

    def get_number(varstr):
        s = ""
        for c in varstr:
            if not c.isnumeric():
                break
            s += c
        return (int(s), len(s))
    for i in range(0, len(string), 1):

        if (not (string[i].isnumeric() or string[i] == " ")):
            num.append(string[temp:i])
            temp = i+1
    for x in string:
        if (not (x == " ")):
            sp.append(x)
    for x in sp:
        if x in nums.keys():
            operator_func = nums.get(x)
            left = 1
            right = 1
            ans += operator_func(left, right)
    print(sp)
    print(num)
    print(ans)


def main():
    print(calculator('(10+ 11 * 12)'))


main()
