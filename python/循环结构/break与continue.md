## 1.break与continue 介绍

break与continue是专门在循环中使用的关键字

1. break:某一条件满足时，退出循环，不再执行重复的代码。

2. continue:某一条件满足时，不执行后续重复的代码。

```
i=0
while i<10:
    if i==3: #当i循环到3时，退出循环
        break    
print(i)
i=i+1
```

#结果
0
1
2

```
i=0
while i<10:
    if i==3: #当i循环到3时，退出循环
        i=i+1 #可能会造成死循环
        continue
     print(i)
```