import CombinationWalker
import CostEvaluators
from Config import *
import CostFunctionCache 


class PlayerPositionScore(object):
    
    def __init__(self, player, detail):
        self.player = player
        self.detail = detail
          
    def positionScore(self, pos):
        score = 0
        table = None
        
        ageContribution = self.detail.ageContribution(self.player)
        moraleContribution = self.detail.moraleContribution(self.player)
        talentContribution = self.detail.talentContribution(self.player)
        readinessEffect = (float) (self.detail.readinessEffect(self.player))
    
        penalty = 1.0
        
        ## goalkeepers
        if self.player.Positions[0] == 'Gk' and pos == 'Gk':
            score = self.detail.goalKeeperScore(self.player)
        else:
            if pos not in self.player.Positions:
                penalty = 0.7
            
            table = self.detail.Stats[pos]
            
            for skl, val in self.player.Skills.iteritems():
                if skl == 'Skl':
                    continue
                coef = table.get(skl) or 1
                score = score + coef * val

        readinessPenaltyCoef = 1.0
        if self.player.Readiness <= 50:
            readinessPenaltyCoef  = 0.33
        
        readiness =  (self.player.Readiness  / 100.0) ** readinessEffect 

        tmp = (score + ageContribution + moraleContribution)  * (readiness) * penalty  +  talentContribution
        result = tmp * readinessPenaltyCoef 
        return result
        

class PlayerRoleScore(object):
    
    def __init__(self, players, detail):
        self.detail = detail
        self.players = players
        self.scoreFuncMap = { 
                'Captain' : detail.captainScore,
                'Penalty' : detail.penaltyScore,
                'FreeKicks' : detail.freeKicksScore,
                'LeftCorners' :detail.leftCornersScore,
                'RightCorners' : detail.rightCornersScore}


    def processNewScore(self, player, scoreID, allScores):
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

                   
class SquadSelectionTactic(object):
    def __init__(self):
        self.data = []
        self.mapping = {}
        
        for stage, name in GlobalData.UserCfg.PickSquadStrategy:
            cf = CostFunctionCache.GlobalCostFunctions.Squad.getCostFunction(name)
            self.mapping[name] = cf
            self.data.append( ( stage, name ) )
            
    class CallHelper(object):
        def __init__(self, cf):
                self.cf= cf

        def __call__(self, player, pos):
                return CostEvaluators.PlayerPositionScore(player,self.cf()).positionScore(pos)
            
            
    def getSelector(self,  formPositions, stage, players):
        for cfgStage, name in self.data:
            print stage, cfgStage, name
            if stage > cfgStage :
                return CombinationWalker.CombinationWalker(formPositions, players, SquadSelectionTactic.CallHelper(self.mapping[name]))
