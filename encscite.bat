@echo off
setlocal
::echo 0 %0%

set _SCRIPT_DRIVE=%~d0
set _SCRIPT_PATH=%~p0
set folder=%_SCRIPT_DRIVE%%_SCRIPT_PATH%
:: echo %_SCRIPT_DRIVE%
::echo %_SCRIPT_PATH%
::old_cd=%CD%
REM echo folder %folder%

:: Override scite home dir, avoids mix/matching with a real SciTE config that may exist on a machine
:: SciTE checks for config files in the following locations in order:
::   SciTE_HOME
::   SciTE_USERHOME
::   USERPROFILE	- Essentially Windows user's home directory

::set SciTE_HOME=C:\programs\prog
::set SciTE_HOME=C:\Users\clach04\OneDrive - Actian Software\programs\encscite\prog
set SciTE_HOME=%folder%
set SciTE_USERHOME=%SciTE_HOME%
path %SciTE_HOME%;%PATH%
path %SciTE_HOME%\prog;%PATH%
::set PTCIPHER_EXE="%SciTE_HOME%\ptcipher.exe"
::set PTCIPHER_EXE="%SciTE_HOME%\dist\ptcipher.exe"

::start 
REM does NOT work
REM start "%SciTE_HOME%\sc1.exe" %*%

echo start "%SciTE_HOME%\sc1.exe" %*%
REM fork bomb!
REM start EncScite "%SciTE_HOME%\sc1.exe" %*%
REM Best; spawns and does not wait, can handle multiple files as parameters (and/or regular scite parameters)
start "MyTitle" "%SciTE_HOME%\sc1.exe" %*%

REM Works, waits
REM "%SciTE_HOME%\sc1.exe" %*%

REM works, also waits
REM CMD /C "%SciTE_HOME%\sc1.exe" %*%

REM works, does not wait BUT opens a blank CMD window
REM start CMD /C "%SciTE_HOME%\sc1.exe" %*%

endlocal
