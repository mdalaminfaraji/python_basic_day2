numbers=[234, 45,56,67,67,78,8,78,78]
numbers.append(1)
print(numbers)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
if "v" in mylist:
  print("Yes")
else:
  print("No")

# for i in range(len(thislist)):
#   print(thislist[i])\

# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# [print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# newlist = [x for x in fruits if "a" in x]
# newlist = [x for x in fruits if x != "apple"]
# newlist = [x for x in fruits]
# newlist = [x for x in range(10) if x!=0]
# newlist = [x.upper() for x in fruits]
# newlist = ['hello' for x in fruits]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# fruits.sort()

# print(fruits)
# thislist1 = [100, 50, 65, 82, 23]
# thislist1.sort(reverse=True)
# print(thislist1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)