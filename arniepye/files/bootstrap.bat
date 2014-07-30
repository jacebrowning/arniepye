::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::
:: Bootstraps a Python 2 and 3 installation + package management on Windows.
::
:: To run outside of the local network, manually download bootstrap.py to the
:: same directory as this file before running this file.
::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


@echo off
set version=34
set /p version="Desired default Python version 27 or [34]? "
@echo on


:: Python 2 and 3 installer sites

set PY27_SITE=http://legacy.python.org/ftp/python/2.7.8
set PY27_FILE=python-2.7.8.msi
set PYWIN27_SITE=http://downloads.sourceforge.net/project/pywin32/pywin32/Build%%20218
set PYWIN27_FILE=pywin32-218.win32-py2.7.exe

set PY34_SITE=http://legacy.python.org/ftp/python/3.4.0/
set PY34_FILE=python-3.4.0.msi
set PYWIN34_SITE=http://downloads.sourceforge.net/project/pywin32/pywin32/Build%%20218
set PYWIN34_FILE=pywin32-218.win32-py3.4.exe

set BOOTSTRAP_URL=http://{ADDRESS}/packages/bootstrap/bootstrap.py
set BOOTSTRAP_FILE=%CD%/bootstrap.py

:: Build full URLs and download paths

set PY27_URL=%PY27_SITE%/%PY27_FILE%
set PYWIN27_URL=%PYWIN27_SITE%/%PYWIN27_FILE%

set PY34_URL=%PY34_SITE%/%PY34_FILE%
set PYWIN34_URL=%PYWIN34_SITE%/%PYWIN34_FILE%


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


:: Download installers

pushd %TEMP%

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

if exist %PY34_FILE% (
    @echo Already download: %PY34_FILE%
) else (
    bitsadmin /transfer Python34 /download /priority normal %PY34_URL% %TEMP%\%PY34_FILE%
)

if exist %PYWIN34_FILE% (
    @echo Already download: %PYWIN34_FILE%
) else (
    bitsadmin /transfer Python34-PyWin32 /download /priority normal %PYWIN34_URL% %TEMP%\%PYWIN34_FILE%
)

:: Download bootstrap.py

popd

if exist %BOOTSTRAP_FILE% (
    @echo Already download: %BOOTSTRAP_FILE%
) else (
    bitsadmin /transfer ArniePye /download /priority normal %BOOTSTRAP_URL% %BOOTSTRAP_FILE%
)

:: Install Python and Windows Extensions

pushd %TEMP%

msiexec /i %PY27_FILE%
start %PYWIN27_FILE%
pause

msiexec /i %PY34_FILE%
start %PYWIN34_FILE%
pause

:: Bootstrap ArniePye

popd

if %version% == 27 (
    C:\Python27\python %BOOTSTRAP_FILE% --clear
    C:\Python34\python %BOOTSTRAP_FILE%
) else (
    C:\Python34\python %BOOTSTRAP_FILE% --clear
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
