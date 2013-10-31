::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: Bootstaps a Python 2 and 3 installation from nothing.
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


@echo off
set version=33
set /p version="Desired default Python version 27 or [33]? "
@echo on


:: Python 2 and 3 installer sites

set PY27_SITE=http://www.python.org/ftp/python/2.7.5
set PY27_FILE=python-2.7.5.msi
set PYWIN27_SITE=http://downloads.sourceforge.net/project/pywin32/pywin32/Build%%20218
set PYWIN27_FILE=pywin32-218.win32-py2.7.exe

set PY33_SITE=http://www.python.org/ftp/python/3.3.2
set PY33_FILE=python-3.3.2.msi
set PYWIN33_SITE=http://downloads.sourceforge.net/project/pywin32/pywin32/Build%%20218
set PYWIN33_FILE=pywin32-218.win32-py3.3.exe

set BOOTSTRAP_URL=http://{ADDRESS}/packages/bootstrap/bootstrap.py
set BOOTSTRAP_FILE=bootstrap.py

:: Build full URLs and download paths

set PY27_URL=%PY27_SITE%/%PY27_FILE%
set PYWIN27_URL=%PYWIN27_SITE%/%PYWIN27_FILE%

set PY33_URL=%PY33_SITE%/%PY33_FILE%
set PYWIN33_URL=%PYWIN33_SITE%/%PYWIN33_FILE%


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


:: Download installers

cd %TEMP%

if exist %PY27_FILE% (
    @echo Already download: %PY27_FILE%
) else (
    bitsadmin /transfer Python27 /download /priority normal %PY27_URL% %TEMP%\%PY27_FILE%
)

if exist %PYWIN27_FILE% (
    @echo Already download: %PYWIN27_FILE%
) else (
    bitsadmin /transfer Python27-PyWin32 /download /priority normal %PYWIN27_URL% %TEMP%\%PYWIN27_FILE%
)

if exist %PY33_FILE% (
    @echo Already download: %PY33_FILE%
) else (
    bitsadmin /transfer Python33 /download /priority normal %PY33_URL% %TEMP%\%PY33_FILE%
)

if exist %PYWIN33_FILE% (
    @echo Already download: %PYWIN33_FILE%
) else (
    bitsadmin /transfer Python33-PyWin32 /download /priority normal %PYWIN33_URL% %TEMP%\%PYWIN33_FILE%
)


:: Run the installers

msiexec /i %PY27_FILE%
start %PYWIN27_FILE%
pause

msiexec /i %PY33_FILE%
start %PYWIN33_FILE%
pause


:: Download bootstrap

bitsadmin /transfer ArniePye /download /priority normal %BOOTSTRAP_URL% %TEMP%\%BOOTSTRAP_FILE%


:: Bootstrap ArniePye

if %version% == 27 (
    C:\Python27\python %BOOTSTRAP_FILE% --clear
    C:\Python33\python %BOOTSTRAP_FILE%
) else (
    C:\Python33\python %BOOTSTRAP_FILE% --clear
    C:\Python27\python %BOOTSTRAP_FILE%
)


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


if %errorlevel% eq 0 goto :end
:error
@echo An error occured during installation.
pause
exit /b %errorlevel%
:end
@echo Logout to reflect the PATH changes.
pause
