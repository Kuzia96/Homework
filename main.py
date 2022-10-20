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

# 15*. Convert (4) to dict comprehension.
d = {num: num**2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)
