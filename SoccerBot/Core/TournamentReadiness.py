import Tournament
import TournamentSelector
from Config  import *
import re
import time
import logging
import PlayerInfo


class TournamentReadiness(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def needSomeRest(self):
        soup = GlobalData.CurrentSession.getContent(GlobalData.Players)
        g = soup.find('tr', attrs = {'class' : 'header'})
        colls = g.find_all('center')
        self.logger.info('Current physio is ' + str(float(colls[5].text) / float(colls[3].text)))
        perc = 100 * float(colls[5].text) / float(colls[3].text)
        self.logger.info('Estimated time to wait %s (sec)' % str(perc))
        return (100 - perc) * 60;

    def verifyLimits(self):
        info = PlayerInfo.PlayerDataTable();
	players = []
	playersByRefId = {}

	for playerID, playerInfo in info.playerInfoByRefId.iteritems():
		player = PlayerInfo.Player (playerID, info)
		players.append(player)
		playersByRefId[playerID] = player

        GkReadiness = [0,0]
        DReadiness = [0,0]
        MReadiness = [0,0]
        FReadiness = [0,0]
        
        for player in players:
            if player.AllowedToPlay == False:
                continue
				
            if player.Positions[0][-1] == 'k':
                GkReadiness[0] = GkReadiness[0] + player.Readiness
                GkReadiness[1] = GkReadiness[1] + 1
            elif player.Positions[0][-1] == 'd':
                DReadiness[0] = DReadiness[0] + player.Readiness
                DReadiness[1] = DReadiness[1] + 1
            elif player.Positions[0][-1] == 'm':
                MReadiness[0] = MReadiness[0] + player.Readiness
                MReadiness[1] = MReadiness[1] + 1
            elif player.Positions[0][-1] == 'f':
                FReadiness[0] = FReadiness[0] + player.Readiness
                FReadiness[1] = FReadiness[1] + 1

        if GkReadiness[0] / GkReadiness[1] < 90:
            return False
        
        if DReadiness[0] / DReadiness[1] < 82 or DReadiness[1] < 4:
            return False

        if MReadiness[0] / MReadiness[1] < 82 or MReadiness[1] < 5:
            return False
        
        if FReadiness[0] / FReadiness[1] < 82 or FReadiness[1] < 3:
            return False

        return True
            
                    
    def isTechnicalWorks(self):
        soup = GlobalData.CurrentSession.getContent(GlobalData.Site)
        res = soup.find('img', src=re.compile("works.jpg"))
        return res != None

    def isTechnicalWorksIn(self,ts,t):
        try:
            GlobalData.CurrentSession.initSessionFast()
            extr = ts.firstTournament()
            if extr:
                t.joinTournament(extr)
                return False
            else:
                time.sleep(0.001)
        except:
            time.sleep(0.001)
        return True
    
    def waitUntilReady(self):
        try :            
            ### Wait until technical works are done
            wasTechnical = False
            ts = TournamentSelector.TournamentSelector()
            t = Tournament.Tournament()
            if self.isTechnicalWorks():
                logging.info('Maintenance works are in progress, waiting')
                while self.isTechnicalWorksIn(ts,t):
                    pass
                    
                wasTechnical = True
                
                       
            if wasTechnical == True:
		GlobalData.CurrentSession.initSessionFast()
                extr = ts.firstTournament()
                t.joinTournament(extr)
                
            
            slpSec = self.needSomeRest()
            while  self.verifyLimits() != True and slpSec > GlobalData.UserCfg.WaitUntilNSecondsLeftToFullRecovery:
                self.logger.info('Left  to sleep ' + str(slpSec))                                    
                tournamentID  = Tournament.Tournament().extractTournamentId()
                if tournamentID != None:
                    break                                     
                slpSec = self.needSomeRest()
                time.sleep(GlobalData.UserCfg.RecoveryStateCheckInterval)
        except Exception as ex:
            print ex
            return False
        
        return True
