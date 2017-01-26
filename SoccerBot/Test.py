# -*- coding: utf-8 -*-
import TeamPlayers
from PlayMatch import *
from Tournament import *
from Analyser import *
from  Config import *
from  TournamentPosition import *
 
gameSession = GameSession()
gameSession.initSession()


req  = GlobalData.Site + '/xml/games/tournaments.php'
r = GlobalData.CurrentSession.get(req)
				
soup = BeautifulSoup(r.content, 'html.parser')
schemaNode = soup.find("script", text = re.compile('document.location.href='))
tournamentID =  schemaNode.text.split('/')[-1].strip(';').strip("'")
print(tournamentID)
ts = TournamentPosition(tournamentID)
print ts.canPass()
