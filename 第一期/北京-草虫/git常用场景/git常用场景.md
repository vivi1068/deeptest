- 从本地提交修改的文件read.txt到远程仓库

	$git add read.txt  #添加文件到缓存区

 	$git commit -m "add read.txt"   #commit并注解

 	$git push  #push 文件到仓库

-- 

- 查看历史记录

 	$git log或$git log --pretty=oneline

-- 

- 如果想回退到上个版本的add

 	$git reset --hard (通过log查看的id)

-- 

- 如果回退后发现不是自己想要的版本，此处有后悔药，请执行如下返回回退前的状态

 	$git reflog

-- 

- 从github上删除仓库

1.进入要删除的仓库，点击“settings”
![](/images/1.png)

2.滑到最下方选择"Delete this repository"
![](/images/2.png)

3.输入要删除的仓库，并同意确定删除即可
![](/images/3.png)

---

- 从github上fork了别人的项目，再同步更新别人提交的最新的代码
有两种方法，一是直接在github页面上进行操作，另一种使用git命令

**在github页面上操作步骤**

1.打开自己的code
![](/images/5.png)

2.选择"New pull request"
![](/images/6.png)

4.选择base fork（自己的仓库和分支），head fork（指的是fork来源的仓库和分支），点击create pull request
注：如果base fork填写目标仓库，head fork填写自己的仓库，就是你向目标推送代码。
![](/images/7.png)

注如果出现下图情况，请点击“compare across forks”在继续执行第4步
![](/images/8.png)

5.输入title，create pull request，在最下方点击“merge pull request”
![](/images/9.png)

**使用git命令操作**

1.打开git命令窗口，cd到仓库根目录
![](/images/10.png)

2.查看远程信息，如果没有远程仓库，使用命令添加远程仓库
![](/images/11.png)

3.从目标仓库同步代码
![](/images/12.png)

4.合并到本地代码仓库
![](/images/13.png)

5.更新并合并到自己远程仓库的代码
![](/images/14.png)

6.向自己远程仓库推送刚才更新的代码
$git push

注：其它命令使用

$git remote remove upstream 删除远程仓库

