:: Python 2 and 3 installer sites


set PY27_SITE=http://www.python.org/ftp/python/2.7.5
set PY27_FILE=python-2.7.5.msi

set PY33_SITE=http://www.python.org/ftp/python/3.3.2
set PY33_FILE=python-3.3.2.msi

set BOOTSTRAP_URL=http://DW-89:8080/packages/bootstrap/bootstrap.py
set BOOTSTRAP_FILE=bootstrap.py


:: Build full URLs and download paths

set PY27_URL=%PY27_SITE%/%PY27_FILE%

set PY33_URL=%PY33_SITE%/%PY33_FILE%


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


:: Download installers

cd %TEMP%

if exist %PY27_FILE% (
    @echo Already download: %PY27_PATH%
) else (
    bitsadmin /transfer Python27 /download /priority normal %PY27_URL% %TEMP%\%PY27_FILE%
)

if exist %PY33_FILE% (
    @echo Already download: %PY33_PATH%
) else (
    bitsadmin /transfer Python33 /download /priority normal %PY33_URL% %TEMP%\%PY33_FILE%
)

if %errorlevel% neq 0 goto :error


:: Run installers in quiet mode

msiexec /i %PY27_FILE%
msiexec /i %PY33_FILE%

if %errorlevel% neq 0 goto :error


:: Download bootstrap

bitsadmin /transfer ArniePye /download /priority normal %BOOTSTRAP_URL% %TEMP%\%BOOTSTRAP_FILE%

if %errorlevel% neq 0 goto :error


:: Bootstrap ArniePye

C:\Python33\python %BOOTSTRAP_FILE% --clear
C:\Python27\python %BOOTSTRAP_FILE%


if %errorlevel% neq 0 goto :error


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


:error
PAUSE
exit /b %errorlevel%
:end