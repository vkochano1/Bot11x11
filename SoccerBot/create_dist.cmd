set ROOT=C:/test/Bot11x11/Bot/SoccerBot
set PYTHONPATH=%ROOT%/Core;%ROOT%/Config;%ROOT%/Utils;%ROOT%/CostFunctions;%ROOT%/Tactics;
echo %PYTHONPATH%

setup.py py2exe 
