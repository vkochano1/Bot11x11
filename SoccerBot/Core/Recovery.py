
# -*- coding: utf-8 -*-
import math
import time
import random
import re
import random
import os
import sys
import requests
from Config import *
import Config
import logging


class PlayerHealthRecord(object):
	def __init__ (self, id):
		self.id = id
		self.stamina = 0
		self.morale = 0
		self.injury = 0
		self.position = None

	def __repr__(self):
		return str((self.id, self.stamina, self.morale, self.injury))
		
class TeamHealthState(object):
	def __init__(self):
		self.logger = logging.getLogger(self.__class__.__name__)
		self.players = {}
		s = GlobalData.CurrentSession.getContent(GlobalData.RecoveryDataSnapshot)
		
		allNodes = []
		part1 = s.find_all('input', attrs = {'name' :re.compile('.*[HMI]') })
		part2 = s.find_all('input', attrs = {'name' :re.compile('Stamina') })

		allNodes.extend(part1)
		allNodes.extend(part2)
	
		self.Morale = None
		self.Injury = None
		self.Stamina = None

		for node in allNodes:
			if node.attrs.get('name'):
				name = str(node.attrs['name'])
				value = str(node.attrs['value'])

				if name == 'Morale':
					self.Morale = int(value)
					continue
				elif name == 'Injury':
					self.Injury = value
					continue 
				elif name == 'Stamina':			
					self.Stamina = int(value)
					continue 		

				elif name[-1] in ['H', 'I', 'M']: 
					id = name[0:-1]
					last = name[-1:]
					player = self.players.get(id)
					if player == None:
						player = PlayerHealthRecord(id)
					self.players[id] = player

				if last == 'H':
					player.stamina = int ( value)
				elif last == 'I':
					player.injury = str(value)
				else:
					player.morale = int(value)

	def getStamina(self, id):
			player = self.players.get(id)
			return player.stamina 
		
	def getMorale(self, id):
			player = self.players.get(id)
			return player.morale 
			
	def addStamina(self, id, diff):
			self.logger.info('Increasing stamina for %s by %s' %(id, str(diff) ) )						
			player = self.players.get(id)
			if player and diff <= self.Stamina:
								
				newPlayerStamina = player.stamina + diff
				self.logger.info("Old stamina for %s was %s and now it's %s" % (id
								, str(player.stamina)
								 ,str(newPlayerStamina) ) )
				
				player.stamina = newPlayerStamina
				self.Stamina = self.Stamina - diff
				self.logger.info('Physician power left %s' % str(self.Stamina))
				
			self.logger.info("Morale for %s can't be increased" % (id))
					
	def addMorale(self,  id, diff):
			self.logger.info('Increasing morale for %s by %s' %(id, str(diff) ) )			
			player = self.players.get(id)
			
			if player and diff * 10 <= self.Morale:
				
				newPlayerMorale = player.morale + diff
				self.logger.info("Old morale for %s was %s and now it's %s" % (id, str(player.morale),(newPlayerMorale) ) )
				player.morale = newPlayerMorale
				self.Morale = self.Morale - diff * 10
				self.logger.info('Psychologist power left %s' % str(self.Morale))
				
			self.logger.info("Morale for %s can't be increased" % (id))


class HealthStateChangeRequest(object):
	def __init__(self):
		self.requestData = { 'step': (None, '1')
			   , 'type': (None, 'players/recovery')
			   , 'firstpage' : (None,'/xml/players/recovery.php?')
			   , 'act' : (None,'select')
			   , 'oldact' : (None,'select')			   			   
			   }


	def send(self, state):	
		for k,p in state.players.iteritems():
			self.addPlayer(p)

		self.addStats(state.Morale, state.Injury, state.Stamina, len(state.players))

		
		req  = GlobalData.HealRequest
		GlobalData.CurrentSession.post(req,  files = self.requestData)
	
	def addPlayer(self, player):
		self.requestData[player.id + 'H'] = (None,str(player.stamina))
		self.requestData[player.id + 'M'] = (None,str(player.morale))
		self.requestData[player.id + 'I'] = (None,str(player.injury))

	def addStats(self, m, i, s, n):
		self.requestData['Stamina'] = (None,str(s))
		self.requestData['Morale'] = (None,str(m))
		self.requestData['Injury'] = (None,str(i))
		self.requestData['numrows'] = (None,str(n))


