list1 = [1,8,9,6,7]
max_num = list1[0]
for i in range(1,len(list1)):
    if list1[i]>max_num:
        max_num =list1[i]
print("The maximum of the given list is",max_num)