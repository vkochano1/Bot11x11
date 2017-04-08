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

	def updateHistogram(hist, val):
		counter = hist.get(val)
		hist[val] = counter + 1 if counter != None else 1 

	def updateHistogramWithRounding(hist, val, roundingBase):
		val = int (val / roundingBase) * roundingBase  + (roundingBase if val % roundingBase > int(roundingBase/2) else 0) 
		counter = hist.get(val)
		hist[val] = counter + 1 if counter != None else 1 
	
	for report in reports:
			gameReport = report.getStatsFor(userID)	
			[strength, schema, tactic, pressing, strategy, passingStyle] = gameReport
			updateHistogram(strategyHist, strategy)
			updateHistogram(schemaHist, schema)
			updateHistogramWithRounding(tacticHist, tactic, 5)			
			
	print(strategyHist, schemaHist, tacticHist)

        contraData = ContraData()					
	schema = contraData.findMostFrequent(schemaHist)
	strategy = contraData.findMostFrequent(strategyHist)
	tactic = contraData.findMostFrequent(tacticHist)

	try:
		print schema, strategy, tactic
		
		tacticCF = TacticCache.GlobalTacticCache.Main.getCostFunction(GlobalData.UserCfg.GameTactic)
		r = tacticCF().getContraData(schema, strategy, str(tactic))

                ret = (	r.formation, r.strategy, int(r.tactic))	
		if len([val for val in ret if val == None]) > 0:		
			raise Exception('Invalid data')   	

	except Exception as ex:
		print 'Failed!!!!!' + str (ex)
		tactic =  random.randint(10,25)
		formation = random.choice(['442', '352'])
		strategy= random.choice(['Normal','LongShots','Dribbling', 'Passing'])
		ret = (formation, strategy, tactic)

	print ('Using', ret)
	return ret
