
from PlayMatch import *
from Tournament import *
from Analyser import *
from Session import *
import LoggerConfig
import TournamentReadiness
import argparse
 
import argparse

parser = argparse.ArgumentParser(description='11x11 Bot')
parser.add_argument('test')
parser.add_argument('--user', help='11x11.ru user')
parser.add_argument('--password', help='11x11.ru password')
parser.add_argument('--best-squad-stage', help='')

args = parser.parse_args()


GlobalData.LoginUser = args.user
GlobalData.LoginPassword = args.password
GlobalData.BestSquadStage= int(args.best_squad_stage)

loggerConfig = LoggerConfig.LoggerConfig(args.user)

print args.user, args.password, GlobalData.BestSquadStage
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
		
					
	
		
