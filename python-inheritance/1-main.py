#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list2 = MyList()
my_list.append(my_list2)
my_list2.append(0)
my_list2.append(-6)
print(my_list)
my_list.print_sorted()
print(my_list)
