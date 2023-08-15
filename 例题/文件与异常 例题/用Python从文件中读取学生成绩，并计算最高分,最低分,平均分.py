
#文件内容
"""
李明,34
阿萨,45
合集,89

"""



def compute_score():
    scores = [] #存放学生成绩的列表
    #将文件中的学生信息一行一行的遍历
    with open("d://py2.txt", encoding="utf8") as fin:
        for line in fin:
            line = line.strip() #去除每一行开头的空格
            fields = line.split(",") #将每一行的学生信息用,分割,存放在列表中,例如['合集',89]
            scores.append(int(fields[-1]))#将学生成绩添加到score中,int将list类型转换为int类型
    max_score = max(scores) #用max计算列表中的最大值
    min_score = min(scores) #用max计算列表中的最小值
    avg_score = round(sum(scores) / len(scores), 2) #round计算列表的平均值,保留两位小数
    print("最高分：" + str(max_score) +
      "\n" + "最低分：" + str(min_score) +
      "\n" + "平均分：" + str(avg_score))

compute_score()














#参考文献
"""
https://zhuanlan.zhihu.com/p/546290921
"""