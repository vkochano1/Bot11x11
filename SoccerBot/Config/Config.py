# -*- coding: utf-8 -*-
import requests
import pickle
import os

class GlobalData(object):

	LoginUser =  None
	LoginPassword = None
    
	UserID = None
	TournamentStartedCheckInterval = 30
	CheckIfOpponentIsAvailableInterval = 30
	TechnicalWorksDoneCheckInterval = 0.35
	
	#recovery
	WaitUntilNSecondsLeftToFullRecovery = 500	
	RecoveryStateCheckInterval = 60

	Site = 'http://www.11x11.ru/'
	Players = Site + '/players/'
	PlayerLookUpAnchor = u'Мастерство'
	PlayerInfoLookupAnchor = u'Gk'	
	TournamentsLink = Site + '/xml/games/tournaments.php'
	ActiveTournamentPrefix = Site + '/tournaments/'
	ArchiveGameForUserPrefix = Site + '/xml/games/history.php?act=userhistory&user='
	PlayMatchLink  = Site + '/php/builder_api.php'
	RecoveryDataSnapshot = Site + '/xml/players/recovery.php'
	HealRequest = Site + '/xml/players/recovery.php?act=select&type=players/recovery'
	Reports = Site + '/reports/'
	CurrenSession = None
	UserCfg  = None


	
class UserConfig(object):
        
        def save(self):
                savePath = os.path.join('UserData', self.UserName)
                pickle.dump( self, open( savePath, "wb" ) )               

        @staticmethod
        def loadConfig(userName):
                loadPath = os.path.join('UserData', userName)
                if os.path.exists(loadPath):
                        return pickle.load( open( loadPath, "rb" ) )
                return None

        def __init__(self, userName, ID, stage):
                self.UserName = userName
                self.ID = ID
                self.Stage = stage
	
