from Config  import *
import re
import time
import logging


class TournamentSelector(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def firstTournament(self):
        htmlDom = GlobalData.CurrentSession.getContent(GlobalData.TournamentsLink)
        tournamnetLink = htmlDom.find('a', href=re.compile("tournaments.php\?id="))
        if tournamnetLink == None:
            return None
        id = tournamnetLink.attrs['href'].split('=')[-1]
        return id

    def populateOpenTournamentsList(self, tournamentsLink):
        htmlDom = GlobalData.CurrentSession.getContent(tournamentsLink)
        #print htmlDom
        allTournamentLinks = htmlDom.find_all('a', href=re.compile("tournaments.php\?id="))
        tornaments = []

        for tournamnetLink in allTournamentLinks:
                tbl =  tournamnetLink.parent.parent.parent
                itms = tbl.find_all('li')
                itms = [''.join(itm.find_all(text=True, recursive=False)).strip() for itm in itms ]
                botLevel = None
                if len(itms)==6:
                    botLevel = int(itms[4]) 
                else:
                    continue
                #for e in itms:
                #    print(e)
                id = tournamnetLink.attrs['href'].split('=')[-1]
                tornaments.append( (id, botLevel) )
        return tornaments
        
    def selectTournament(self):
        tournaments = self.populateOpenTournamentsList(GlobalData.TournamentsLink)
        if GlobalData.UserCfg.SkipNonBotTournaments == True:
            tournaments = [tInfo for tInfo in tournaments if tInfo[1] != None]
        if len(tournaments) == 0:
            return None
        
        return tournaments[0][0]




