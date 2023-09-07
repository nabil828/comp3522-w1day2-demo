# int is immutable
def main():
    x = 5
    print(hex(id(x)))
    add_5(x)
    print(x)


def add_5(a):
    print(hex(id(a)))
    a = a + 5
    print(hex(id(a)))


main()


# a list in python is mutable
def main2():
    a_list = [1, 2, 3]
    add_5_to_alist(a_list)
    print(a_list)


def add_5_to_alist(a_param):
    a_param.append(5)


main2()


# if we want to actually modify x in main, we can return the new value
# x = changeX(x)

def main3():
    x = 5
    x = add_5v2(x)
    print(x)


def add_5v2(a):
    a = a + 5
    return a


main3()


# a list in python is mutable
def main4():
    a_list = [1, 2, 3]
    add_5_to_alistv2(a_list)
    print(a_list)


def add_5_to_alistv2(a_param):
    a_param.append(5)
    # rebinding a_param to a new list
    a_param = []  # this is a new list, not the same as the one in main
    a_param.append(6)


main4()


# if we want to actually modify a_list in the main, we can return a  new value
# def main4():
#   a_list = [1, 2, 3]
#   a_list = add_5_to_alistv2(a_list)
#   print(a_list)

# def add_5_to_alistv2(a_param):
#   a_param.append(5)
#   # rebinding a_param to a new list
#   a_param = [] # this is a new list, not the same as the one in main
#   a_param.append(6)
#   return a_param


def main5():
    a_list = [1, 2, 3]
    for x in a_list:
        x = x + 5
    print(a_list)

main5()

# if we want to actually modify the elements of the list, 


def main6():
    a_list = [1, 2, 3]
    for x in range(len(a_list)):
        a_list[x] = a_list[x] + 5
    print(a_list)

main6()