# GIT -> REMOTE USE(github)
## 远程仓库
### 关联仓库
1、先执行命令生成ssh密钥
```
ssh-keygen -t rsa -C "youremail@example.com"
```

2、找到ssh密钥

id_rsa

id_rsa.pub

3、在github中添加公钥 id_rsa.pub

4、创建远程仓库

Create a new repo

5、关联远程仓库
```
git remote add origin git@github.com:estheimqwu/learningbook
```

6、推送本地仓库

`git push filename`

使用`-u`参数可以关联分支。

### 克隆仓库
1、新建一个远程仓库

2、克隆这个仓库
```
git clone git@github.com:estheimqwu/learningbook
```
clone会新建一个本地仓库

### 拉取工程
```
git pull
git pull origin
git pull origin master:brantest # 拉取并与brantest合并
git pull origin master
```

## 分支
### 管理分支
```
HEAD->master->final
      dev   ->
```
1、创建分支

`git checkout -b dev`

->
```
git branch dev
git checkout dev # 切换分支
```

2、查看当前分支情况
```
git branch
```

3、合并分支

合并指定分支到当前分支

`git merge dev`

4、删除分支

`git branch -d dev`

5、switch命令切换分支

创建并切换到新分支

`git switch -c dev`

直接切换到已有的master分支

`git switch master`

6、合并冲突
当合并存在冲突时，需要定位去统一文件。

### 分支管理策略
1、合并策略

合并分支时，使用--no-ff参数。（与Fast forward模式相对）

`git merge --no-ff -m "merge with no-ff" dev`

这样合并会保留分支信息。

2、分支策略
+ master分支应该是非常稳定的，仅用来发布新版本，平时不在上面编写代码。
+ dev承载日常开发的工作。

### bug分支
情境：1、正在一个dev分钟工作；2、有一个亟需解决的bug任务。

通过`git stash`功能可以冻结当前工作现场，等恢复后继续工作。

通过`git stash list`查看stash列表。

通过`git stash apply`可以恢复，同时注意：

`git stash pop` = `git stash` + `git stash drop`

`git stash apply`不会删除stash信息（你可以重复恢复这工作空间）

EXTRA:`git cherry-pick`

### feature分支

+ 开发一个新feature，最好新建一个分支；

+ 如果要丢弃一个没有被合并过的分支，可以通过git branch -D \<name\>强行删除。

### 多人协作
1、查看远程仓库的信息，使用`git remote`，或者`git remote -v`获得更详细的信息。

2、先使用`git push orgin <branch-name>`尝试推送自己的修改。

3、推送失败，使用`git pull`试图合并。

4、合并失败，解决代码冲突，并在本地提交。

5、解决冲突后，重复第二步。

P.S 如果`git pull`提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令`git branch --set-upstream-to <branch-name> origin/<branch-name>`。

### rebase
使用rebase命令可以整理分支与时间线。