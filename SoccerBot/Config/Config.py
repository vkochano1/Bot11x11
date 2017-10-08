# -*- coding: utf-8 -*-
import requests
import os
import ModuleCache

class GlobalData(object):
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
	Level = None
	Money = None

	
class UserConfig(object):
    def __init__(self, userName):            
            self.UserName = userName
            self.TournamentStartedCheckInterval = 30
            self.CheckIfOpponentIsAvailableInterval = 30
            self.TechnicalWorksDoneCheckInterval = 0.1
            self.WaitUntilNSecondsLeftToFullRecovery = 500
            self.RecoveryStateCheckInterval = 60
            self.PassingStyle = "Default"
            self.GameTactic   = "Default"
            self.RolesAssignment= "Default"
            self.AnalyseNOpponentReports = 15
            self.HealPlayersTactic = [ ('Gk', 75, 96, 20), ('Cf', 75, 90, 20), ('Cd', 75, 85, 20), ('Cm', 75, 85, 20) ] 
            self.PickSquadStrategy = [ (16, 'TalentAndReadiness'), (0,'BestSkill') ]
            self.SkipNonBotTournaments = True
           
            loadPath = os.path.join(GlobalData.AppDir,'UserData', userName )

            print('Loading ' , loadPath)
            configModule = ModuleCache.ModuleCache.importFromURI(loadPath)
            
            if configModule.TournamentStartedCheckInterval:
                    self.TournamentStartedCheckInterval = configModule.TournamentStartedCheckInterval
	
            if configModule.CheckIfOpponentIsAvailableInterval:
                    self.CheckIfOpponentIsAvailableInterval = configModule.CheckIfOpponentIsAvailableInterval
	
            if configModule.AnalyseNOpponentReports:
                    self.AnalyseNOpponentReports = configModule.AnalyseNOpponentReports
	
            if configModule.TechnicalWorksDoneCheckInterval:
                    self.TechnicalWorksDoneCheckInterval = configModule.TechnicalWorksDoneCheckInterval

            if configModule.RecoveryStateCheckInterval:
                    self.RecoveryStateCheckInterval = configModule.RecoveryStateCheckInterval

            if configModule.SkipNonBotTournaments:
                    self.SkipNonBotTournaments = configModule.SkipNonBotTournaments
                    
            if configModule.WaitUntilNSecondsLeftToFullRecovery:
                    self.WaitUntilNSecondsLeftToFullRecovery = configModule.WaitUntilNSecondsLeftToFullRecovery

            if configModule.PassingStyle:
                    self.PassingStyle = configModule.PassingStyle

            if configModule.GameTactic:
                    self.GameTactic = configModule.GameTactic

            if configModule.RolesAssignment:
                    self.RolesAssignment = configModule.RolesAssignment

            if configModule.HealPlayersTactic:
                    self.HealPlayersTactic = configModule.HealPlayersTactic

            if configModule.PickSquadStrategy:
                    self.PickSquadStrategy = configModule.PickSquadStrategy


            self.TrainingTactic = None
            if configModule.TrainingTactic:
                    self.TrainingTactic = configModule.TrainingTactic
            
            print(self.TrainingTactic)
            self.UserID = configModule.UserID
            self.Password = configModule.Password



           
