# 20200904 HOW TO USE GIT

## git的基本结构
```
Remote--------------------------------> Workspace
      -------> Repository----Index---->     
      ------->           <----    <----
```

1、Remote：远程仓库，像github就是一个远程仓库。
-->github

2、Repository:本地仓库，通过git clone将远程仓库的代码下载到本地。代码库的元数据信息在根目录下的.git目录下。
-->local repository, git commit

3、Index：暂存区，指的是.git目录下的index文件。
-->index, git add

4、Workspace：工作空间，就是我们写代码的目录。
-->workspace

## 安装与配置
### Linux
1、unbuntu 与 debian 可以使用**sudo apt-get install git**安装。
2、其他系统可以通过官网下载解压安装，也可以使用yum查看安装。

### MacOSX
1、homebrew
2、xcode集成了git，可以在perference中配置。

### windows
1、gitbash

## 开始使用git仓库
1、初始化git仓库
```
git init # 将当前目录初始化为git仓库
```
\# windows的记事本使用了0xefbbbf去标记一个utf8文件，因此会导致各种奇怪的问题。

2、本地添加->添加到暂存区
```
git add filename # 提交指定文件
git add . # 提交全部文件
```

3、本地提交->覆盖到仓库
```
git commit -m changed a readme file"
```

## 状态管理
1、查看工作区状态，确认是否有文件被修改
```
git status
```

2、查看具体修改内容
```
git diff
```

## 版本回退
1、先通过查看历史记录，定位回溯的版本节点
```
git log
git log --pretty=oneline # one line
```

2、回溯版本
使用`HEAD`表示当前版本，往前追溯，上一个版本是`HEAD^`，上上个版本是`HEAD^^`，当追溯版本过多时，试试`HEAD~100`

```
git reset --hard HEAD~10
```

3、回溯回溯版本（禁止套娃）
找到/确定版本的commit id，然后使用`git reset`。
```
git reset --hard 1024adb # 不用写全
```
4、查看历史操作(命令历史)
```
git reflog
```

## 工作区与暂存区（workspace and stage）
1、逻辑
```
            add         commit
workspace ----> stage ----> master
```

2、管理修改
使用如下命令查看工作区与版本库中最新版本的差别。
```
git diff HEAD -- readme.txt
```
3、撤销修改-工作区
使用`git check -- filename`可以丢弃工作区的修改，只能撤销到工作区位置，对暂存区内容无能无力。

4、撤销修改-暂存区
使用`git reset HEAD filename`可以撤销（unstage）暂存区的修改。

5、撤销修改-仓库
没什么办法。。。只要没有push就还有救，push了就人没了，希望人没事.jpg

## 删除文件
1、确认删除
`rm filename`->`git rm`->`git commit -m "delete"`

2、误操作
`git checkout -- filename`

3、同步到远程仓库
`git push origin xxx`

## 新建分支
`git checkout -b newbranch` = `git branch newbranch` + `git checkout inewbranch`

切换分支：`git checkout inewbranch`

## 远程与本地仓库交互汇总
1. `git pull -p`可以从远程同步被删除的信息到本地（删除本地文件）
2. `git remote show orgin`查看remote地址，远程分支，还有本地分支与之对应的关系信息。
3. `git pull origin xxx` = `git fetch orgin xxx` + `git merge origin xxx`
4. 更多远程操作，可以查阅`git remote -h`
5. 合并分支操作