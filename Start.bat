@echo off

echo Running...

:: check if Python is installed
python --version
IF ERRORLEVEL 1 (
    echo Python is not installed.
    echo Installing Python...

    :: download Python installer
    powershell -Command "& { Invoke-WebRequest https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -OutFile .\pythonInstaller.exe }"

    :: install Python
    .\pythonInstaller.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    :: remove Python installer
    del .\pythonInstaller.exe
) else (
    echo Python checked!
)

echo Almost done! Installing Environment in 5 sec
timeout /t 5 /nobreak

:: install Requests library
pip3 install requests
IF ERRORLEVEL 1 (
    echo Failed to install Requests library.
    echo Don't worry! Just close and re-run the Start.bat
) else (
    echo Successfully installed Requests library.
)

:: run python
echo Ready!!
echo Running...
echo ---------------

python ".\py\Menu.py"

@echo Render Completed!
@echo Press any key to exit!
@echo See you next time!
pause