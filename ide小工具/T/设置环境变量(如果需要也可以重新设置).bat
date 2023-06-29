@ECHO OFF
set pa=%cd%
md TKM
setx Path "%pa%\TKM";
set txt=%*
echo @ECHO OFF >.\TKM\tk.bat
echo set pa=%pa%\tk >>.\TKM\tk.bat
copy /b .\TKM\tk.bat+tk.txt .\TKM\tk.bat

chcp 65001
rem 生成注册表
call reg\run
rem 导入注册表 regedit /s tkr.reg
call tkr.reg
