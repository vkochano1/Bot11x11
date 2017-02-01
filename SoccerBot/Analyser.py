# -*- coding: utf-8 -*-
import autopy
import math
import time
import random
import re
import random
import os
import sys
import requests
import browsercookie
from bs4 import BeautifulSoup

from Config import *
import GameArchive


def findMostFrequent(hist):
	prevMax = 0
	mostFreq = None
	for k, v in hist.iteritems():
		if v > prevMax:
			mostFreq  = k
			prevMax = v
	return mostFreq

		
def findContraStrategy(strategy):
	"""игра в пас эффективна против нормальной стратегии
нормальная стратегия эффективна против дальних ударов
дальние удары эффективны против техничной игры
техничная игра эффективна против игры в пас
нормальная игра эффективна против техничной игры"""

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


def findContraSchema(schema):

	"""4-3-3 против 3-5-2, 3-4-3, 5-3-2, 4-5-1, 2-4-4, 4-2-4, 2-6-2
	   4-4-2 против 4-3-3, 4-2-4, 5-4-1, 3-4-3, 2-5-3, 1-6-3
	"""

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



def findContraTactic(tactic, schema = None):
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
		contra = '442'		
	print contra[tactic]
	print schema
	return contra[tactic]

def extractContraData(userID):

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
		
	for report in reports:
			gameReport = report.getStatsFor(userID)	
			#self.logging.info('----- Analyzing game report ----\n %s ' % str(gameReport))
			[strength, schema, tactic, pressing, strategy, passingStyle] = gameReport
			updateHistogram(strategyHist, strategy)
			updateHistogram(schemaHist, schema)
			updateHistogramWithRounding(tacticHist, tactic, 5)
			
			
	print('Hist')
	print(strategyHist, schemaHist, tacticHist)					
	schema = findMostFrequent(schemaHist)
	strategy = findMostFrequent(strategyHist)
	tactic = findMostFrequent(tacticHist)

	
	print('Most freq')
	print(schema)
	print(strategy)
	print(tactic)
	print('Done')
	#try:
	contraSch = findContraSchema(schema)
	ret =  ( contraSch, findContraStrategy(strategy), findContraTactic(tactic, contraSch) )
	print(ret)		
	if len([val for val in ret if val == None]) > 0:
		raise Exception('Invalid data')   	
	print('OKKKKKKKK')
	#except:
	#	print 'Failed!!!!!'
	#	tactic =  random.randint(10,25)

	#	print('DSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSDSDSDS')
	#	formation = random.choice(['442', '352'])

	#	strategy= random.choice(['Normal','LongShots','Dribbling', 'Passing'])
	#	ret = (formation, strategy, tactic)

	print (ret)
	return ret
