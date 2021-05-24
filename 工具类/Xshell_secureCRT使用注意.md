1、关于rz命令与sz命令乱码的问题。

rz，sz是便是Linux/Unix同Windows进行ZModem文件传输的命令行工具。windows端需要支持ZModem的telnet/ssh客户端（比如SecureCRT）运行命令rz，即是接收文件，SecureCRT就会弹出文件选择对话框，选好文件之后关闭对话框，文件就会上传到当前目录
注意：单独用rz会有两个问题：上传中断、上传文件变化（md5不同），解决办法是上传是用**rz -be**，并且去掉弹出的对话框中“Upload files as ASCII”前的勾选

```markdown
-a, –ascii
-b, –binary 用binary的方式上传下载，不解释字符为ascii
-e, –escape 强制escape 所有控制字符，比如Ctrl+x，DEL等
rar,gif等文件文件采用 -b 用binary的方式上传。
文件比较大而上传出错的话，采用参数 -e
如果用不带参数的rz命令上传大文件时，常常上传一半就断掉了，很可能是rz以为上传的流中包含某些特殊控制字符，造成rz提前退出。
```