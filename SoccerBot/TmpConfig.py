# -*- coding: utf-8 -*-
import requests


class GlobalData(object):

	LoginUser =  'TobBotR'
    	LoginPassword = 'TobBotR1234'
    
	UserID = '3823292'
	TournamentStartedCheckInterval = 30
	CheckIfOpponentIsAvailableInterval = 30
	TechnicalWorksDoneCheckInterval = 0.35	

	Site = 'http://www.11x11.ru/'
	Players = Site + '/players/'
	PlayerLookUpAnchor = u'Мастерство'
	PlayerInfoLookupAnchor = u'Gk'	
	TournamentsLink = Site + '/xml/games/tournaments.php'
	ActiveTournamentPrefix = Site + '/tournaments/'
	ArchiveGameForUserPrefix = Site + '/xml/games/history.php?act=userhistory&user='
	PlayMatchLink  = Site + '/php/builder_api.php'
	CurrenSession = None


class GameSession(object):

	def initSession(self):

		proxies = {
		  		'http': 'http://109.188.138.81:8081'
			  }
		logon = {
	    		'step' : '1',
	    		'login' : '1',
	     		'userresl' : '1366x768',
	    		'useragent' : 'Mozilla 5.0',
	    		'useragent' : 'Mozilla 5.0',
	    		'auth_name': GlobalData.LoginUser,
	    		'auth_pass': GlobalData.LoginPassword,
	    		'auth_pass1': '',
	    		'userdate' : '12',
	    		'usertime' :  '62609'
			}
		#self-register 
		self.session = requests.Session()
		GlobalData.CurrentSession = self.session
		
		p = GlobalData.CurrentSession.post(GlobalData.Site, data=logon)	
	
	def get(self, *args, **kwargs):
		kwargs['timeout'] = 15
		self.session.get(*args, **kwargs)
	
	def post(self, *args, **kwargs):
		kwargs['timeout'] = 15
		self.session.get(*args, **kwargs)
	

class BestSkillPriority(object):

	Stats = {    
    'Cd'  : {'Tck' : 10 ,  'Mrk' : 10 , 'Pas' : 6 , 'Drb' : 2  },
    'Ld'  : {'Tck' : 10 ,  'Mrk' : 8 , 'Pas' : 7 , 'Drb' : 7, 'Stm' : 7, 'Pos' : 5  },
    'Rd'  : {'Tck' : 10 ,  'Mrk' : 8 , 'Pas' : 7 , 'Drb' : 7, 'Stm' : 7, 'Pos' : 5  },
    'Cm'  : {'Tck' : 7 ,   'Pas' : 10 , 'Drb' : 7, 'Stm' : 7 , 'Pos' : 8, 'Shs' : 5  },
    'Rm'  : {'Tck' : 5 ,   'Pas' : 10 , 'Drb' : 10, 'Stm' : 8 , 'Pos' : 9, 'Shs' : 6  },
    'Lm'  : {'Tck' : 5 ,   'Pas' : 10 , 'Drb' : 10, 'Stm' : 8 , 'Pos' : 9, 'Shs' : 6  },
    'Cf'  : {'Tck' : 4 ,   'Drb' : 7, 'Stm' : 8 , 'Shs' : 9, 'Sha' : 10  },
    'Lf'  : {'Tck' : 4 ,   'Drb' : 7, 'Stm' : 8 , 'Shs' : 9, 'Sha' : 10  },
    'Rf'  : {'Tck' : 4 ,   'Drb' : 7, 'Stm' : 8 , 'Shs' : 9, 'Sha' : 10  }
    
    }

	def __init__(self):
		pass

	def ageContribution(self, player):
		return (40 - player.Age) * 0.5   

	def moraleContribution(self, player):
		return player.Morale * 5

	def talentContribution(self, player):
		return 0

	def readinessEffect(self, player):
		return 1		


class TalentAndReadinessPriority(object):

	Stats = {    
    'Cd'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Ld'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Rd'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Cm'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Rm'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Lm'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Cf'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Lf'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  },
    'Rf'  : {'Tck' : 0 ,  'Mrk' : 0,  'Pas' : 0 , 'Drb' : 0, 'Stm' : 0 , 'Pos' : 0, 'Shs' : 0, 'Sha' : 0  }
    
    }
	def __init__(self):
		pass

	def ageContribution(self, player):
		if player.Talent <= 4:
			return (40 - player.Age)/2
		return (40 - player.Age) * 2   

	def moraleContribution(self, player):
		return player.Morale * 3

	def talentContribution(self, player):
		if player.Talent <= 4:
			return 0

		return player.Talent * (40 - player.Age)

	def readinessEffect(self, player):
		return 1		


class RolesPriority(object):
	def captainScore(self, player):
		print(player.ID)
		return 10 if 'Gk' in player.Positions else 5
	
	def penaltyScore(self, player):
		if 'Gk' in player.Positions:
			return 1
		else :
			return player.Skills['Sha']  +  player.Skills['Shs'] * 0.5


	def freeKicksScore(self, player):
		if 'Gk' in player.Positions:
			return 1
		else :
			return player.Skills['Sha'] * 0.5 +  player.Skills['Shs'] 


	def leftCornersScore(self, player):
		if 'Gk' in player.Positions:
			return 1
		else :
			posBonus = 10 if 'Lm' in player.Positions else 0
			return player.Skills['Pas']  +  player.Skills['Sha'] * 0.5 + posBonus  

	def rightCornersScore(self, player):
		if 'Gk' in player.Positions:
			return 1
		else :
			posBonus = 10 if 'Rm' in player.Positions else 0
			return player.Skills['Pas']  +  player.Skills['Sha'] * 0.5 + posBonus  





	
