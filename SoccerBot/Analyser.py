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
from HTMLParser import HTMLParser
from Config import *


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def __init__ (self):
		
		HTMLParser.__init__(self)
		self.out = ''
    
	def handle_starttag(self, tag, attrs):

		if tag in ['table','tr','td', 'html','body', 'tbody','a']:
			
			href =''
			for  t, v in attrs:
				if t == 'href':
					href = 'href=' + v
					 
        		
			self.out = self.out + '<%s %s>'% (tag, href)

	def handle_endtag(self, tag):
		if tag  in ['table','tr','td', 'html','body', 'tbody','a']: 
        		self.out = self.out + '</%s>'% tag
        
    	def handle_data(self, data):
		self.out = self.out + data


class ArchiveGame(object):
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

		strategyMapping = { u"нормальная": "Normal",
				    u"игра в пас": "Passing",
				    u"техничная игра" : "Dribbling", 
				    u"дальние удары": "LongShots" 	
		} 
		return strategyMapping.get(strategyStr)

	@staticmethod
	def extractPassingStyle(passingStyleStr):

		passingMapping = { u"дальние": "Long",
				    u"смешанные": "Mixed",
				    u"короткие" : "Short" 	
		} 
		return passingMapping.get(passingStyleStr)
	
	@staticmethod
	def extractPressing(pressingStr):

		pressingMapping = { u"нет": False,
				    u"да":  True}
			
		pressEnabled = pressingMapping.get(pressingStr)
	    	if pressEnabled == None:
			
			return False
		return pressEnabled

	def getStatsFor(self,userID):
		if self.uids[0] == userID:
			idx = 0
		elif self.uids[1] == userID:
			idx = 1
		else:
			return None
		
		return [ self.strength[idx], self.schema[idx], self.tactic[idx], self.pressing[idx], self.strategy[idx],self.passingStyle[idx]  ]
			

	def __init__(self, gameID):
		req = 'http://www.11x11.ru/reports/' + gameID
		response = GlobalData.CurrentSession.get(req)
		parser = MyHTMLParser()
		parser.feed(response.content)
		
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
		rows = matchReportTable.findAll('tr')
		table = []		
		for row in rows:
			cols = row.findAll('td')
			table.append([cols[0].text, cols[2].text])
	
		self.strength =  [ArchiveGame.extractStrength(v) for v in table[2] ]  
		self.schema =  [ArchiveGame.extractSchema(v) for v in table[3] ] 
		self.tactic =  [ArchiveGame.extractTactic(v) for v in table[4] ]
		self.pressing =  [ArchiveGame.extractPressing(v) for v in table[5] ]
		self.strategy =  [ArchiveGame.extractStrategy(v) for v in table[6] ]
		self.passingStyle =  [ArchiveGame.extractPassingStyle(v) for v in table[7] ]
		self.gameID = gameID		
		print self.__dict__
		


def getReportsForUser(user, N):
	req  = GlobalData.ArchiveGameForUserPrefix + user
	response = GlobalData.CurrentSession.get(req)
	
	parser = MyHTMLParser()
	parser.feed(response.content)
	soup = BeautifulSoup(parser.out, 'html.parser')
	reportNodes = soup.find_all("a", href = re.compile('/reports/'))

	reportIDs = []
	for reportNode in reportNodes:
		reportIDs.append(reportNode.attrs['href'].split('/')[2])
	
	archiveGames = []
	for i in range(min(len(reportIDs),N) ):
		
		try:
			game = ArchiveGame(reportIDs[i])
			[strength, schema, tactic, pressing, strategy, passingStyle ] = game.getStatsFor(user)
			if schema != None and strategy != None and tactic != None:			
				archiveGames.append(game)
		except:
			pass
			
				
	return archiveGames




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
	
	reports = getReportsForUser(userID, 8)
	
	print(reports)
	
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
			print(gameReport)
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
	try:
		contraSch = findContraSchema(schema)
		ret =  ( contraSch, findContraStrategy(strategy), findContraTactic(tactic, contraSch) )
		print(ret)		
		if len([val for val in ret if val == None]) > 0:
		 	raise Exception('Invalid data')   	
		print('OKKKKKKKK')
	except:
		print 'Failed!!!!!'
		tactic =  random.randint(10,25)

		print('DSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSDSDSDS')
		formation = random.choice(['442', '352'])

		strategy= random.choice(['Normal','LongShots','Dribbling', 'Passing'])
		ret = (formation, strategy, tactic)

	print (ret)
	return ret
