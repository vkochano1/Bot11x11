import sys
import os

subirs = ['CostFunctions', 'Tactics', 'Config', 'Core', 'Utils']

for d in subirs:
    sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), d ))

from Config import *
GlobalData.AppDir = os.path.abspath(os.path.dirname(__file__))

import GameArchive
from Config import *
import Session
import logging
import re
import pickle
import CostEvaluators
import CostFunctionCache


class GlobalGameArchive(object): 
    def __init__(self):
        self.archiveGames = []
        self.logger = logging.getLogger(self.__class__.__name__)
            
    def fetchGames(self):       
        req  = 'http://www.11x11.ru/xml/games/history.php?act=fullhistory'
        soup = GlobalData.CurrentSession.getContent(req)        
        reportNodes = soup.find_all("a", href = re.compile('/reports/'))
        
        reportIDs = []
        for reportNode in reportNodes:
            reportIDs.append(reportNode.attrs['href'].split('/')[2])
        
        self.archiveGames = []
        
        for i in range(min(10,len(reportIDs))):
        
            try:
                print('Extracting', reportIDs[i])
                game = GameArchive.GameExtended(reportIDs[i])
            
                self.archiveGames.append(game)
                
                print('.')
            except Exception as ex:
                print (ex)
                pass
            
        return self.archiveGames
    
    def evaluatePlayers(self, players):
        res = []
        for playedPosition, player in players:
            cf = CostFunctionCache.GlobalCostFunctions.Squad.getCostFunction('BestSkill')
            score = CostEvaluators.PlayerPositionScore(player,cf()).positionScore(playedPosition)
            print score
            res.append((playedPosition, score))
            
        return res
    
    def extractTacticInfo(self, game, idx):
        return [game.strategy[idx], game.tactic[idx], game.schema[idx], game.passingStyle[idx], game.pressing[idx] ]
    
    
    def calculateAggScore(self, playerScores):
        
        aggScore = {'Gk' : 1.0, 'Def' : 1.0, 'Mid' : 1.0, 'Att': 1.0}
        
        for pos, score in playerScores:
            if pos in ['Ld','Rd', 'Cd', 'Sw']:
                aggScore['Def'] = aggScore['Def'] + score
            elif pos in ['Cm','Dm', 'Lm', 'Rm', 'Lw', 'Rw']:
                aggScore['Mid'] = aggScore['Mid'] + score
            elif pos in ['Cf', 'Lf', 'Rf', 'Am']:
                aggScore['Att'] = aggScore['Att'] + score
            elif pos == 'Gk':
                aggScore['Gk'] = aggScore['Gk'] + score                
        
        return aggScore
    
    def calculateAggPowerRatio(self, playerScores1, playerScores2):
        
        aggScore1 = self.calculateAggScore(playerScores1)
        aggScore2 = self.calculateAggScore(playerScores2)
        
        
        return [ aggScore1['Gk']  / aggScore2['Gk']
                , aggScore1['Att']/aggScore2['Def']
                , aggScore1['Def']/aggScore2['Att']
                , aggScore1['Mid'] /aggScore2['Mid']
                ]
        
            
        
    def enrichData(self, game):
        if game.uids[0] =='2' or game.uids[1] =='2':
            print('bot')
            return None
        
        if game.score[0] == game.score[1]:
            return None
            
        
        winnerIdx = 0 if game.score[0] > game.score[1] else 1
        looserIdx = 1 - winnerIdx
        
        winners = self.evaluatePlayers(game.extendedData[winnerIdx])
        loosers = self.evaluatePlayers(game.extendedData[looserIdx])
        winnerInfo = self.extractTacticInfo(game, winnerIdx)
        looserInfo = self.extractTacticInfo(game, looserIdx)
        
        powerRatio = None
        try:
            powerRatio = self.calculateAggPowerRatio(winners, loosers)
        except Exception as ex:
            print('Failed to get ratio', ex)
            
        print(powerRatio)
        return [ [ winnerInfo, winners], [ looserInfo, loosers] , powerRatio]


import argparse
 

#parser = argparse.ArgumentParser(description='11x11 Bot')
#parser.add_argument('test')
#parser.add_argument('--user', help='11x11.ru user')
#args = None# parser.parse_args()
#args.user='RavenXXX'

GlobalData.UserCfg = UserConfig('RavenXXX')

while True:
    try:       
        enrichedOld = None
        try:
            with open('outdata_new.txt', 'r') as f:
                enrichedOld = pickle.load( f )
        except:
            enrichedOld = {}
              
        gameSession = Session.GameSession()
        gameSession.initSession()
        arch = GlobalGameArchive()       
        games = arch.fetchGames()
        enriched = {}
        
        for gm in games:
            try :
                enrichedOne = arch.enrichData(gm)
                if enrichedOne != None and enrichedOld.get(gm.gameID) == None :
                    enriched [gm.gameID] = enrichedOne
            except Exception as ex:
                    print('Cant extract' , ex)
        
        if len(enriched) > 0:
            with open('outdata_new.txt', 'w') as f:
                enrichedOld.update(enriched)
                pickle.dump(enrichedOld, f )
    except Exception as ex:
        print ex
        pass




