
from PlayMatch import *
from Tournament import *
from Analyser import *
from Session import *
import LoggerConfig

gameSession = GameSession()
gameSession.initSession()
 


while True:
		try:
			gameSession = GameSession()
			gameSession.initSession()
			ts = Tournament()
			ts.playTournament()

			slpSec = ts.needSomeRest()
			while slpSec > 500:
				print('Left  to sleep ' + str(slpSec))
				
				t = ts.extractTournamentId()
				if t != None:
					break
				slpSec = ts.needSomeRest()
				time.sleep(30)
		except  Exception as ex:
			print('Exception ' , ex)
			pass			

		time.sleep(10)
