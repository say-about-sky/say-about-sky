rem chcp 65001 

copy /b reg\tkf.reg tkr.reg

call reg\rm

copy tkr.reg+reg\tkff.txt tkr.reg

set opo=%cd%\tk.exe open ^%%1
echo %opo%^" >>tkr.reg