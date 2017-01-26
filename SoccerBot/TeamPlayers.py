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
from Config import *

 
class PlayersInfo(object):

    ExtraAbilityMapping = { u"Атлетизм": "Athlet", 
		     u"Ауты" : "ThrowIn", 
		     u"Игра головой" : "Heading", 
		     u"Лидер" : "Leader",
		     u"Навесы" : "LongPassing",
		     u"Пенальти" : "Penalty",
		     u"Перехват" : "Interception",
		     u"Плеймейкер": "Playmaker",
		     u"Подкат"    : "Tackling",
		     u"Скорость" : "Speed",
		     u"Угловые"  : "Corners",
		     u"Технарь"  : "Technic",
		     u"Универсал" : "Universal",
		     u"Штрафные"  : "FreeKicks"}


    def __init__(self, playerID = ''):
        
	response = GlobalData.CurrentSession.get(GlobalData.Site +'/xml/players/' + playerID)
	
	htmlDom = BeautifulSoup(response.content, 'html.parser')

        GkRecord = htmlDom.find('center', text = GlobalData.PlayerInfoLookupAnchor )

        table = GkRecord.parent.parent.parent
        
        self.playerIDByPosition = {}
        self.playerInfoByRefId = {}

        playerInfoRows = table.find_all('tr')[1:];
        
        for tr in playerInfoRows:
            columns = tr.find_all('td')
            if len(columns) < 4:
                continue

            IDEl = columns[1].find('a')
            positionEl = columns[3].find('center')
 
            if not (IDEl  and  positionEl):
                continue
        
            refId = str(IDEl.attrs['href']).split('/')[-1]
            positions = str(positionEl.text).split('/')
    
            
            imgs = str(columns[1])
            
            disq = False
            inj = False
            if imgs.find('disq.gif') != -1 :
                disq = True
            if imgs.find('injury.gif') != -1 :
                inj = True
                 
            
            info = {}
            info ['Positions'] = positions
            info ['Readiness'] = float(columns[6].text) 
            info ['Morale']  = int(columns[8].text)
            info ['Injury'] = inj
            info ['RedCard'] = disq
            info ['Age'] = int(columns[4].text)
            info ['Talent'] = int(columns[9].text)

	    extraAbilities = {}
	    info ['ExtraAbilities'] = extraAbilities
 	
	    for ability in columns[10].find_all('span'):
		for k, v in self.ExtraAbilityMapping.iteritems():
			titleText = ability.attrs['title']
			if titleText.startswith(k):
				
				parts = titleText.split('-')
				
				if len(parts[-1]) == 0:
					extraAbilities[v] = 1
				else:
					extraAbilities[v] = int(parts[-1])
 
				

            for position in positions:    
                bucket = self.playerIDByPosition.get(position)
                if bucket:
                    bucket.append(refId)
                else:
                    self.playerIDByPosition[position] = [refId] 

	    
            self.playerInfoByRefId[refId] = info
            

class Player:
    SkillColumns = ['Skl' ,'Tck', 'Mrk' , 'Drb', 'Pos', 'Stm' , 'Pas', 'Shs', 'Sha' ]

    def __str__(self):
	out = ""
	skillsStr = ','.join( [ str("%s=%s" % (k, v)) for k, v in self.Skills.iteritems()] )
	specialAbStr = 	','.join( [ "%s=%s" % (k, v) for k, v in self.ExtraAbilities.iteritems()] )
	positionsStr = '/'.join(self.Positions)
	out = """
---------------------------------------------------------------
PlayerID: %s   
Skills: %s
ExtraAbilities: %s		
Positions: %s
Age: %s
Morale: %s
Readiness: %s
Talent: %s 
	      """ % (self.ID, skillsStr,  specialAbStr
, positionsStr, str(self.Age), str(self.Morale)
, str(self.Readiness), str(self.Talent))
	return out

    def __repr__(self):
	return str(self)
	
    def __init__(self, id, info):
        self.ID = id     
        playerInfo = info.playerInfoByRefId [id]
        self.Positions = playerInfo['Positions']
        self.AllowedToPlay = playerInfo['Injury'] == False and playerInfo['RedCard'] == False and playerInfo['Readiness'] > 20
        self.Skills = {}
        self.Age = playerInfo['Age']
        self.Morale = playerInfo['Morale']
        self.Readiness = playerInfo['Readiness']
	self.Talent = playerInfo['Talent']
        
	self.ExtraAbilities = playerInfo['ExtraAbilities']
        response = GlobalData.CurrentSession.get(GlobalData.Players + id)
        
        htmlDOM = BeautifulSoup(response.content, 'html.parser')
        element = htmlDOM.find('u', text = re.compile(GlobalData.PlayerLookUpAnchor,re.UNICODE ))
        
        table = element.parent.parent.parent
        rows = table.find_all('tr')
        
        idx = 0
        
        for row in rows:
            val = int(row.find('b').text)
            self.Skills[Player.SkillColumns[idx]] = val
            idx = idx + 1
            

