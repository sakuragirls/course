#为什么要序列化
"""
我们可以将字符串写入一个文件中，如果是一个对象(元组,字典,列表等等)无法直接写入一个文件中，那么就必须对对象进行序列化，才能写入这个文件中

"""


#序列化方法
"""
使用json模块的dump与dumps方法，将一个对象进行序列化

dumps方法就是将对象转换成字符串,而方法本身不能将数据写入到文件中
"""

#将列表写入文件中
"""
import json
list=[1,2,3,4]
name=json.dumps(list) #将list转换为字符串
#将列表list写入创建的文件jk.txt
with open('e://jk.txt','w') as f:
    f.write(name)
    f.close()
"""    
    
#反序列化
"""
就是将json字符串转换为对象

使用json模块的load方法将json字符串转换为对象
"""  
import json
with open('e://jk.txt','r') as f:
    content=f.read()
    result=json.loads(content)
    print(result)
    f.close()
    #结果
    """
    [1, 2, 3, 4]
    """