def hi():
    def decor(name):
        print(f"does this work{name}")
    print('hi')
    decor("bob")


hi()
