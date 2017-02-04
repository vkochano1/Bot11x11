# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from Config import *
import re
import logging

 
class PlayerDataTable(object):

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
                
	if playerID != '': 
		req = GlobalData.Site +'/users/' + playerID
	else:
		req = GlobalData.Site +'/xml/players/'
        response = GlobalData.CurrentSession.get(req)
	
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

            playerNumber = columns[0].text
            
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
            info ['Number'] = int(playerNumber)

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
    
    def __str__(self):
	       return str(self.playerInfoByRefId)
 

    def __repr__(self):
	       return str(self)

class Player:
    SkillColumns = ['Skl' ,'Tck', 'Mrk' , 'Drb', 'Pos', 'Stm' , 'Pas', 'Shs', 'Sha' ]

    def __str__(self):
        out = ""
        skillsStr = ','.join( [ str("%s=%s" % (k, v)) for k, v in self.Skills.iteritems()] )
        specialAbStr = 	','.join( [ "%s=%s" % (k, v) for k, v in self.ExtraAbilities.iteritems()] )
        positionsStr = '/'.join(self.Positions)
        out = """
-------------------------------------------------------------------------------
Number        : %s
PlayerID      : %s   
Skills        : %s
ExtraAbilities: %s		
Positions     : %s
Age           : %s
Morale        : %s
Readiness     : %s
Talent        : %s 
--------------------------------------------------------------------------------"""% (self.Number, self.ID, skillsStr,  specialAbStr
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
        self.Number = playerInfo['Number']
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
            
		

            
