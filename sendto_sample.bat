@echo off

SET pdir=%~DP0

python "%pdir%\sendto_sample.py" %* && ^
pause && exit