class PlayerEffectiveness (object):
    
    def __init__(self, player, detail):
        self.player = player
	self.detail = detail
        
    
    def positionScore(self, pos):
        score = 0
        table = None
        
        ageContribution = self.detail.ageContribution(self.player)
        moraleContribution = self.detail.moraleContribution(self.player)
	talentContribution = self.detail.talentContribution(self.player)
	readinessEffect = self.detail.readinessEffect(self.player)
	
	#print(ageContribution,moraleContribution ,talentContribution,readinessEffect)
	## penalty for placing at position that was not trained
        penalty = 1.0
        
	## goalkeepers
        if self.player.Positions[0] == 'Gk' and pos == 'Gk':
            score = self.player.Skills['Skl']
        else:
        	if pos not in self.player.Positions:
            		penalty = 0.7
		table = self.detail.Stats[pos]
            
        	for skl, val in self.player.Skills.iteritems():
            		if skl == 'Skl':
                		continue
            		coef = table.get(skl) or 1
            		score = score + coef * val
        

	readiness =  (self.player.Readiness / 100.0) ** readinessEffect 
        print(readiness)	
	#print(score, ageContribution, moraleContribution ,talentContribution, readinessEffect)
	
	res = (score + ageContribution + moraleContribution)  * (readiness) * penalty  +  talentContribution
	#print (res)
	return res
	


class RoleSelector(object):
	def __init__(self, players, detail):
		self.detail = detail
		self.players = players
		self.scoreFuncMap = { 'Captain' : detail.captainScore,
				'Penalty' : detail.penaltyScore,
				'FreeKicks' : detail.freeKicksScore,
				'LeftCorners' :detail.leftCornersScore,
				'RightCorners' : detail.rightCornersScore}


	def processNewScore(self, player, scoreID, allScores):
		print(player.ID)
		newVal = self.scoreFuncMap[scoreID](player)
		if newVal > allScores[scoreID][0]:
			allScores[scoreID] = (newVal, player)
	
	def assignRoles(self, roles):
		bestScores = { 'Captain' : (0, None),
				'Penalty' : (0, None),
				'FreeKicks' : (0, None),
				'LeftCorners' : (0, None),
				'RightCorners' : (0, None) }

			
		for player in self.players:
			self.processNewScore(player,'Captain', bestScores)
			self.processNewScore(player,'Penalty', bestScores)
			self.processNewScore(player,'FreeKicks', bestScores)
			self.processNewScore(player,'LeftCorners', bestScores)
			self.processNewScore(player,'RightCorners', bestScores)


		for scoreID , (score, player) in bestScores.iteritems():
			roles.__dict__[scoreID] = player
		

import itertools

class BestSquadSelector(object):
    def __init__(self, schemaPositions, players, costFunc):
        
	self.schemaPositions = []
	tmp = {}
	for pos in schemaPositions:
		tmp[pos] = (tmp.get(pos) or 0) + 1

	for k, v in tmp.iteritems():
		self.schemaPositions.append((k,v))


        self.playersByPosition = []
	self.costFunc = costFunc
	self.players = [player for player in players if player.AllowedToPlay == True ]
	
	for position, numPlayers in self.schemaPositions:
            posPlayers = []
            for player in self.players:
                if position in player.Positions:			                 
  	            	score = self.costFunc(player, position)
		    	posPlayers.append( (player, score) )

            self.playersByPosition.append(posPlayers)
     	

    def lockCombination(self, combination, position,  lockDict):
	aggScore = 0
	for player, score in combination:
		lockDict [ player.ID ] = position
		aggScore = aggScore + score

	return aggScore

    def unlockCombination(self, combination, lockDict):
	for player, score in combination:
		del lockDict [player.ID]
	

    def isCombinationLocked(self, combination, lockDict):
	for player, score in combination:
	    	if lockDict.get(player.ID) != None:
                	return True 
	return False             
			
    def  findBestCombination(self):

	   self.bestScore = 0
           self.bestCombination = None 
	   
	   print('------------------------- STARTED -----------------')
	   start = time.time()
           usedIDs = {}
           self._findBestCombination(0, usedIDs, 0)
	   end = time.time()
	   
	   print('------------------------- STOPPED ----------------- > ' + str(end-start) + ' seconds')
	   
           return self.bestCombination

    def exitCondition(self, currentIdx, score, usedIDs):
        if currentIdx == len(self.schemaPositions):
	    if score > self.bestScore:
                    self.bestScore = score
                    self.bestCombination = usedIDs.copy()
		    print('changed new best' + str (self.bestCombination) + str(self.bestScore) )
            return True
	return False	
        

    def borrowPlayersFromAnotherPosition(self, currentIdx, position, players, playersRequired, usedIDs):
	needPlayersNum = playersRequired - len(players) 

	scoreAgg = self.lockCombination(players, position, usedIDs)
	
	scores = [] 

	for player in self.players:
		score = self.costFunc(player, position)
			
		if True == self.isCombinationLocked([(player, score)], usedIDs):
			continue
		
		
		scores.append((player, score))


	scores.sort(key=lambda tup: tup[1], reverse = True)
	
	bestN = scores[:needPlayersNum]
	
	scoreAgg = scoreAgg + self.lockCombination(bestN, position, usedIDs)

	self._findBestCombination(currentIdx + 1, usedIDs, scoreAgg)
	

	self.unlockCombination(players, usedIDs)
	self.unlockCombination(bestN, usedIDs)
	

    def  _findBestCombination(self, currentIdx, usedIDs, prevScore):

	if self.exitCondition(currentIdx, prevScore, usedIDs) == True:
		return

        players = self.playersByPosition[currentIdx]
	(pos, playersRequired) = self.schemaPositions[currentIdx]
	

	if len(players) < playersRequired:
		self.borrowPlayersFromAnotherPosition(currentIdx, pos, players, playersRequired, usedIDs)
		return


        for combination in itertools.combinations(players, playersRequired) :

	    
	    if self.isCombinationLocked(combination,usedIDs) == True:
		continue

	    scoreAgg = self.lockCombination(combination, pos, usedIDs)

	    newScore = prevScore + scoreAgg
            
            self._findBestCombination(currentIdx + 1, usedIDs, newScore)		                    


	    self.unlockCombination(combination, usedIDs)
            
