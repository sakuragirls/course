list=[1,1,2,3,4,5,5]
list1=[]

#如果list中的列表元素在list1中不存在,则将该元素添加进list1中
for list2 in list:
    if list2 not in list1:
        list1.append(list2)

print(list1)