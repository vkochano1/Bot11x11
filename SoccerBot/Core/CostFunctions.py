import CombinationWalker
import CostEvaluators
from Config import *
import CostFunctionCache        
            
class SquadSelectionTactic(object):
    fB = CostFunctionCache.GlobalCostFunctions.Squad.getCostFunction('BestSkill')
    fT =  CostFunctionCache.GlobalCostFunctions.Squad.getCostFunction('TalentAndReadiness')
    def __init__(self):
        pass
    
    def getScoreBest(self, player, pos):        
        return CostEvaluators.PlayerPositionScore(player,SquadSelectionTactic.fB()).positionScore(pos)

    
    def getHealthy(self, player, pos):        
        return CostEvaluators.PlayerPositionScore(player,SquadSelectionTactic.fT()).positionScore(pos)

                
    def getSelector(self,  formPositions, stage, players):
        f = None 
        if stage <= GlobalData.BestSquadStage :
                f = self.getScoreBest
        else:
                f = self.getHealthy
        return CombinationWalker.CombinationWalker(formPositions, players, f)
            

 

