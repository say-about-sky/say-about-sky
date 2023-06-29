@ECHO OFF
rem 生成环境
set pa=%cd%
md Tk
setx Path "%pa%\Tk";
set txt=%*
set pa=%cd%
echo @ECHO OFF >.\Tk\tk.bat
echo set pa=%pa%\tk >>.\Tk\tk.bat
copy /b .\Tk\tk.bat+tk.txt .\Tk\tk.bat

rem 注册表
tk_reg