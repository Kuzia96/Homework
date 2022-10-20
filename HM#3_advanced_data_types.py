# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print('Updated list:', lst_d)
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print('Anna has {} apples and {} peaches'.format(3, 2))
# 6. By passing index numbers into the curly braces.
print('Anna has {1} apples and {0} peaches'.format(3, 2))
# 7. By using keyword arguments into the curly braces.
print('Anna has {apple} apples and {peach} peaches'.format(apple =3, peach =2))
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {apple:5} apples and {peach:3} peaches.'.format(apple =3, peach =2))
# 9. With f-strings and variables
apple = 3
peach = 2
print(f"Anna has {apple} apples and {peach} peaches.")
# 10. With % operator
print("Anna has %(apples)s apples and %(peaches)s peaches." % {"apples": apple, "peaches": peach})
# 11*. With variable substitutions by name (hint: by using dict)
dict_a = {"apples": 3, "peaches": 2}
print("Anna has {} apples and {} peaches".format(dict_a["apples"], dict_a["peaches"]))

# Comprehensions:
# # (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
# #
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
lst = [num**2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)
# 13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
# 14. Convert (3) to dict comprehension.
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)

# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
# 15*. Convert (4) to dict comprehension.
d = {num: num**2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)

# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# 16. Convert (5) to regular for with if.
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
print(d)

# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# 17*. Convert (6) to regular for with if-else.
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
    else:
        d [num] = num
print(d)

# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y

# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
# 19*. Convert (8) to regular function
def foo(x, y, z):
    if x > y and x > z:
        return z
    else:
        return y

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

# 21. Sort lst_to_sort from max to min
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort(reverse=True)
print(lst_to_sort)

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst = list(map(lambda x: x*2, lst_to_sort))
print(lst)

# 23*. Raise each list number to the corresponding number on another list:
# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst = list(map(lambda x, y: x**y, list_A, list_B))
print(lst)

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst)

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
r = range(-10, 10)
negative_numbers = list(filter(lambda o: o < 0, r))
print(negative_numbers)

# 26*. Using the filter function, find the values that are common to the two lists:
# list_1 = [1,2,3,5,7,9]
# list_2 = [2,3,5,6,7,8]
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
s = list(filter(lambda x: x in list_1, list_2))
print(s)
