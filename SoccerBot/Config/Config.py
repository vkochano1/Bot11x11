# -*- coding: utf-8 -*-
import requests
import pickle
import os

class GlobalData(object):
	LoginUser =  None
	LoginPassword = None
	AppDir = None
	
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
	
	RequestTimeout = 15
	CurrenSession = None
	UserCfg  = None


	
class UserConfig(object):
    def save(self):
            savePath = os.path.join(GlobalData.AppDir,'UserData', self.UserName)
            pickle.dump( self, open( savePath, "wb" ) )               

    @staticmethod
    def loadConfig(userName):
            loadPath = os.path.join(GlobalData.AppDir,'UserData', userName)
            if os.path.exists(loadPath):
                    return pickle.load( open( loadPath, "rb" ) )
            return None

    def __init__(self, userName, ID):
            self.UserName = userName
            self.UserID = ID
            self.TournamentStartedCheckInterval = 30
            self.CheckIfOpponentIsAvailableInterval = 30
            self.TechnicalWorksDoneCheckInterval = 0.35
            self.TournamentStartedCheckInterval = 30
            self.CheckIfOpponentIsAvailableInterval = 30
            self.TechnicalWorksDoneCheckInterval = 0.35
            self.WaitUntilNSecondsLeftToFullRecovery = 500
            self.RecoveryStateCheckInterval = 30
            self.PassingStyle = "Default"
            self.GameTactic   = "Default"
            self.RolesAssignment="Default"
            self.AnalyseNOpponentReports = 15
            self.HealPlayersTactic = [ ('Gk', 75, 96, 20), ('Cf', 75, 90, 20), ('Cd', 75, 85, 20), ('Cm', 75, 85, 20) ] 
            self.PickSquadStrategy = [ (16, 'TalentAndReadiness'), (0,'BestSkill') ]
            self.SkipNonBotTournaments = True
	
