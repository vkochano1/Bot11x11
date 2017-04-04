class SquadCostFunction(object):

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

    def goalKeeperScore(self, player):
	return player.Skills['Skl']

    def ageContribution(self, player):
        return (40 - player.Age) * 0.5   

    def moraleContribution(self, player):
        return player.Morale * 5

    def talentContribution(self, player):
        return 0

    def readinessEffect(self, player):
        return 1 
