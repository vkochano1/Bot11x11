from Config import *
from Session import *
import TacticCache

class Training(object):
    TrainingSkillIdx  = ['Tck', 'Mrk', 'Drb', 'Rcv', 'Edu', 'Pas', 'Shp', 'Sha']
    
    def __init__(self):
        url= GlobalData.Site + '/xml/players/train.php'
        soup = GlobalData.CurrentSession.getContent(url )
        tbl = soup.find_all("table", attrs={'class' : 'maintable'})[-1]
        rows = tbl.find_all('tr')
        
        self.trainingData  = []
        #need to skipp first row &  2 footer rows
        for row in rows[1:-2]:
            tds = row.find_all('td')

            ###Extract playing positions
            positions = tds[0].text.strip('\n\r').split('/')

            ###Extract playerID
            playerIDAnchor = tds[1].find('a');
            playerID = playerIDAnchor.attrs['href'].split('/')[-1]

            ###Extract experience
            exp = int(tds[6].text.strip('\n\r'))

            ###Extract level & required exp to advance for each stat
            stats = {}
            if len (tds) <= 8:
                stats = [tds[7].text.strip('\n\r').split('(')]
            else:
                stats = [ td.text.strip('\n\r').split('(') for td in tds[7:]]

            ### normalize stats to array of pairs ( current level, exp to raise to the next level)
            stats = [ (int(skill[0]), int(skill[1].strip(' ()\n\r')) ) for skill in stats ]


            ### normalize current skill as sklI/max(sklN)

            maxLevelAcrossAll = max ( [ skill[0] for skill in stats] )
            
            normalizedLevels = [ 100 * skill[0]/ maxLevelAcrossAll for skill  in stats ]
            
            trainingRecord ={ 'PlayerID'  : playerID,
                         'Positions' : positions,
                         'Experience': exp,
                         'Stats'     : stats,
                         'NormalizedLevels' : normalizedLevels
                        }
            
            self.trainingData.append(trainingRecord)

    def processTrainingRecord(self, trainingRecord, trainingPolicy):
        posTrPolicy = trainingPolicy[trainingRecord['Positions'][0]]

        diffs = [pNormSkl - policyNormSkl for (pNormSkl, policyNormSkl) in zip(trainingRecord['NormalizedLevels'], posTrPolicy)]

        curMin = 999
        minIdx = -1
        for idx, v in enumerate(diffs):
            if v < curMin:
                minIdx = idx
                curMin = v
        sklInfo = trainingRecord['Stats'][minIdx]
        expDiff = trainingRecord['Experience'] - sklInfo[1]
        return (trainingRecord['PlayerID'], Training.TrainingSkillIdx[minIdx], expDiff, sklInfo[0])


    def processAll(self, trainingPolicy):
        incNum = 0
        for trainingRecord in self.trainingData:
            (playerID, Skill, expDiff, curLevel) = self.processTrainingRecord(trainingRecord,trainingPolicy)
            if expDiff >= 0:
                incNum = incNum + 1
                self.incStat(playerID, Skill, curLevel)
        return incNum
             
    def incStat(self, player, stat, level):
        url= GlobalData.Site + '/xml/players/train.php?act=raise&id=%s&ability=%s&level=%s'% (player,stat,level)
        soup = GlobalData.CurrentSession.getContent(url)
        
    def trainAll(self, policyName):       
	try:		
		trainingCF = TacticCache.GlobalTacticCache.TrainingTactic.getCostFunction(policyName)
		trainingPolicy = trainingCF()
                self.processAll(trainingPolicy)
	except Exception as ex:
                print(ex)
                pass
