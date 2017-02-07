import Tournament
from Config  import *
import re
import time
from bs4 import BeautifulSoup
import logging


class TournamentReadiness(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def needSomeRest(self):
        r = GlobalData.CurrentSession.get(GlobalData.Players)
        soup = BeautifulSoup(r.content, 'html.parser')
        g = soup.find('tr', attrs = {'class' : 'header'})
        colls = g.find_all('center')
        self.logger.info('Current physio is ' + str(float(colls[5].text) / float(colls[3].text)))
        perc = 100 * float(colls[5].text) / float(colls[3].text)
        self.logger.info('Estimated time to wait %s (sec)' + str(perc))
        return (100 - perc) * 60;
    
    def isTechnicalWorks(self):
        r = GlobalData.CurrentSession.get(GlobalData.Site)
        soup = BeautifulSoup(r.content, 'html.parser')    
        res2 = soup.find('img', src=re.compile("works.jpg"))
        return res2 != None
    
    
    def waitUntilReady(self):
            try :            
                ### Wait until techicals works are done
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
                    if t != None:
                        break
                                       
                    slpSec = ts.needSomeRest()
                    time.sleep(GlobalData.RecoveryStateCheckInterval)
            except Exception as ex:
                print ex
                return False
            
            return True