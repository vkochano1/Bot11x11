# -*- coding: utf-8 -*-
import math
import time
import random
import re
import random
import os
import sys
import requests
import PlayerInfo
import logging

from Config import *
import GameArchive
import TacticCache



class ContraData(object):

	def findMostFrequent(self, hist):
		prevMax = 0
		mostFreq = None
		for k, v in hist.iteritems():
			if v > prevMax:
				mostFreq  = k
				prevMax = v
		return mostFreq

		

def extractContraData(userID):
	if userID != '2':
		opponentInfo = PlayerInfo.PlayerDataTable(userID)
		logging.info('Opponent team %s' % str(opponentInfo))

	userGames  = GameArchive.UserGameArchive(userID,GlobalData.UserCfg.AnalyseNOpponentReports)
	userGames.fetchGames()
	reports = userGames.games()	
	
	schemaHist = {} 
	strategyHist = {}
	tacticHist = {}
	combinedHash = {}

	def updateHistogram(hist, val):
		counter = hist.get(val)
		hist[val] = counter + 1 if counter != None else 1 

	def updateHistogramWithRounding(hist, val, roundingBase):
		val = int (val / roundingBase) * roundingBase  + (roundingBase if val % roundingBase > int(roundingBase/2) else 0) 
		counter = hist.get(val)
		hist[val] = counter + 1 if counter != None else 1
		

	def updateCombinedHash(combinedHash, strategy, schema, tactic, roundingBase):
                adjustedTactic = int (tactic / roundingBase) * roundingBase  + (roundingBase if tactic % roundingBase > int(roundingBase/2) else 0)
                key = str(adjustedTactic) + str(strategy)+ str(schema)
                val = ( adjustedTactic, strategy, schema)
                tacticInfo  = combinedHash.get(key)
                if  tacticInfo == None:
                        combinedHash[key] = [1,val]
                else:
                        combinedHash[key][0] = combinedHash[key][0] + 1

        def findMostFrequentCombinedHash(combinedHash):
                mostFrequentKey = None
                maxCounter =  0
                for k,v  in combinedHash.iteritems():
                        if maxCounter < v[0]:
                                maxCounter = v[0]
                                mostFrequentKey = k

                if mostFrequentKey == None:
                        return None
                
                return combinedHash[mostFrequentKey]
                
	for report in reports:
			gameReport = report.getStatsFor(userID)	
			[strength, schema, tactic, pressing, strategy, passingStyle] = gameReport
			updateHistogram(strategyHist, strategy)
			updateHistogram(schemaHist, schema)
			updateHistogramWithRounding(tacticHist, tactic, 5)
			updateCombinedHash(combinedHash, strategy, schema, tactic, 5)

        try:
                [counter,(tactic, strategy, schema)] = findMostFrequentCombinedHash (combinedHash)

                if counter <= 1:
                        contraData = ContraData()					
                        schema = contraData.findMostFrequent(schemaHist)
                        strategy = contraData.findMostFrequent(strategyHist)
                        tactic = contraData.findMostFrequent(tacticHist)

	
		
		tacticCF = TacticCache.GlobalTacticCache.Main.getCostFunction(GlobalData.UserCfg.GameTactic)
		r = tacticCF().getContraData(schema, strategy, str(tactic))
                addT = random.choice([0,1,2,3,4])
                ret = (	r.formation, r.strategy, int(r.tactic) + addT)	
		if len([val for val in ret if val == None]) > 0:		
			raise Exception('Invalid data')   	

	except Exception as ex:
                print( str(ex) )
		tactic =  random.randint(10,25)
		formation = random.choice(['442', '352'])
		strategy= random.choice(['Normal','LongShots','Dribbling', 'Passing'])
		ret = (formation, strategy, tactic)

	return ret
