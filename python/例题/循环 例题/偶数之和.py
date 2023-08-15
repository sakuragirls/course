
#使用while循环
i=1
result=0 #定义一个记录最终结果的变量
while i<=100: #判断变量i中的数值，是否是一个偶数
    if i%2==0:
        result+=i
    i+=1
print(result)

#使用for循环
result=0#定义一个记录最终结果的变量
for i in range(1,101): #从0遍历到100，range()会对上限减1，所以100+1=101
    if i%2==0:
        result+=i

print(result)