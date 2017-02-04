# -*- coding: utf-8 -*-
import math
import time
import random
import re
import random
import os
import sys
import requests
from bs4 import BeautifulSoup
import PlayerInfo
import logging

from Config import *
import GameArchive



class ContraData(object):

	def findMostFrequent(self, hist):
		prevMax = 0
		mostFreq = None
		for k, v in hist.iteritems():
			if v > prevMax:
				mostFreq  = k
				prevMax = v
		return mostFreq

		
	def findContraStrategy(self,strategy):

		ret = None
		if strategy == 'Normal':
			ret = "Passing" 
		elif strategy =="Passing":
			ret = "Dribbling" 
		elif strategy =="Dribbling":
			ret = "LongShots" 
		elif strategy =="LongShots":
			ret = "Normal" 

		return ret


	def findContraSchema(self, schema):

		ret = None
	
		if schema in ['352', '343', '532', '451', '244', '424', '262']:
			formation = ['352']
			ret = random.choice(formation) 
		elif  schema in ['433', '433W', '424', '541', '343', '253', '163']:
			ret = "442"
		else:
			formation = ['442', '442', '352']
			fres = random.choice(formation)
			ret = fres	
		return ret



	def findContraTactic(self, tactic, schema = None):
		if tactic == None or schema == None:
			return None
		if schema.startswith('442'):
			contra = {0: 5, 65: 20, 35: 0, 100: 0, 5: 5, 70: 15, 40: 10, 10: 5, 75: 10, 45: 15, 15: 15, 80: 15, 50: 15, 20: 15, 85: 5, 55: 5, 25: 0, 90: 15, 60: 15, 30: 30, 95: 10}
		elif schema.startswith('343'):
			contra = {0: 5, 65: 15, 35: 5, 100: 10, 5: 15, 70: 5, 40: 5, 10: 15, 75: 15, 45: 20, 15: 15, 80: 0, 50: 0, 20: 15, 85: 5, 55: 0, 25: 15, 90: 0, 60: 15, 30: 15, 95: 0}
		elif schema.startswith('433'):
			contra = {0: 0, 65: 5, 35: 5, 100: 0, 5: 15, 70: 35, 40: 0, 10: 0, 75: 0, 45: 30, 15: 5, 80: 40, 50: 10, 20: 5, 85: 5, 55: 10, 25: 15, 90: 5, 60: 10, 30: 20, 95: 0}
		elif schema.startswith('352'):
			contra = {0: 15, 65: 0, 35: 5, 100: 0, 5: 15, 70: 0, 40: 15, 10: 15, 75: 15, 45: 10, 15: 15, 80: 15, 50: 20, 20: 15, 85: 20, 55: 0, 25: 15, 90: 5, 60: 0, 30: 15, 95: 20}
		else:
			return 13		
		return contra[tactic]

def extractContraData(userID):
	if userID != '2':
		opponentInfo = PlayerInfo.PlayerDataTable(userID)
		logging.info('Opponent team %s' % str(opponentInfo))

	userGames  = GameArchive.UserGameArchive(userID,10)
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
	
	print('All reports', len (reports))
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
		contraSch = contraData.findContraSchema(schema)
		ret =  ( contraSch, contraData.findContraStrategy(strategy), contraData.findContraTactic(tactic, contraSch) )
		print(ret)		
		if len([val for val in ret if val == None]) > 0:		
			raise Exception('Invalid data')   	

	except Exception as ex:
		print 'Failed!!!!!' + str (ex)
		tactic =  random.randint(10,25)

		print('DSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSDSDSDS')
		formation = random.choice(['442', '352'])

		strategy= random.choice(['Normal','LongShots','Dribbling', 'Passing'])
		ret = (formation, strategy, tactic)

	print (ret)
	return ret
