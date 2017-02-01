# -*- coding: utf-8 -*-
import Utils
from Config import GlobalData
from bs4 import BeautifulSoup
import re
import logging

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
        response = GlobalData.CurrentSession.get(req)
        parser = Utils.MyHTMLParser()
        parser.feed(response.content)
        self.logger = logging.getLogger(self.__class__.__name__)
        dom = BeautifulSoup(response.content,'html.parser')

        #score
        self.score = None
        nodes = dom.find_all("font", attrs = {"size" : "2"} )
        for node in nodes:
            scoreElement = node.find('h2')
            if scoreElement:        
                self.score  = [ int(s) for s in scoreElement.text.split(':')]
        
        #user IDS
        nodes = dom.find_all("a", href = re.compile('users') )
        self.uids = []
        for nd in nodes[-2:]:
            id = nd.attrs['href'].split('/')[2]
            self.uids.append(id)

        #extract table elements
        soup = BeautifulSoup(parser.out, 'html.parser')
        schemaNode = soup.find("td", text = re.compile(u'схема'))
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
        
        
        
class UserGameArchive(object): 
    def __init__(self, userID, N):
        self.userID  = userID
        self.N = N
        self.archiveGames = []
        self.logger = logging.getLogger(self.__class__.__name__)
            
    def fetchGames(self):       
        req  = GlobalData.ArchiveGameForUserPrefix +  self.userID
        response = GlobalData.CurrentSession.get(req)
        parser = Utils.MyHTMLParser()
        parser.feed(response.content)
        soup = BeautifulSoup(parser.out, 'html.parser')
        
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
                print (ex)
                pass
            
        return self.archiveGames
    
    def games(self):
        return self.archiveGames
    
import time   
class MatchReportTracker(object):
    def __init__(self, gameID):
        self.gameID = gameID
        
    
    def waitUntilReportIsReady(self):
        
        for i in range(60):
            try:
                game = Game(self.gameID)
                print ('Played')
                print(str(game))
                break
            except:
                pass
            time.sleep(5)
            print('not ready yet')