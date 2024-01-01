REM assuming in EncScite dir
copy /y puren_tonbo\integrations\scite\pt_scite.lua SciTEStartup.lua

del EncScite_release.zip
7z a EncScite_release.zip SciTEStartup.lua SciTE.properties encscite.bat sc1.exe
cd puren_tonbo\dist
7z a ..\..\EncScite_release.zip lib prog
cd ..\..
