count=int(input('请输入数字'))
#质数大于1
if count>1:
    for i in range(2,count):
        if count%i==0:
            print('%d不是质数'%(count))
            break #如果检测出输入的数字不是质数，则退出循环
    else:
        print('%d是质数'%(count))
#如果输入的数字小于及等于1，不是质数
else: 
    print('%d不是质数'%(count))