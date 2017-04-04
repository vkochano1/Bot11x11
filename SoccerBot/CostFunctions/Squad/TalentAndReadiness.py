class SquadCostFunction(object):

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

    def goalKeeperScore(self, player):
	return player.Talent * (40 - player.Age)

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
