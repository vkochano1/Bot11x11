rmdir /S /Q build
set ROOT=%cd%
set PYTHONPATH=%ROOT%/Core;%ROOT%/Config;%ROOT%/Utils;%ROOT%/CostFunctions;%ROOT%/Tactics;
echo %PYTHONPATH%

setup.py py2exe 
