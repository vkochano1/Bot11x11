import Tournament
from Config  import *
import re
import time
import logging


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
    
    def isTechnicalWorks(self):
        soup = GlobalData.CurrentSession.getContent(GlobalData.Site)
        res = soup.find('img', src=re.compile("works.jpg"))
        return res != None
    
    
    def waitUntilReady(self):
            try :            
                ### Wait until technical works are done
                wasTechnical = False
                while self.isTechnicalWorks():
                    time.sleep(GlobalData.TechnicalWorksDoneCheckInterval)
                    wasTechnical = True
                    logging.info('Maintenance works are in progress, waiting')
                
                if wasTechnical == True:
                    return True
                    
                slpSec = self.needSomeRest()
                while  slpSec > GlobalData.WaitUntilNSecondsLeftToFullRecovery:
                    self.logger.info('Left  to sleep ' + str(slpSec))
                                    
                    tournamentID  = Tournament.Tournament().extractTournamentId()
                    if tournamentID != None:
                        break
                                       
                    slpSec = self.needSomeRest()
                    time.sleep(GlobalData.RecoveryStateCheckInterval)
            except Exception as ex:
                print ex
                return False
            
            return True
