@ECHO OFF
rem 生成环境
set pa=%cd%
md Tk
setx Path "%pa%\Tk";
set txt=%*
set pa=%cd%
echo @ECHO OFF >.\Tk\tk.bat
echo set pa=%pa%\tk.py >>.\Tk\tk.bat
copy /b .\Tk\tk.bat+tk.txt .\Tk\tk.bat

chcp 65001
rem 生成注册表
reg\run
rem 导入注册表 regedit /s tkr.reg
tkr.reg
