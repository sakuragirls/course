from re import I
import telnetlib
from unicodedata import name


list=[]

def menu():
    print('1:添加信息')
    print('2:查询信息')
    print('3:查询所有信息')
    print('4:删除信息')
    print('5:更改号码')
    
    
def add():
    name=input('请输入名字')
    phone=input('请输入电话号码')
    dict1={'name':name,'phone':phone}
    list.append(dict1)
    print(list)
    
def search():
    key=input('请输入姓名')
    for item in list:#遍历列表中所有字典
        if key in item['name']:#如果遍历到列表中的字典的键匹配到输入name的值
            print('电话号码:{}'.format(item['phone']))
            
def showall():
    for item in list:#遍历列表中所有字典
         print('姓名:{},电话号码:{}'.format(item['name'],item['phone'])) #item['name'],item['phone']分别是显现键name，phone对应的值
   #就是将字典中name与phone的值全部打印出来      
         
def delete():
    i=0
    deletes=input('请输入要删除的名字')
    for item in list:#遍历列表中所有字典
        i=i+1 #每循环一次就加1，用于统计被删除元素的序数
        if deletes in item['name']: #检测输入名字在列表中有匹配的名字；
            del list[i-1] #i为序数，而下标从0开始；所以i-1才能得出被删除元素的下标，删除目标所在字典
            print(list)
        
        else:
            print('没有')

def alter():
    phone=input('请输入要更改的号码')
    name=input('请输入要修改的姓名')
    i=0
    for item in list:
        i+=1
        if name in item['name']:
            list[i-1]['phone']=phone
            
            
  
         
while True:
    menu()
    xu=int(input('请输入序号'))
    if xu==1:
        add()
    
    elif xu==2:
        search()
        
    elif xu==3:
        showall()
        
        
    elif xu==4:
        delete()
        
    elif xu==5:
        alter()
        
    else:
        print('请再输入一遍')
            
            

    