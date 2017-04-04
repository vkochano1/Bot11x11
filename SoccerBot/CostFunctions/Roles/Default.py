class RolesCostFunction(object):
    def captainScore(self, player):
        return 10 if 'Gk' in player.Positions else 5
    
    def penaltyScore(self, player):
        if 'Gk' in player.Positions:
            return 1
        else :
            val = player.ExtraAbilities.get('Penalty') or 0
	    skillBonus = val * 2
            return player.Skills['Sha']  +  player.Skills['Shs'] * 0.5 + skillBonus


    def freeKicksScore(self, player):
        if 'Gk' in player.Positions:
            return 1
        else :
	    val = player.ExtraAbilities.get('FreeKicks') or 0
	    skillBonus = val * 3	
            return player.Skills['Sha'] +  player.Skills['Shs'] + player.Skills['Pas'] + skillBonus


    def leftCornersScore(self, player):
        if 'Gk' in player.Positions:
            return 1
        else :
            posBonus = 10 if 'Lm' in player.Positions else 0
	    val = player.ExtraAbilities.get('Corners') or 0
	    skillBonus = val * 2	
            return player.Skills['Pas']  +  player.Skills['Sha'] * 0.5 + posBonus + skillBonus  

    def rightCornersScore(self, player):
        if 'Gk' in player.Positions:
            return 1
        else :
            posBonus = 10 if 'Rm' in player.Positions else 0
	    val = player.ExtraAbilities.get('Corners') or 0
	    skillBonus = val * 2 
            return player.Skills['Pas']  +  player.Skills['Sha'] * 0.5 + posBonus + skillBonus  


