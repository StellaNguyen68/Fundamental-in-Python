# Ex7.4
n = eval(input('How many elements in your tuple? '))
list = []
for i in range(0, n-1):
    value = eval(input("Append your tuple: "))
    list.append(value)
tuple = tuple(list)
str = input('Enter the str: ')
print(str, ' appears ', tuple.count(str), ' time(s)')

# # Ex7.2
# list = []
# stop = 1
# while stop == 1:
#     value = eval(input("Append your list: "))
#     list.append(value)
#     stop = eval(input("Do you want to continue? (1:Yes, 0:No) "))

# x = eval(input('Enter a number x: '))
# print('Sum of list: ', sum(list))

# count = list.count(x)
# if count > 0:
#     print(x, ' appears ', count, ' time')
# else:
#     print('There is no ', x, ' in the list')
# # solution 1
# greater = []
# for i in list:
#     if x < i:
#         greater.append(i)
# if len(greater) == 0:
#     print(x, ' is greater than all numbers in the list')
# else:
#     print(x, ' is smaller than: ', greater)
# solution 2??????
# list.sort()
# if x > max(list):
#     print(x, ' is greater than all numbers in the list')
# else:
#     for i in range(0, len(list)-1):
#         if x < list[i]:
#             print(x, ' is smaller than: ', list[i, ])
#         else: break

# # Ex7.1
# list_animals = ['ant', 'bear', 'cat', 'dog','elephant', 'fish', 'goat', 'hippo']
# print('List of animals: ', list_animals)
# print('Number of animals: ', len(list_animals))
# find = input("I want to find:")
# found = find in list_animals
# if found:
#     print('There is a ', find, ' in the list')
# else:
#     print('There is no ', find, ' in the list')
