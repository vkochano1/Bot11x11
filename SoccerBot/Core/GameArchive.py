# -*- coding: utf-8 -*-
from Config import GlobalData
import re
import logging
import time 
import PlayerInfo

class Game(object):

    @staticmethod
    def extractTactic(tacticStr):
        percB = tacticStr.find('(')
        percE = tacticStr.find('%')    
        extr = tacticStr[percB + 1 : percE]
        if extr == '':
            return None
        return int(extr)
    
    @staticmethod
    def extractSchema(schemaStr):
        return str(schemaStr.replace('-',''))
    
    @staticmethod
    def extractStrength(strengthStr):
        if strengthStr == '':
            return None
        return float(strengthStr)
    
    @staticmethod
    def extractStrategy(strategyStr):

        strategyMapping = { 
            u"нормальная": "Normal", 
            u"игра в пас": "Passing",
            u"техничная игра" : "Dribbling", 
            u"дальние удары": "LongShots"     
        } 
        return strategyMapping.get(strategyStr)

    @staticmethod
    def extractPassingStyle(passingStyleStr):
        passingMapping = { u"дальние": "Long",u"смешанные": "Mixed", u"короткие" : "Short" } 
        return passingMapping.get(passingStyleStr)
    
    @staticmethod
    def extractPressing(pressingStr):
        pressingMapping = { u"нет": False, u"да": True}
        pressEnabled = pressingMapping.get(pressingStr)
        return pressEnabled == True            

    def getStatsFor(self,userID):
        idx =  0 if self.uids[0] == userID else 1
        return [ self.strength[idx], 
            self.schema[idx], 
            self.tactic[idx], 
            self.pressing[idx], 
            self.strategy[idx],
            self.passingStyle[idx]  
            ]
    def __str__(self):
        text = """
%s\t\t  UserID        %s
%s\t\t  Score         %s
%s\t\t  Schema        %s
%s\t\t  Tactic        %s
%s\t\t  Pressing      %s
%s\t\t  Strategy      %s
%s\t\t  Passing style %s
%s\t\t  Strength      %s
""" % (  self.uids[0], self.uids[1]
        ,self.score[0], self.score[1] 
        ,self.schema[0], self.schema[1]
        ,self.tactic[0], self.tactic[1]
        ,self.pressing[0], self.pressing[1]
        ,self.strategy[0], self.strategy[1]
        ,self.passingStyle[0], self.passingStyle[1]
        ,self.strength[0], self.strength[1]
        
        )
        return text
        
    def __init__(self, gameID):
        req = GlobalData.Reports + '/' + gameID

        self.logger = logging.getLogger(self.__class__.__name__)
        dom = GlobalData.CurrentSession.getContent(req)
        self.dom = dom
        #score
        self.score = None
        nodes = dom.find_all("font", attrs = {"size" : "2"} )
        for node in nodes:
	    if len(node.text) == 0:
		continue
            scoreElement = node
            if scoreElement:        
                self.score  = [ int(s) for s in scoreElement.text.split(':')]
        
        #user IDS
        nodes = dom.find_all("a", href = re.compile('users') )
        self.uids = []
        for nd in nodes[-2:]:
            id = nd.attrs['href'].split('/')[2]
            self.uids.append(id)

        #extract table elements
        soup = dom
        schemaNode = dom.find("td", text = re.compile(u'схема'))
        matchReportTable = schemaNode.find_parent('table')
        if matchReportTable == None:
            raise Exception('No data for report', gameID)
        rows = matchReportTable.findAll('tr')
        table = []        
        for row in rows:
            cols = row.findAll('td')
            table.append([cols[0].text, cols[2].text])
    
        self.strength =  [Game.extractStrength(v) for v in table[2] ]  
        self.schema =  [Game.extractSchema(v) for v in table[3] ] 
        self.tactic =  [Game.extractTactic(v) for v in table[4] ]
        self.pressing =  [Game.extractPressing(v) for v in table[5] ]
        self.strategy =  [Game.extractStrategy(v) for v in table[6] ]
        self.passingStyle =  [Game.extractPassingStyle(v) for v in table[7] ]
        self.gameID = gameID    
            
        
    
class GameExtended(Game):
    
    def __init__(self, gameID):
        super(GameExtended, self).__init__(gameID)
        if self.uids[0] == '2' or self.uids[1] == '2':
            raise Exception('Skipping bot')
        
        if self.score[0] != self.score[1] == '2':
            raise Exception('Skipping draw')
        
        self.populateExtendedData(self.dom)
        
    def populateExtendedData(self, htmlDom):
        
        teamSquads = htmlDom.find_all("div", text = 'Gk')
        
        user1Info = PlayerInfo.PlayerDataTable(self.uids[0])
        user2Info = PlayerInfo.PlayerDataTable(self.uids[1])
        
        team1ExtendedData = self.extractExendedSquadData(teamSquads[0].parent.parent.parent, user1Info)
        team2ExtendedData = self.extractExendedSquadData(teamSquads[1].parent.parent.parent, user2Info)
        
        if len(team1ExtendedData) != 11 or len(team1ExtendedData) != 11:
            raise Exception('Skipping inj/reds')
        
        self.extendedData = [team1ExtendedData, team2ExtendedData]
        
    def extractExendedSquadData(self, table, userInfo):        
        playersParticipated = []
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            pos = cols[0].text
            id = cols[1].find('a').attrs['href'].split('/')[-1]
            score = cols[2].text
            playersParticipated.append( ( pos, PlayerInfo.Player(id, userInfo) ))
            
        return playersParticipated
    
    def __str__(self):
        text = super(GameExtended,self).__str__()
        extendedTeam1 = str ([ (pos, player.ID) for pos, player in self.extendedData[0] ] )
        extendedTeam2 = str ([ (pos, player.ID) for pos, player in self.extendedData[1] ] )
        
        return text + extendedTeam1 + extendedTeam2
        
    
class UserGameArchive(object): 
    def __init__(self, userID, N):
        self.userID  = userID
        self.N = N
        self.archiveGames = []
        self.logger = logging.getLogger(self.__class__.__name__)
            
    def fetchGames(self):       
        req  = GlobalData.ArchiveGameForUserPrefix +  self.userID
        soup = GlobalData.CurrentSession.getContent(req)
        
        reportNodes = soup.find_all("a", href = re.compile('/reports/'))
        
        reportIDs = []
        for reportNode in reportNodes:
            reportIDs.append(reportNode.attrs['href'].split('/')[2])
        
        self.archiveGames = []
        for i in range(min(len(reportIDs),self.N) ):
        
            try:
                game = Game(reportIDs[i])
                [strength, schema, tactic, pressing, strategy, passingStyle ] = game.getStatsFor(self.userID)
                if schema != None and strategy != None and tactic != None:
                    self.logger.info('Extracted game \n%s' % str(game))            
                    self.archiveGames.append(game)
            except Exception as ex:
                print ('Failed to extract data for repportID=%s' % str(reportIDs[i]))
                pass
            
        return self.archiveGames
    
    def games(self):
        return self.archiveGames
    
  
class MatchReportTracker(object):
    def __init__(self, gameID):
        self.gameID = gameID
        self.logger = logging.getLogger(self.__class__.__name__)
           
    def waitUntilReportIsReady(self):
        
        for i in range(30):
            try:
                game = Game(self.gameID)
                self.logger.info(str(game))
                break
            except:
                pass
            time.sleep(5)
            self.logger.info('not ready yet')
