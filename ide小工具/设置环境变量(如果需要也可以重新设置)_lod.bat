@ECHO OFF
rem ���ɻ���
set pa=%cd%
md Tk
setx Path "%pa%\Tk";
set txt=%*
set pa=%cd%
echo @ECHO OFF >.\Tk\tk.bat
echo set pa=%pa%\tk.py >>.\Tk\tk.bat
copy /b .\Tk\tk.bat+tk.txt .\Tk\tk.bat

chcp 65001
rem ����ע���
reg\run
rem ����ע��� regedit /s tkr.reg
tkr.reg
