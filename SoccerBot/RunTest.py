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
import TournamentReadiness
import TournamentSelector
import argparse
 

parser = argparse.ArgumentParser(description='11x11 Bot')
parser.add_argument('test')
parser.add_argument('--user', help='11x11.ru user')
parser.add_argument('--password', help='11x11.ru password')


args = parser.parse_args()


GlobalData.LoginUser = args.user
GlobalData.LoginPassword = args.password
GlobalData.UserCfg = UserConfig.loadConfig(GlobalData.LoginUser)


loggerConfig = LoggerConfig.LoggerConfig(args.user)

gameSession = GameSession()
gameSession.initSession()

print args.user, args.password
tournamentReadiness = TournamentReadiness.TournamentReadiness()


while True:
		try:
			gameSession = GameSession()
			gameSession.initSession()

			while False == tournamentReadiness.waitUntilReady():
				gameSession = GameSession()
				gameSession.initSession()

			newTournament = Tournament()
			newTournament.playTournament()

		except  Exception as ex:
			print('Exception ' , ex)
			pass
		
					
	
		
