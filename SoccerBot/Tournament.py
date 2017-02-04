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
from bs4 import BeautifulSoup
import Recovery 
from TournamentPosition import *

import CombinationWalker
import CostEvaluators
import PlayerInfo
import CostFunctions
import logging
from cookielib import logger
import GameArchive		

class Tournament(object):
	
	def __init__(self):
		self.logger = logging.getLogger(self.__class__.__name__)
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
			self.logger.info('Tournament %s is not started yet, waiting' % (self.tournamentID) )
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
		self.logger.info('Current Physio is ' + str(float(colls[5].text) / float(colls[3].text)))
		perc = 100 * float(colls[5].text) / float(colls[3].text)
		self.logger.info('Estimated time to wait %s (sec)' + str(perc))
		return (100 - perc) * 60;

		
	def isWaitingForTournament(self, response):
		htmlDom = BeautifulSoup(response.content, 'html.parser')
		canCancelTournament = htmlDom.find('a', href=re.compile("\/tournaments\/"+ self.tournamentID + "\/act=cancel"))	
		canCancelTournament = htmlDom.find('a', href=re.compile("\/act=cancel"))
		return canCancelTournament != None 

	def stillInGame(self):
		tournamentPosition = TournamentPosition(self.tournamentID)
		
		tournamentPosition.fetchLatestState()
		
		self.logger.info('Current Tournament State  \n %s' % str(tournamentPosition))
				
		if tournamentPosition.stillInGame != True:
			return (None, False)
		
		return (tournamentPosition.stage, tournamentPosition.inGroup)


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
			self.logger.info('Waiting for the opponent ' + str(stage) )
	
		self.logger.info('Warming up for new game (%s)' % self.currentGameID)
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
		tracker = GameArchive.MatchReportTracker(matchID)
		tracker.waitUntilReportIsReady()
				

	def joinTournament(self, id):
		reqJoin = GlobalData.ActiveTournamentPrefix+ id + '/act=join&step=1'
		r = GlobalData.CurrentSession.get(reqJoin)
		return	


	def pickPlayers(self, formation, stage):	
			formPositions = MatchSettings.SchemaMapping[formation]

			info = PlayerInfo.PlayerDataTable();

			players = []
			playersByRefId = {}

			for playerID, playerInfo in info.playerInfoByRefId.iteritems():
			    player = PlayerInfo.Player (playerID, info)
			    players.append(player)
			    playersByRefId[playerID] = player
			    
			    self.logger.info('Updated data for player: %s' % str(player.ID))

			selector = CostFunctions.SquadSelectionTactic().getSelector(formPositions,stage, players)	
			bestSquad  = selector.findBestCombination()
			
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
			logging.info('Maintenance works are in progress, waiting')
			


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
			tp.fetchLatestState()
			while tp.canPass(opponentID) == True:
				time.sleep(20)
				tp.fetchLatestState()

			res = Analyser.extractContraData(opponentID)
			
			[formation,strategy,tactic ] = res
			selectedSquad = self.pickPlayers(formation, stage)
			
			self.needBoost(stage, isGroup, opponentID,selectedSquad.allPlayers)
			
			##roles
			roles = Roles()
			#squadPlayers = [player for pos, player in selectedSquad.aPlayers.iteritems()]
			CostEvaluators.PlayerRoleScore(selectedSquad.allPlayers,CostFunctions.RolesPriority()).assignRoles(roles)

			matchSettings = MatchSettings(formation, strategy, tactic, 'Mixed')
			matchOrder = MatchOrder(GlobalData.UserID, self.currentGameID, matchSettings, selectedSquad, roles, None)
			matchOrder.serializeOrder()
			matchOrder.sendOrder()

			self.checkReport(self.currentGameID)
			time.sleep(60)
			self.prevGameID = self.currentGameID
			(stage, isGroup) = self.stillInGame()
			



	


	
	





