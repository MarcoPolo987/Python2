

def calculator(string):
    m = []
    for x in string:
        if (not (x.isdigit() or x == " ")):
            m.append(x)
        print(m)


def main():
    print(calculator('(10+ 11 * 12)'))


main()
