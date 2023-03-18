# HNUST自动登录脚本

#### 介绍
湖南科技大学校园网开机自动登录

#### 软件架构
使用python作为脚本，bat启动。


#### 安装教程

1.  安装python3（仅支持python3）
2.  下载代码 `git clone https://gitee.com/hpleapfrog_0/hnustzidongdeng.git`

3.  按说明修改代码内容

#### 使用说明

1. 将web.py中的UserName、PassWord、Operators填写完整。例如下

```
UserName = "123456" # 账号

PassWord = "123456"  # 密码

Operators = "@cmcc" # 运营商选择：电信“@telecom”，移动“@cmcc”，联通“@unicom”，校园网为空值
```

2. 将修改后的web.py文件放在你想保存的文件夹下

3. 在web.bat中第四行改为 cd “你存放web.py的绝对地址”，例如 “cd C:\app\setup”

4. 按win+R打开启动，输入'shell:Common Startup'或'shell:Startup'打开启动文件夹，将修改后的web.bat放入启动文件夹。
