if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
cd C:\Users\wbycn %将此处改为你存放web.py文件位置%
python web.py