class Positions(object):
	def __init__(self):

		s = GlobalData.CurrentSession.getContent('http://www.11x11.ru/xml/players/')
		
		keeper = s.find('center', text = u'Gk' )

		self.playersByPosition = {}
		self.playersByRefId = {}

		for tr in keeper.parent.parent.parent.find_all('tr')[1:]:
	
			tds = tr.find_all('td')
			if len(tds) < 4:
				continue

			refIdEl = tds[1].find('a')
			positionEl = tds[3].find('center')
 
			if not (refIdEl  and   positionEl):
				continue
		
			refId = str(refIdEl.attrs['href']).split('/')[-1]
			positions = str(positionEl.text).split('/')
	
			for position in positions:	
				bucket = self.playersByPosition.get(position)
				if bucket:
					bucket.append(refId)
				else:
					self.playersByPosition[position] = [refId] 

	def healPosition (self, position, lowLimit, highLimit, maxSpend, state, blackList):
		sumAdded = 0		
		for id in self.playersByPosition[position]:
			pstamina = state.getStamina(id)
			
			if id in  blackList : 
				continue
			valToAdd = 10 if state.Stamina >= 10 else state.Stamina

			if sumAdded + valToAdd > maxSpend:
				valToAdd = maxSpend - sumAdded
			
			if  pstamina < highLimit and pstamina > lowLimit and valToAdd > 0:
				state.addStamina(id, valToAdd)
				sumAdded = sumAdded + valToAdd
				morale = state.Morale
				
				if morale >= 30:
					state.addMorale(id, 3)				
				elif morale >= 20:				
					state.addMorale(id, 2)
				elif morale >= 10:
					state.addMorale(id, 1)
				
			
	def healPlayer (self, playerID, lowLimit, highLimit, maxSpend, state):

			pstamina = state.getStamina(playerID)
						
			sumAdded  = 0
			valToAdd = 10 if state.Stamina >= 10 else state.Stamina

			print playerID

			if sumAdded + valToAdd > maxSpend:
				valToAdd = maxSpend - sumAdded
			
			if  pstamina < highLimit and pstamina > lowLimit and valToAdd > 0:
				state.addStamina(playerID, valToAdd)
				sumAdded = sumAdded + valToAdd
			
			morale = state.Morale
	
			
			if morale >= 30:
				state.addMorale(playerID, 3)				
			elif morale >= 20:				
				state.addMorale(playerID, 2)
			elif morale >= 10:
				state.addMorale(playerID, 1)		
	  	
	def healPlayers(self, state, blackList, priority):
                for pos, low, high, maxToSpend in GlobalData.UserCfg.HealPlayersTactic:
                        self.healPosition(pos, low, high, maxToSpend, state, blackList)


def  healPlayers():
	try:
		state = TeamHealthState()

		positions = Positions()

		positions.healPlayers(state, blackList, [])

		statusReq = HealthStateChangeRequest()

		statusReq.send(state)
	except Exception as ex:
		print('Somehing happened ' + str(ex))

	print('------------------recovery is done ------------------------')

def  healSquadPlayers( players):
	try:
		state = TeamHealthState()

		positions = Positions()

		for player in players:
			if 'Gk' in player.Positions or 'Cf' in player.Positions:
				positions.healPlayer(player.ID,  75, 96, 20, state)
			
		statusReq = HealthStateChangeRequest()

		statusReq.send(state)
	except Exception as ex:
		print('Something happened ' + str(ex))

	print('------------------recovery is done ------------------------')

