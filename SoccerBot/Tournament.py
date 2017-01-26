# -*- coding: utf-8 -*-
import autopy
import math
import time
import random
import Analyser
import Config
import random
import requests

import re

from Config import *
from PlayMatch import *
import TeamPlayers
from bs4 import BeautifulSoup
import Recovery 
from TournamentPosition import *



class SquadSelectionTactic(object):

	def __init__(self):
		pass
	
	def getScoreBest(self, player, pos):
		return TeamPlayers.PlayerEffectiveness(player, BestSkillPriority()).positionScore(pos)
	
	def getHealthy(self, player, pos):
		return TeamPlayers.PlayerEffectiveness(player,TalentAndReadinessPriority()).positionScore(pos)
				

	def getSelector(self,  formPositions, stage, players):
		print ('stage ' + str(stage))	
		if stage < 16 :
				return TeamPlayers.BestSquadSelector(formPositions, players, self.getScoreBest)
		else:
				return TeamPlayers.BestSquadSelector(formPositions, players, self.getHealthy)		

class Tournament(object):
	
	def __init__(self):
		self.tournamentID = None
		self.prevGameID  = None
		self.currentGameID = None
	
	def populateOpenTournamentsList(self):
		response = GlobalData.CurrentSession.get(GlobalData.TournamentsLink)
				
		htmlDom = BeautifulSoup(response.content, 'html.parser')
		allTournamentLinks = htmlDom.find_all('a', href=re.compile("\/tournaments\/"))
		tornamentIDs = []
		for tournamnetLink in allTournamentLinks:
			id = tournamnetLink.attrs['href'].split('/')[2]
			tornamentIDs.append(id)
		return tornamentIDs

	def waitForStart(self):		
		response = GlobalData.CurrentSession.get(GlobalData.ActiveTournamentPrefix+ self.tournamentID)

		while True == self.isWaitingForTournament(response):
			time.sleep(GlobalData.TournamentStartedCheckInterval)
			print('.')
			response = GlobalData.CurrentSession.get(GlobalData.ActiveTournamentPrefix+ self.tournamentID)
			
	def extractTournamentId(self):
		req  = GlobalData.Site + '/xml/games/tournaments.php'
		r = GlobalData.CurrentSession.get(req)
				
		soup = BeautifulSoup(r.content, 'html.parser')
		schemaNode = soup.find("script", text = re.compile('document.location.href='))
		if schemaNode == None:
			return None
		return schemaNode.text.split('/')[-1].strip(';').strip("'")
	
	
	def isTechnicalWorks(self):
		r = GlobalData.CurrentSession.get(GlobalData.Site)
		soup = BeautifulSoup(r.content, 'html.parser')	
		res2 = soup.find('img', src=re.compile("works.jpg"))
		return res2 != None

	def needSomeRest(self):
		r = GlobalData.CurrentSession.get(GlobalData.Players)
				
		soup = BeautifulSoup(r.content, 'html.parser')
		g = soup.find('tr', attrs = {'class' : 'header'})
		colls = g.find_all('center')
		print ('Physio ratio' + str(float(colls[5].text) / float(colls[3].text)))
		perc = 100 * float(colls[5].text) / float(colls[3].text)
		print('Perc wait' + str(perc))
		return (100 - perc) * 60;
		

		
	def isWaitingForTournament(self, response):
		htmlDom = BeautifulSoup(response.content, 'html.parser')
		canCancelTournament = htmlDom.find('a', href=re.compile("\/tournaments\/"+ self.tournamentID + "\/act=cancel"))	
		canCancelTournament = htmlDom.find('a', href=re.compile("\/act=cancel"))
		print(canCancelTournament)
		return canCancelTournament != None 

	def stillInGame(self):
		r = GlobalData.CurrentSession.get(GlobalData.Site + '/tournaments/'+ self.tournamentID)
		
		soup = BeautifulSoup(r.content, 'html.parser')
		
		isInGameNode = soup.find(['b','td'], text=re.compile(ur'Вы играете в', re.UNICODE) )

		if isInGameNode == None:
			return (None, False)

		if soup.find(['b','td'], text=re.compile(ur'Вы играете в финале', re.UNICODE) ):
			return (1, False)

		stage  = 1
		try:
			print (isInGameNode.text)
			match = re.search('\d\/(\d+)', isInGameNode.text, re.UNICODE)
			stage = int(match.group(1))
				
		except:
			stage = 1
		
		return (stage, False)


	def nextGameID(self):
		response = GlobalData.CurrentSession.get(GlobalData.Site + '/tournaments/'+ self.tournamentID)
		
		soup = BeautifulSoup(response.content, 'html.parser')
		gameLink = soup.find('a', href=re.compile("\/builder\/\?id="))
		if gameLink == None:
			return None
		
		return gameLink.attrs['href'].split('=')[-1]	
	
	def waitForNextGame(self):

		self.currentGameID = self.nextGameID()

		while self.currentGameID == None or self.prevGameID == self.currentGameID:
			(stage, isGroup) = self.stillInGame()
			if stage == None:
				self.currentGameID = None
				break
			time.sleep(GlobalData.CheckIfOpponentIsAvailableInterval)
			self.currentGameID = self.nextGameID()
			print('Waiting for the opponent ' + str(stage) )
	
		return self.currentGameID

	def getOpponentID(self):
		tournamentLink  = GlobalData.ActiveTournamentPrefix + self.tournamentID
		response = GlobalData.CurrentSession.get(tournamentLink)
		htmlDom = BeautifulSoup(response.content, 'html.parser')
		gameLink = htmlDom.find("a", text = re.compile(u'Перейти', re.UNICODE))
		userNode  = gameLink.parent.parent.find("a", href = re.compile('/users/'))
		userID = userNode.attrs['href'].split('/')[2]
		return userID
	
	def joinNextToPlay(self):
		tournaments = self.populateOpenTournamentsList()
		if len(tournaments) == 0:
			return None
		firstTournament = tournaments[0]	
		self.joinTournament(firstTournament)
		return firstTournament

	def checkReport(self, matchID):
		report  = GlobalData.Site + '/reports/' + matchID
		r = GlobalData.CurrentSession.get(report)		
		soup = BeautifulSoup(r.content, 'html.parser')
		print('Opening report' + report)		

	def joinTournament(self, id):
		reqJoin = GlobalData.ActiveTournamentPrefix+ id + '/act=join&step=1'
		r = GlobalData.CurrentSession.get(reqJoin)
		return	


	def pickPlayers(self, formation, stage):	
			formPositions = MatchSettings.SchemaMapping[formation]

			info = TeamPlayers.PlayersInfo();

			players = []
			playersByRefId = {}

			for playerID, playerInfo in info.playerInfoByRefId.iteritems():
			    player = TeamPlayers.Player (playerID, info)
			    players.append(player)
			    playersByRefId[playerID] = player
			    print('Added ' + str(player))

			print('searching for the best combination')

			print(formPositions)
			selector = SquadSelectionTactic().getSelector(formPositions,stage, players)	
			bestSquad  = selector.findBestCombination()
			
			print(bestSquad)
			principalSquad = PrincipleSquad ()

			for playerID, position in bestSquad.iteritems():
			    principalSquad.addPlayer(playersByRefId[playerID], position)
			return principalSquad		

	def needBoost(self, stage, isGroup, opponentID, players):
		#if stage <= 2:
		#	GlobalData.CurrentSession.get('http://11x11.ru/xml/players/practice.php?activate=1')
		#if stage <= 16:
		Recovery.healSquadPlayers(players)
		
	def playTournament(self):
		random.seed(time.time())
		wasTechnical = False

		### Wait until techicals works are done
		while self.isTechnicalWorks():
			time.sleep(GlobalData.TechnicalWorksDoneCheckInterval)
			wasTechnical = True
			print 'Techical works'


		self.tournamentID = self.extractTournamentId()
		
		if self.tournamentID == None:
			self.needSomeRest()
			self.tournamentID = self.joinNextToPlay()
			self.waitForStart()	
		else:
			self.waitForStart()
				
		prevMatchID = None

		(stage, isGroup) = self.stillInGame()

		while  stage != None:
			
			if not self.waitForNextGame():
				return
			
			opponentID = self.getOpponentID()
	
			tp = TournamentPosition(self.tournamentID)
			while tp.canPass(opponentID) == True:
				time.sleep(20)
				print('Passing the game')
				tp = TournamentPosition(self.tournamentID)

			res = Analyser.extractContraData(opponentID)
			
			[formation,strategy,tactic ] = res
			selectedSquad = self.pickPlayers(formation, stage)
			
			self.needBoost(stage, isGroup, opponentID,selectedSquad.allPlayers)
			
			##roles
			roles = Roles()
			#squadPlayers = [player for pos, player in selectedSquad.aPlayers.iteritems()]
			TeamPlayers.RoleSelector(selectedSquad.allPlayers,RolesPriority()).assignRoles(roles)

			matchSettings = MatchSettings(formation, strategy, tactic, 'Mixed')
			matchOrder = MatchOrder(GlobalData.UserID, self.currentGameID, matchSettings, selectedSquad, roles, None)
			matchOrder.serializeOrder()
			matchOrder.sendOrder()

			self.checkReport(self.currentGameID)
			time.sleep(60)
			self.prevGameID = self.currentGameID
			(stage, isGroup) = self.stillInGame()
			



	


	
	





