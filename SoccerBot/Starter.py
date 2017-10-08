import os
import sys
import subprocess

subirs = ['CostFunctions', 'Tactics', 'Config', 'Core', 'Utils']

for d in subirs:    
    sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0]))), d ))

AppDir = os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0])))
UserDataDir = os.path.join(AppDir, 'UserData')

for fname in os.listdir(UserDataDir):
            configName, ext = os.path.splitext(fname)
            if ext != '.py':
                continue
            print 'Executing ' , configName
            p = subprocess.Popen(["python", "RunBot.py", "--user", configName, 'start'])
            print 'Started ' , p.pid

		
					
	
		
