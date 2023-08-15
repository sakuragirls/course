## 2.github 生成ssh密钥

## 1.前言

将电脑生成的密钥粘贴进自己GitHub中，那么就可以将本地

### 2.在 github 上添加 SSH key 的步骤：

**第一步：如果能进入到.ssh文件目录下 ，则证明，之前生成过.ssh秘钥，可以直接使用里面的秘钥。**

1. 如果能进入到.ssh文件目录下 ，则证明，之前生成过.ssh秘钥，可以直接使用里面的秘钥。如果不能进入到.ssh文件目录下，则：检测下自己之前有没有配置：

```lua
git config user.name和git config user.email（直接分别输入这两个命令）
```

2. 如果之前没有创建，则执行以下命令：

```verilog
git config –global user.name ‘xxxxx’ 
git config –global user.email ‘xxx@xx.xxx’
```

3. 生成秘钥

```undefined
ssh-keygen -t rsa -C ‘上面的邮箱’
```

代码参数含义：

-t 指定密钥类型，默认是 rsa ，可以省略。  
-C 设置注释文字，比如邮箱。  
-f 指定密钥文件存储文件名。

4. 接着按3个回车

```vbnet
[root@localhost ~]# ssh-keygen -t rsa       <== 建立密钥对，-t代表类型，有RSA和DSA两种
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):   <==密钥文件默认存放位置，按Enter即可
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase):     <== 输入密钥锁码，或直接按 Enter 留空
Enter same passphrase again:     <== 再输入一遍密钥锁码
Your identification has been saved in /root/.ssh/id_rsa.    <== 生成的私钥
Your public key has been saved in /root/.ssh/id_rsa.pub.    <== 生成的公钥
The key fingerprint is:
SHA256:K1qy928tkk1FUuzQtlZK+poeS67vIgPvHw9lQ+KNuZ4 root@localhost.localdomain
The key's randomart image is:
+---[RSA 2048]----+
|           +.    |
|          o * .  |
|        . .O +   |
|       . *. *    |
|        S =+     |
|    .    =...    |
|    .oo =+o+     |
|     ==o+B*o.    |
|    oo.=EXO.     |
+----[SHA256]-----+
```

最后在.ssh目录下(C盘用户文件夹下)得到了两个文件：id_rsa（私有秘钥）和id_rsa.pub（公有密钥）

## 

**第二步、如果想登陆远端，则需要将rsa.pub里的秘钥添加到远端**

首先，去.ssh目录下找到id_rsa.pub这个文件夹打开复制全部内容。

1. 登录GitHub，进入你的Settings

![](https://img2020.cnblogs.com/blog/1833224/202003/1833224-20200323114403508-625146572.png)

2. 会看到左边这些目录，点击SSH and GPG keys

![](https://img2020.cnblogs.com/blog/1833224/202003/1833224-20200323114608488-786274780.png)

3. 创建New SSH key

![](https://img2020.cnblogs.com/blog/1833224/202003/1833224-20200323114634462-1837490460.png)

4. 粘贴你的密钥到你key输入框中

![](https://img2020.cnblogs.com/blog/1833224/202003/1833224-20200323114651978-1318462262.png)

5.点击Add SSH key  
6.再弹出窗口，输入你的GitHub密码，点击确认按钮。  
7.到此，就大功告成了。

## 第四步 测试。

再使用下面的命令测试是否成功

```css
ssh -T git@github.com
```

然后会看到这个内容，输入yes即可  
![](https://img2020.cnblogs.com/blog/1833224/202003/1833224-20200323114903108-1714804783.png)

最后，如看到以下信息，那么就完美了。成功了！！！  
![](https://img2020.cnblogs.com/blog/1833224/202003/1833224-20200323114955428-1355713122.png)
