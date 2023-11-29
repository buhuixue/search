# 脚本功能
在命令行下执行脚本，查看IP地址归属地信息  
 <span style="color:#333333">`search <IP>` </span> 
## 一、在代码中添加token
## 二、使用pyinstaller将脚本打包成exe文件
1.在search.py 所在目录，按住shift+鼠标右键，选择 此处打开命令行 程序  
2.输入: pyinstaller -F --uac-admin search.py  
3.复制: build 文件夹的 search 文件夹里面的 search.exe.manifest 到与 search.py 同级目录  
4.在 search.py 所在目录，按住shift+鼠标右键，选择 此处打开命令行 程序  
5.输入: pyinstaller -F --uac-admin -r search.exe.manifest,1 search.py  
6.在 dist 文件夹生成的 search.exe 就是拥有管理员模式的可执行文件 图标上有盾牌)  
## 三、设置系统环境变量，实现在全局环境下执行脚本
我的电脑-->属性-->高级系统设置-->环境变量-->Path中为脚本添加路径
## 注意事项
如果电脑开启代理，执行脚本会出错
