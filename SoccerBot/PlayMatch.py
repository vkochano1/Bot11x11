# -*- coding: utf-8 -*-
import requests
import os
import sys
import browsercookie
from bs4 import BeautifulSoup
import time
import md5
from xml.dom import minidom
from Config import *

class MatchSettings(object):
    StrategyMapping = { 'Normal' : 0, 'LongShots' : 1,  'Dribbling' : 2, 'Passing' : 3 }
    SchemaMapping =  { '442' :  ['Gk','Rd', 'Ld', 'Cd', 'Cd', 'Lm', 'Cm', 'Cm', 'Rm', 'Cf', 'Cf']
		     , '352' :  ['Gk','Cd', 'Cd', 'Cd', 'Lm', 'Cm', 'Cm', 'Cm', 'Rm', 'Cf', 'Cf']  
		     , '433' :  ['Gk','Ld', 'Cd', 'Cd', 'Rd', 'Lm', 'Cm', 'Rm', 'Cf', 'Cf', 'Cf']  
  		     , '343' :  ['Gk','Cd', 'Cd', 'Cd', 'Lm', 'Cm', 'Cm', 'Rm', 'Cf', 'Cf', 'Cf']  	   
		     }    
    PassingStyleMapping =   {'Mixed' : 0 , 'Long' : 1,  'Short' : 2 } 
    
    DefaultSchema = '442'
    DefaultStrategy = 'Normal'
    DefaultPassingStyle = 'Mixed'
    DefaultTactic = 12
    DefaultPressing = False

    def __init__(self, schema, strategy, tactic, passingStyle, pressingEnabled = DefaultPressing, premium = None):
            
        self.strategy = MatchSettings.StrategyMapping.get(strategy)
        self.schema = MatchSettings.SchemaMapping.get(schema)
        self.passingStyle = MatchSettings.PassingStyleMapping.get(passingStyle)
        self.premium = premium

        if self.passingStyle == None:
            self.passingStyle = MatchSettings.PassingStyleMapping.get(MatchSettings.DefaultPassingStyle)

            
        if self.schema == None:
            self.schema = MatchSettings.SchemaMapping.get(MatchSettings.DefaultSchema)

        
        if self.strategy == None:
            self.strategy = MatchSettings.StrategyMapping.get(MatchSettings.DefaultStrategy)

            
        if tactic >= 0 and tactic <= 100:
            self.tactic = tactic
        else:
            self.tactic = MatchSettings.DefaultTactic


class PrincipleSquad(object):
    
    Positions = { "Gk" : ("Gk", 1)
                , "Ld" : ("Ld", 1)
                , "Rd" : ("Rd",1)
                , "Cd" : ("Cd",3)
                , "Lm" : ("Lm",1)
                , "Rm" : ("Rm",1)
                , "Cm" : ("Cm",3)
                , "Lf" : ("Lf", 1)
                , "Rf" : ("Rf",1)
                , "Cf" : ("Cf",3)
                }
                
    def __init__ (self):
        self.addedPlayers = {}
	self.allPlayers = []
        self.allPlayersN = 0
        
    def addPlayer(self, player, position):
        players = self.addedPlayers.get(position)
        
        if self.allPlayersN >= 11:
                raise Exception('Reached maximum number of players(11)')
            
        if players != None:
            if len(players) < PrincipleSquad.Positions[position][1]:
                players.append(player)
            else:
                raise Exception('Reached maximum number of players for position' + str(position))
        else:
            self.addedPlayers[position] = [player]
            
	self.allPlayers.append(player)
        self.allPlayersN = self.allPlayersN + 1
	print ('Using player ' + str(player))
        

class Roles(object):
    def __init__(self, captain = None, leftCorners = None, rightCorners = None, penalty = None, freeKicks = None):
        self.Captain = captain
        self.LeftCorners = leftCorners
        self.RightCorners = rightCorners
        self.FreeKicks  = freeKicks
        self.Penalty = penalty
        
        
class Susbstitutions(object):
    def __init__(self):
        self.players =  []
        
    def addPlayer(self, player):
        self.players.append(player)
        
    
class MatchOrder(object):
    
    def __init__(self, userID, orderID, matchSettings, principleSquad, roles, substitutions)  :
        self.userID = userID
        self.orderID = orderID
        self.matchSettings = matchSettings
        self.principleSquad = principleSquad
        self.roles = roles
        self.substitutions = substitutions
        self.serialized = None
        
        
    def serializeOrder(self):
        doc = minidom.Document()
        order = doc.createElement('Order')
        
        ###
        ###  Match settings
        ###
        if self.matchSettings.premium != None :
                order.setAttribute('AwardFee', str(self.matchSettings.premium))
        else:
            order.setAttribute('AwardFee',"")
        
        order.setAttribute('Passing', str(self.matchSettings.passingStyle))
            
        order.setAttribute('Strategy', str(self.matchSettings.strategy))
        order.setAttribute('Tactic', str(self.matchSettings.tactic))
                           
        
        order.setAttribute('Captcha',"0")
        order.setAttribute('UserID', self.userID)
        order.setAttribute('ID', self.orderID)
        order.setAttribute('Name', "")
        
        order.setAttribute('Timestamp', str(int(time.time())))
        
        tasks = doc.createElement('Tasks')
        subs = doc.createElement('Substitutes')
        
        order.appendChild(tasks)
        order.appendChild(subs)
        
        
        ####
        #### Serialize roles
        ####
        roles = doc.createElement('Roles')
        print self.roles
        if self.roles.Captain:
            roles.setAttribute('Captain',self.roles.Captain.ID)
        else:
            roles.setAttribute('Captain','')
            
        if self.roles.LeftCorners:
            roles.setAttribute('LeftCorners',self.roles.LeftCorners.ID)
        else:
            roles.setAttribute('LeftCorners','')
            
        if self.roles.RightCorners:
            roles.setAttribute('RightCorners',self.roles.RightCorners.ID)
        else:
            roles.setAttribute('RightCorners','')
        
        if self.roles.Penalty:
            roles.setAttribute('Penalty',self.roles.Penalty.ID)
        else:
            roles.setAttribute('Penalty','')
            
        if self.roles.FreeKicks:
            roles.setAttribute('FreeKicks',self.roles.FreeKicks.ID)
        else:
            roles.setAttribute('FreeKicks','')  
            
        order.appendChild(roles)
    
        squad = doc.createElement('Squad')
        if self.principleSquad.allPlayersN != 11:
            raise Exception('Invalid number of players')
        for position, positionPlayers in self.principleSquad.addedPlayers.iteritems():
            for player in positionPlayers:
                playerNode = doc.createElement('Player')
                playerNode.setAttribute('ID', player.ID)
                playerNode.appendChild(doc.createTextNode(PrincipleSquad.Positions[position][0]))
                squad.appendChild(playerNode)
            
            
        order.appendChild(squad)
        doc.appendChild(order)
        self.serializedOrder = doc.toxml()
        
        print self.serializedOrder
        
    def sendOrder(self):

        hash = md5.new()
        hash.update(self.serializedOrder + 'AiGhach0')
        hk = hash.hexdigest()


        rdata = { 'function': 'set_order'
                 , 'id': self.orderID
                 , 'hash' : hk
                 , 'championship' : '0'
                 , 'NoCache' : str(int(time.time()))
                 , 'order' : self.serializedOrder 
    
        }
        
        print (rdata)
        
        response = GlobalData.CurrentSession.post(GlobalData.PlayMatchLink, data = rdata)
        print(response.text)
        return response
        



