import os
import sys

subirs = ['CostFunctions', 'Tactics', 'Config', 'Core', 'Utils']

for d in subirs:
    sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0]))), d ))

from Config import *
GlobalData.AppDir = os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0])))

from PlayMatch import *
from Tournament import *
from Analyser import *
from Session import *
import LoggerConfig
import Training
import TournamentReadiness
import TournamentSelector
import argparse
 

parser = argparse.ArgumentParser(description='11x11 Bot')
parser.add_argument('start')
parser.add_argument('--user', help='11x11.ru user')

args = parser.parse_args()

GlobalData.UserCfg = UserConfig(args.user)
loggerConfig = LoggerConfig.LoggerConfig(args.user)

gameSession = GameSession()
gameSession.initSession()

tournamentReadiness = TournamentReadiness.TournamentReadiness()
newTournament = Tournament()

try:
    if GlobalData.UserCfg.TrainingTactic:
        Training.Training().trainAll(GlobalData.UserCfg.TrainingTactic)
except Exception as ex:
        print(ex)
        
while True:
		try:
			gameSession = GameSession()
			gameSession.initSession()

			while False == tournamentReadiness.waitUntilReady():
				gameSession.initSession()

			 
			newTournament.playTournament()

		except  Exception as ex:
			print('Exception ' , ex)
			pass

		try:
                    if GlobalData.UserCfg.TrainingTactic:
                        Training.Training().trainAll(GlobalData.UserCfg.TrainingTactic)
                except Exception as ex:
                    print(ex)
		
