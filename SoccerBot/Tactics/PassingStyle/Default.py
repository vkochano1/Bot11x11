
from collections import namedtuple
class PassingStyleFunction(object):
    GameStrategy=namedtuple('GameStrategy', ['formation', 'strategy', 'tactic'] )
    
    Data = {  # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '35' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '40' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '35' ) : 'Mixed',
 # Confidence=7.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '95' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '70' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '35' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '35' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '35' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '20' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '25' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '75' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '0' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '55' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '75' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '65' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '90' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '55' ) : 'Long',
 # Confidence=3.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '10' ) : 'Short',
 # Confidence=3
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '70' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '20' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '0' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '145', strategy = 'Dribbling', tactic = '5' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '10' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '10' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '5' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '60' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '70' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '25' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '95' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '0' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '10' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '45' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '25' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '85' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '20' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '25' ) : 'Mixed',
 # Confidence=5.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '100' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '10' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '60' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '5' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '60' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '30' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '20' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'LongShots', tactic = '50' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '10' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '50' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '5' ) : 'Long',
 # Confidence=5
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '40' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '100' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '30' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '95' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '30' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '85' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '35' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '45' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '20' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '0' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '60' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '25' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '15' ) : 'Mixed',
 # Confidence=4
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '30' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '40' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '10' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '40' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '10' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '15' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '75' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '30' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '45' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '15' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '30' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '70' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '30' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '40' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '75' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '0' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '60' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '25' ) : 'Long',
 # Confidence=7
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '95' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '0' ) : 'Short',
 # Confidence=3
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '65' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '85' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '40' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '40' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '45' ) : 'Short',
 # Confidence=2.1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '20' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '15' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '35' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '60' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '70' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '60' ) : 'Short',
 # Confidence=3.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '65' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '55' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '5' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '70' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '15' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '65' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '45' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '5' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '40' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '15' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '10' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '80' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '50' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '50' ) : 'Short',
 # Confidence=2.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '55' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '5' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '20' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '80' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '60' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '55' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '75' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '70' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '45' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '50' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '10' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '55' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '75' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '85' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '85' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '65' ) : 'Short',
 # Confidence=2.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '75' ) : 'Short',
 # Confidence=7
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '80' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '45' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '30' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '415', strategy = 'Passing', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '85' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '10' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '15' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '15' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '85' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '20' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '95' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '75' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '50' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '25' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '35' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '30' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '90' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '5' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '85' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '35' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '55' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '80' ) : 'Short',
 # Confidence=2.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '75' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '60' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '95' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '10' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '100' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '85' ) : 'Mixed',
 # Confidence=4
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '35' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '70' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '95' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '65' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '10' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '55' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '100' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '60' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '5' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '15' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '5' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '75' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '60' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '70' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '75' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '25' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '80' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'LongShots', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '70' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '75' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '90' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '50' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '55' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '30' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '20' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'Passing', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '40' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '90' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '65' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '5' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '50' ) : 'Mixed',
 # Confidence=4.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '45' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '80' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '80' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '0' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '5' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '50' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '35' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '10' ) : 'Short',
 # Confidence=5
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '60' ) : 'Long',
 # Confidence=3.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '100' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '20' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '514', strategy = 'LongShots', tactic = '20' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '85' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '40' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '55' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '35' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '85' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '90' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '95' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '0' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '30' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '55' ) : 'Long',
 # Confidence=5
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '75' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '10' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '75' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '20' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '40' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '45' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '85' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '55' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '30' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '15' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '95' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '65' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '55' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '50' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '10' ) : 'Long',
 # Confidence=3.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'LongShots', tactic = '5' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '60' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '60' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '20' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '65' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '45' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '85' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '30' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '100' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '5' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '80' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '20' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '95' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '0' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '40' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=7
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '45' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '15' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '20' ) : 'Short',
 # Confidence=12.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '90' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '15' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '100' ) : 'Mixed',
 # Confidence=5.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '85' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '90' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '70' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '25' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '75' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '10' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '40' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'Dribbling', tactic = '50' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '45' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '25' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '20' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '85' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '15' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '70' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '90' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '25' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '20' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '85' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '60' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '25' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '35' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '235', strategy = 'Normal', tactic = '35' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '50' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '15' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '10' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '70' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '100' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '80' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '50' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '20' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '60' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '35' ) : 'Mixed',
 # Confidence=4.1
                      GameStrategy(formation = '415', strategy = 'LongShots', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '0' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '80' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '40' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '20' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '80' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '10' ) : 'Short',
 # Confidence=4.1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '85' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '35' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '5' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '100' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '45' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '0' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '70' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '40' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '75' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '30' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '60' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '514', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '70' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '25' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '70' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '60' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '55' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '45' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '45' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '80' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '35' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '45' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '100' ) : 'Long',
 # Confidence=3.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '60' ) : 'Short',
 # Confidence=2.1
                      GameStrategy(formation = '235', strategy = 'Normal', tactic = '0' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '55' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '20' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '50' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '70' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '75' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '50' ) : 'Short',
 # Confidence=5.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '60' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '15' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '100' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '25' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '50' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '90' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '85' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '85' ) : 'Mixed',
 # Confidence=9
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '55' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '15' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '55' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '25' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '100' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '65' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '25' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '20' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '154', strategy = 'LongShots', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '35' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '80' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '10' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '80' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '55' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '80' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '20' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '65' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '25' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '0' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '35' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '90' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '25' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '80' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '65' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '10' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '5' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '60' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '25' ) : 'Short',
 # Confidence=3
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '90' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '80' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '85' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '55' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '55' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '40' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '80' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '50' ) : 'Short',
 # Confidence=4.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '20' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '100' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '90' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '10' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '20' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '70' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '100' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '45' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '50' ) : 'Mixed',
 # Confidence=4
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '60' ) : 'Mixed',
 # Confidence=4.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '10' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '20' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '95' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '80' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '35' ) : 'Mixed',
 # Confidence=6
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '50' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '45' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '80' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '55' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '85' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '20' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '95' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '30' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '45' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '0' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '75' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '25' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '25' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '5' ) : 'Short',
 # Confidence=3.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '55' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '100' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '40' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '40' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '0' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '25' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '10' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '75' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '25' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '10' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '10' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '90' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '75' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '15' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '541', strategy = 'Passing', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '75' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '15' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '80' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '95' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '90' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '85' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '25' ) : 'Short',
 # Confidence=3
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '65' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '10' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '95' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '514', strategy = 'LongShots', tactic = '50' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '20' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '50' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=4.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '30' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '235', strategy = 'Passing', tactic = '10' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '40' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '70' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '80' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '90' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '50' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '45' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '60' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '45' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '65' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '15' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '80' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '15' ) : 'Mixed',
 # Confidence=4
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '35' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '10' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '45' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '60' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '145', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '35' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '35' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '25' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '45' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '90' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '35' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '40' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '95' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '45' ) : 'Short',
 # Confidence=2.1
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '35' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '20' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '100' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '25' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '25' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '45' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '20' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '0' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '100' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '50' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '65' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '20' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '100' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '100' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '10' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '541', strategy = 'Normal', tactic = '10' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '25' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '50' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '10' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '25' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '85' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '50' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '20' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '50' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '75' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '70' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '15' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '15' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '20' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '5' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '100' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '45' ) : 'Mixed',
 # Confidence=4
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '20' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'LongShots', tactic = '5' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '30' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Passing', tactic = '80' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '20' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '10' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Passing', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '35' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '433', strategy = 'Dribbling', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '523', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '95' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '70' ) : 'Long',
 # Confidence=3.1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '60' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '15' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '70' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '75' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '85' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '30' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '244', strategy = 'Normal', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'LongShots', tactic = '0' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '55' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '30' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '50' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '65' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '85' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '532', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=3.1
                      GameStrategy(formation = '451', strategy = 'Dribbling', tactic = '0' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '80' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '95' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '65' ) : 'Mixed',
 # Confidence=6
                      GameStrategy(formation = '532', strategy = 'Passing', tactic = '25' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '70' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '10' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '10' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '30' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '415', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '75' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '15' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '45' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '90' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '55' ) : 'Long',
 # Confidence=4
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '60' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '75' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '60' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '65' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '100' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '55' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '90' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '253', strategy = 'Dribbling', tactic = '15' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '10' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '5' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '523', strategy = 'Passing', tactic = '40' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '75' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '35' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Passing', tactic = '55' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '100' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '442', strategy = 'LongShots', tactic = '85' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '85' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '60' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'LongShots', tactic = '30' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '85' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '532', strategy = 'Dribbling', tactic = '80' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '20' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '15' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '10' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '352', strategy = 'Dribbling', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '30' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '334', strategy = 'Dribbling', tactic = '25' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '40' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '235', strategy = 'Dribbling', tactic = '20' ) : 'Long',
 # Confidence=3.1
                      GameStrategy(formation = '424', strategy = 'Dribbling', tactic = '75' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '5' ) : 'Long',
 # Confidence=3
                      GameStrategy(formation = '334', strategy = 'Normal', tactic = '25' ) : 'Long',
 # Confidence=3.1
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '80' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Normal', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '45' ) : 'Mixed',
 # Confidence=3
                      GameStrategy(formation = '442', strategy = 'Dribbling', tactic = '70' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'LongShots', tactic = '20' ) : 'Short',
 # Confidence=1.1
                      GameStrategy(formation = '415', strategy = 'Passing', tactic = '100' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '325', strategy = 'Dribbling', tactic = '0' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '50' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '95' ) : 'Mixed',
 # Confidence=2.1
                      GameStrategy(formation = '343', strategy = 'Passing', tactic = '100' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'Passing', tactic = '95' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '50' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '30' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '65' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '25' ) : 'Long',
 # Confidence=2.1
                      GameStrategy(formation = '451', strategy = 'LongShots', tactic = '60' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '40' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '541', strategy = 'Dribbling', tactic = '5' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '5' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '50' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '325', strategy = 'Passing', tactic = '15' ) : 'Long',
 # Confidence=5
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '55' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '5' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '80' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'LongShots', tactic = '10' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '325', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '35' ) : 'Short',
 # Confidence=1
                      GameStrategy(formation = '532', strategy = 'Normal', tactic = '5' ) : 'Mixed',
 # Confidence=4
                      GameStrategy(formation = '352', strategy = 'LongShots', tactic = '55' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'LongShots', tactic = '90' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '451', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '433', strategy = 'LongShots', tactic = '95' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '334', strategy = 'Passing', tactic = '20' ) : 'Short',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Dribbling', tactic = '60' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '244', strategy = 'Dribbling', tactic = '30' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '352', strategy = 'Normal', tactic = '0' ) : 'Mixed',
 # Confidence=0
                      GameStrategy(formation = '235', strategy = 'LongShots', tactic = '25' ) : 'Long',
 # Confidence=2
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '5' ) : 'Short',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Passing', tactic = '95' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '433', strategy = 'Normal', tactic = '80' ) : 'Mixed',
 # Confidence=1.1
                      GameStrategy(formation = '523', strategy = 'Dribbling', tactic = '15' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '60' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '253', strategy = 'Normal', tactic = '20' ) : 'Mixed',
 # Confidence=2
                      GameStrategy(formation = '244', strategy = 'Passing', tactic = '15' ) : 'Long',
 # Confidence=1.1
                      GameStrategy(formation = '424', strategy = 'Passing', tactic = '35' ) : 'Long',
 # Confidence=1
                      GameStrategy(formation = '541', strategy = 'LongShots', tactic = '15' ) : 'Long',
 # Confidence=0
                      GameStrategy(formation = '442', strategy = 'Normal', tactic = '30' ) : 'Mixed',
 # Confidence=1
                      GameStrategy(formation = '343', strategy = 'Normal', tactic = '50' ) : 'Short' }
    
    def getPassingStyle( self, formation, strategy, tactic ):
        val = PassingStyleFunction.Data.get( PassingStyleFunction.GameStrategy(formation = formation, strategy = strategy, tactic = str(tactic) ) )
        if val == None:
            val = 'Mixed'
        return val
