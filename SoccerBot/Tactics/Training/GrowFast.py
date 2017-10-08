defender = [100,100,50,70,70,70,30,30]
midfielder = [80, 30,80,90,70,100,70,70]
attacker = [70,10,90,70,70,70,100,100]


def TrainingTacticFunction():
        return {'Gk' : [100]
                ,'Cd' : defender
                ,'Ld' : defender
                ,'Rd' : defender
                ,'Cm': midfielder
                ,'Lm' : midfielder
                ,'Rm' : midfielder
                ,'Rf' : attacker
                , 'Lf' : attacker
                ,'Cf' : attacker}
