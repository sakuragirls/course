## 2.git 将本地项目关联到远程仓库

## 

### 1.在本地项目根目录进行git初始化

```
git init
```

此时会发现，命令行窗口出现git的master分支字样。

### 2.关联远程仓库

```
git remote add origin  https://xxxxxxxxx.git
```

### 3.查看是否添加成功

```
git remote -v
```

此时已经展示关联好的远程仓库

### 4. 提交代码

```
git add .

git [commit](https://so.csdn.net/so/search?q=commit&spm=1001.2101.3001.7020) -m "一些描述"

git push origin master   或  git push -u origin master
```
