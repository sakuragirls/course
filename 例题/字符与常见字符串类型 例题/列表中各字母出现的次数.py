
"""
{'元素1':'元素1个数','元素2':'元素2个数',...}
"""

result=['java','python','perl','python','java','java']
result_dict={}#用空字典来统计各元素个数

for i in result: #将列表result的元素遍历
#如果遍历的元素在字典中不存在，则添加进去
    if i not in result_dict: 
        result_dict[i]=1
    
    else:
        result_dict[i]+=1
        
print(result_dict)

#结果
"""
{'java': 3, 'python': 2, 'perl': 1}
"""


#统计一个数据使用i=0,i++计数,统计多个则使用for遍历加if... not in