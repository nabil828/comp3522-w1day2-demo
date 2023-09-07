
# sequences in python: lists, tuples, sets, dictionaries

# lists are mutable and ordered

# lists
a_list = [1, 2, 3, 4, 5]
x_list =[{1,2,3}, (2,3,5), "asdas", 12312, {'a':1, 'b':2}]

# common operations on lists
# indexing
print(a_list[0])
print(a_list[-1])
print(a_list[1:3])
print(a_list[1:])
print(a_list[:3])
print(a_list[::2])
print(a_list[::-1])

# append
a_list.append(6)
print(a_list)

# insert
a_list.insert(0, 999)
a_list.insert(0, 999)
print(a_list)

# pop
a_list.pop()
print(a_list)

# remove
a_list.remove(999)
print(a_list)

# reverse
a_list.reverse()
print(a_list)


# sort
# a_list.sort()
# print(a_list)

# you can sort a copy of the list
sorted_list = sorted(a_list)
print(sorted_list)

# how to iterate over a list
for item in a_list:
    print(item)

# length
print(len(a_list))

# check if an element contained in a list
print(1 in a_list)
print(998 in a_list)
print(a_list.__contains__(1))
print(6 not in a_list)


# index
print(a_list.index(1))


# tuples are immutable and ordered
a_tuple = (1, 2, 3, 4, 5)

# a_tuple.append(6) # error
# a_tuple.remove(1) # error


# sets are mutable and unordered and unique
a_set = {1, 2, 3, 4, 5}
a_set.add(6)
print(a_set)
a_set.add(6)
print(a_set)


# dictionaries are mutable and unordered and unique keys
a_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'a': 4}

# we need dictionaries real life entity like a person
a_person ={
    'name': 'John',
    'age': 30,
}

# or we can we can use dictionaries to represent a collection of these entities
people = {
    'John': {
        'age': 30,
        'Address': '123 Main St'
    },
    'Jane': {
        'age': 29,
        'Address': '123 Main St'
    }
}

print(a_dict)

# a_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'a': 4}

# get
print(a_dict.get('a'))

# update or add
a_dict['d'] = 5
print(a_dict)

a_dict.update({'e': 6})
print(a_dict)

# delete
del a_dict['a']

# how to iterate over a dictionary
for key in a_dict:
    print(key)

print(type(a_dict.items()))
for key, value in a_dict.items(): # a_dict.iteritems() is a view object
    print(key, value)

# we can also iterate over the values
for value in a_dict.values():
    print(value)

# iterate and update
for key in a_dict:
    a_dict[key] = a_dict[key] + 1

# get method with a default value
print(a_dict.get('a', 0))
