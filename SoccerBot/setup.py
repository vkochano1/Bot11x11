from distutils.core import setup
import py2exe
import os
import sys

filesToCopy = []
def addDataDirectory(dataDir, filesToCopy):
    filesToCopy.append((dataDir, []))
    for f in os.listdir(dataDir):
        if os.path.splitext(f)[-1] =='.py':
            filesToCopy.append( (dataDir, [os.path.join(dataDir,  f )]))

DIST_DIR='C:/dist4'
addDataDirectory('Tactics/Main', filesToCopy)
addDataDirectory('Tactics/PassingStyle', filesToCopy)
addDataDirectory('CostFunctions/Squad', filesToCopy)
addDataDirectory('CostFunctions/Roles', filesToCopy)
addDataDirectory('CostFunctions/Tournament', filesToCopy)
addDataDirectory('CostFunctions/Recovery', filesToCopy)
addDataDirectory('UserData', filesToCopy)
filesToCopy.append('starterX.cmd')

options = {'py2exe': {  
           'dist_dir': os.path.join(DIST_DIR, 'SoccerBot1'),
           }}

setup(console=['RunTest.py'], name='Bot11x11', data_files=filesToCopy, options=options)
