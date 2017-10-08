
from collections import namedtuple
class ContraDataFunction(object):
    GameStrategy=namedtuple('GameStrategy', ['formation', 'strategy', 'tactic'] )
    
    Data = { 
                      # Confidence 1.1
                      GameStrategy(formation = '145', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '145', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '145', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '145', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '145', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '154', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '154', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '154', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '154', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '154', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '154', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '60' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '523', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '65' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '85' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '45' )
,
                      # Confidence 1.0
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '70' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '85' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '55' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '45' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '80' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '60' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '85' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 6.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '30' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '85' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '80' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '90' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '451', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '253', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '451', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '55' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '90' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '70' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '90' ) : GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '60' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '75' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '40' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '70' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '90' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '95' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '100' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '75' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '45' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '85' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '90' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '95' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 10.0
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '65' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '65' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 8.0
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 6.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '70' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 10.0
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '25' )
,
                      # Confidence 6.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '65' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '80' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '85' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '65' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '65' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '85' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '90' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '95' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 7.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '85' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '95' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '45' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '65' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '100' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '415', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '100' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '415', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '60' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '60' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '55' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '90' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '45' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 8.0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '85' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '90' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '95' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '65' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '80' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '85' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '45' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '70' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '70' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 9.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 8.0
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 8.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '55' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '70' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '95' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 6.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 5.75
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 6.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 6.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '65' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '85' ) : GameStrategy(formation = '451', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '95' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '45' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '80' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '85' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '45' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '65' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '80' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '85' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '65' )
,
                      # Confidence 6.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 9.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 9.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 7.0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '45' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '65' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 6.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '90' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '95' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 10.0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 4.0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '70' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '45' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 5.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '75' )
,
                      # Confidence 9.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '65' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '80' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '40' )
,
                      # Confidence 1.0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '45' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.0
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '25' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '45' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 12.5
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '532', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '70' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '40' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '90' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '80' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '85' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '514', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '253', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '514', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '514', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '514', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '514', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '514', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '514', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '75' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '541', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '35' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '75' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '45' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '85' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '75' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '5' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '60' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '85' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '80' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '90' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.0
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '65' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '65' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '80' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '75' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '95' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '451', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '100' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 2.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '55' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '60' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '70' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '75' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 4.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 3.0
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 3.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '60' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '60' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '65' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '90' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '95' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '100' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '15' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '20' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '25' ) : GameStrategy(formation = '433', strategy = 'Passing', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '35' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '40' ) : GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '75' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '85' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '95' ) : GameStrategy(formation = '433', strategy = 'Normal', tactic = '10' )
,
                      # Confidence 5.0
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '0' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '100' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '75' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '15' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '20' ) : GameStrategy(formation = '532', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '70' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '80' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '50' ) : GameStrategy(formation = '532', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '60' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '70' ) : GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '80' ) : GameStrategy(formation = '433', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '10' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '25' ) : GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '30' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '55' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '5' ) : GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '50' ) : GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '80' ) : GameStrategy(formation = '352', strategy = 'Passing', tactic = '80' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '0' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '10' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '35' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '15' ) : GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '20' ) : GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '25' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '40' ) : GameStrategy(formation = '343', strategy = 'Passing', tactic = '30' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '5' ) : GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '50' ) : GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '10' )
,
                      # Confidence 1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '55' ) : GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' ) }
    
    def getContraData( self, formation, strategy, tactic ):
        val = ContraDataFunction.Data.get( ContraDataFunction.GameStrategy(formation = formation, strategy = strategy, tactic = str(tactic) ) )
        return val
    


