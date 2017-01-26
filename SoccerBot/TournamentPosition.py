# -*- coding: utf-8 -*-
from  Config import *
from bs4 import BeautifulSoup
import re

class TournamentPosition(object):

	def canPass(self, opponentID):

		print(GlobalData.UserID)
		if self.inGroup == True:
			leader = self.groupStats[0]
			second = self.groupStats[1]
			third  = self.groupStats[2]
			looser = self.groupStats[3]
			
			if leader['Score'] == 6 and second['Score'] == 6:
				if leader['ID'] == GlobalData.UserID and  opponentID == second['ID']:
					return True

				if second['ID'] == GlobalData.UserID and  opponentID == leader['ID']:
					return True
				
			if looser['Played'] == 2 and looser['ID'] == GlobalData.UserID and looser['Score'] == 0 :
				return True

			return False
		else:
			return False
				
			
	def __init__(self,tournamentID):
		tournaMentView = GlobalData.CurrentSession.get(GlobalData.Site + '/tournaments/'+ tournamentID)
		htmlDom = BeautifulSoup(tournaMentView.content, 'html.parser')		
		isInGameNode = htmlDom.find(['b','td'], text=re.compile(ur'Вы играете в', re.UNICODE) )
		match = re.search('\d\/(\d+)', isInGameNode.text, re.UNICODE)
		stage = int(match.group(1))
		groupTable = isInGameNode.parent.find('table')

		self.groupStats = []
		self.inGroup = False
		if groupTable != None:
			rows = groupTable.find_all('tr')
			if len(rows) >= 5:
				playerStat = []	
				self.inGroup = True

				for row in groupTable.find_all('tr')[1:]:
					columns = row.find_all('td')
					played = int(columns[3].text)
					playerID = columns[2].find('a').attrs['href'].split('/') [-1]
					won = 	int(columns[4].text)
					draw = int(columns[5].text)
					lost = int(columns[6].text)
					diff = 	[ int(i) for i in columns[7].text.split('-')]
					score = int(columns[8].text)							
					self.groupStats.append({'ID' : playerID, 'Played' : played,'Won' : won, 'Draw': draw, 'Lost' : lost, 'Diff' : diff, 'Score' : score})

		print self.groupStats

