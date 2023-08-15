## 4.错误：git remote: Permission to denied

### 1.出错内容如下：

```
D:\GIT\doubango>git push origin quantum6
Username for 'https://github.com': quantum6
Password for 'https://quantum6@github.com':
remote: Permission to DoubangoTelecom/doubango.git denied to quantum6.
fatal: unable to access 'https://github.com/DoubangoTelecom/doubango/': The requ
ested URL returned error: 403
```

### 2.解决方法

1. 配置一下：

```
git config --global user.name quantum6

git config --global user.email quantum6@yeah.net
```

2. 检查是否有多余的凭据，如果有其它github账号的凭据就直接删除
