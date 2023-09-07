# All the example below are extracted from - http://web.stanford.edu/class/archive/cs/cs106a/cs106a.1212/handouts/mutation.html

# Question 1: What will this print?

def main1():
    x = [1, 2, 3]
    y = x
    # does this change impact x?
    y.append(4)
    print(x)


main1()

# OPTIONS
# A. [1, 2, 3]
# B. [1, 2, 3, 4]


# Question 2: Now lets swap the third line for a different way of changing the variable y:

def main2():
    x = [1, 2, 3]
    y = x
    # does this change impact x?
    y = []
    print(x)


main2()

# OPTIONS
# A. [1, 2, 3]
# B. []


# Question 3: What will this print?
def main3():
    my_list = [1, 2, 3]
    for value in my_list:
        # will this change impact my_list?
        value += 5
    print(my_list)


main3()

# OPTIONS
# A. [1, 2, 3]
# B. [6, 7, 8]

# Output:
# [1, 2, 3]
# Here the change to value in the for loop body does not affect my_list.


# Question 4: What will this print?
# parameters are passed via binding
def main4():
    original = [1, 2, 3]
    do_your_thing(original)
    print(original)

# when this function is called, the param_name in do_your_thing
# is "bound" to the same value as original.


def do_your_thing(param_name):
    # mutation change impacts both original and param_name
    param_name.append(4)

    # re-binding will not impact original
    param_name = []

    # param_name and original are no longer bound to the same value
    # so this mutation does not impact the variable "original"
    param_name.append(5)


main4()

# OPTIONS
# A. [1, 2, 3]
# B. [1, 2, 3, 4]


###################################################
# x = change(x) for persistent binding
###################################################


# Question 5: What will this print?
def main5():
    x = 0
    # here is where x = change(x) pattern gets its name
    x = add_five(x)
    print(x)


def add_five(x):
    x += 5
    return x


main5()

# OPTIONS
# A. 0
# B. 5


# Question 6: What will this print?
# fixed using x = change(x) paradigm. Binding change now persists.
def main6():
    x = [1, 2, 3]
    x = add_five(x)
    print(x)


def add_five(x):
    x = [1, 2, 3, 5]
    return x


main6()

# OPTIONS
# A. [1, 2, 3]
# B. [1, 2, 3, 5]


# Question 7: What will this print?
# fixed using a loop over indices
def main7():
    x = [1, 2, 3]
    # switch to a loop over indices
    for i in range(len(x)):
        # this mutation will have persistent changes
        x[i] += 5
    print(x)


main7()

# OPTIONS
# A. [1, 2, 3]
# B. [6, 7, 8]
