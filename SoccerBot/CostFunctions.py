import CombinationWalker
import CostEvaluators
            
            
class SquadSelectionTactic(object):

    def __init__(self):
        pass
    
    def getScoreBest(self, player, pos):
        return CostEvaluators.PlayerPositionScore(player, BestSkillPriority()).positionScore(pos)
    
    def getHealthy(self, player, pos):
        return CostEvaluators.PlayerPositionScore(player,TalentAndReadinessPriority()).positionScore(pos)
                

    def getSelector(self,  formPositions, stage, players):
        print ('stage ' + str(stage))    
        if stage <= 16 :
                return CombinationWalker.CombinationWalker(formPositions, players, self.getScoreBest)
        else:
                return CombinationWalker.CombinationWalker(formPositions, players, self.getHealthy)

            
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
        return 1.5        


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

