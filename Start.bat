@echo off

:: check if Python is installed
python --version
IF ERRORLEVEL 1 (
    echo Python is not installed. Installing Python...

    :: download Python installer
    powershell -Command "& { Invoke-WebRequest https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -OutFile .\pythonInstaller.exe }"

    :: install Python
    .\pythonInstaller.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    :: remove Python installer
    del .\pythonInstaller.exe
) else (
    echo Python is already installed.
)

:: install Requests library
pip3 install requests
IF ERRORLEVEL 1 (
    echo Failed to install Requests library.
) else (
    echo Successfully installed Requests library.
)

:: run python
echo running Menu.py...
python ".\py\Menu.py"

@echo Installation completed. Press any key to exit...
pause