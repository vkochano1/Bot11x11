import itertools
import time
import logging

class CombinationWalker(object):
    """
        Finds the best combination of players for 
        provided schema and provided cost function
    """
    def __init__(self, schemaPositions, players, costFunc):
        self.logger = logging.getLogger(self.__class__.__name__)     
        self.prepareCosts(schemaPositions, players, costFunc)
	
    def prepareCosts(self, schemaPositions, players, costFunc):
        self.schemaPositions = []        
        self.playersByPosition = []
        self.costFunc = costFunc
        
        #filter players who can participate in next game
        allPlayers = [player for player in players if player.AllowedToPlay == True ]

        #field players
        self.keepers = [ player for player in allPlayers if player.Positions[0] == 'Gk' ]

        #goalkeepers
        self.players = [ player for player in allPlayers if player.Positions[0] != 'Gk' ]
        
        #position histogram
        tmp = {}
        for pos in schemaPositions:
            if pos != 'Gk':
                tmp[pos] = (tmp.get(pos) or 0) + 1

        for position, requiredNbrOfPlayers in tmp.iteritems():
            self.schemaPositions.append((position,requiredNbrOfPlayers))

        

        #populate cost
        for position, numPlayers in self.schemaPositions:
            posPlayers = []
            for player in self.players:
                if position in player.Positions:                             
                      score = self.costFunc(player, position)
                      posPlayers.append( (player, score) )

                      ## Don't need more than numPlayers * 2 players for each position
                      if len(posPlayers) > numPlayers * 2:
                          idx = 0
                          worstIdx = 0
                          worstScore = None
                          for p, s in posPlayers:
                              if worstScore == None or s < worstScore:
                                  worstScore = s
                                  worstIdx = idx
                              idx = idx + 1
                          del posPlayers[worstIdx]

            self.playersByPosition.append(posPlayers)

	forLog = {}
	for i, positionPlayers in enumerate(self.playersByPosition):
		position = self.schemaPositions[i][0]
		forLog[position]  = [ (player.ID, score) for ( player, score) in positionPlayers ] 

	self.logger.info('Evaluated players: %s ' % (str(forLog)))

    def lockPlayers(self, playersWithCalculatedScore, position, lockDict):
        aggScore = 0
        for player, score in playersWithCalculatedScore:
            lockDict [ player.ID ] = position
            aggScore = aggScore + score
        return aggScore

    def unlockPlayers(self, playersWithCalculatedScore, lockDict):
        for player, score in playersWithCalculatedScore:
            del lockDict [player.ID]
    

    def isPlayerLocked(self, player, lockDict):
        return lockDict.get(player.ID) != None
            
    def findBestCombination(self):        
       self.bestScore = 0
       self.bestCombination = None 
       self.logger.info('------------------------- STARTED ---------------------------')       
       start = time.time()

       #find the best keeper
       bestKeeperScore = 0
       bestKeeper = None
       for keeper in self.keepers:
            score = self.costFunc(keeper, 'Gk')
            if score > bestKeeperScore:
                bestKeeperScore = score
                bestKeeper = keeper

       usedIDs = {}
       self.findPlayerForPosition(0, usedIDs, 0)

       if self.bestCombination != None:
           self.bestCombination[ bestKeeper.ID] = 'Gk'
       
       end = time.time()
       
       self.logger.info('------------------------- STOPPED (%s sec) ----------------- > ' % str(end-start))
       
       return self.bestCombination
       
    def exitCondition(self, currentIdx, score, usedIDs):
        if currentIdx == len(self.schemaPositions):
            if score > self.bestScore:
                    self.bestScore = score
                    self.bestCombination = usedIDs.copy()
            return True
        return False    
        

    def borrowPlayersFromAnotherPosition(self, currentIdx, position, players, playersRequired, usedIDs):
        needPlayersNum = playersRequired - len(players) 
        
        scoreAgg = self.lockPlayers(players, position, usedIDs)
        
        scores = [] 
        
        for player in self.players:
            score = self.costFunc(player, position)
            
            if True == self.isPlayerLocked(player, usedIDs):
                continue
            
            scores.append((player, score))
            
        scores.sort(key=lambda tup: tup[1], reverse = True)
        bestN = scores[:needPlayersNum]
        
        scoreAgg = scoreAgg + self.lockPlayers(bestN, position, usedIDs)
 
        self.findPlayerForPosition(currentIdx + 1, usedIDs, scoreAgg)
    
        self.unlockPlayers(players, usedIDs)
        self.unlockPlayers(bestN, usedIDs)
    

    def  findPlayerForPosition(self, currentIdx, usedIDs, prevScore):

        if self.exitCondition(currentIdx, prevScore, usedIDs) == True:
            return
        
        players = self.playersByPosition[currentIdx]
        (pos, playersRequired) = self.schemaPositions[currentIdx]
    
        if len(players) < playersRequired:
            self.borrowPlayersFromAnotherPosition(currentIdx, pos, players, playersRequired, usedIDs)
            return

        for combination in itertools.combinations(players, playersRequired) :

            locked = False
            
            for player, score in combination:
                if True == self.isPlayerLocked(player, usedIDs):
                    locked  = True
                    break
            
            if locked == True:
                continue
            
            scoreAgg = self.lockPlayers(combination, pos, usedIDs)

            newScore = prevScore + scoreAgg
            
            self.findPlayerForPosition(currentIdx + 1, usedIDs, newScore)                            
            
            self.unlockPlayers(combination, usedIDs)

