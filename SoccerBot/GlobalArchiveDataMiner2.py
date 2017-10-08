import os
import sys

subirs = ['CostFunctions', 'Tactics', 'Config', 'Core', 'Utils']

for d in subirs:
    sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), d ))

from Config import *
GlobalData.AppDir = os.path.abspath(os.path.dirname(__file__))


import GameArchive
from Config import *
import Session
import logging
import re
import pickle
import CostEvaluators
import numpy as np




def findBest(dataFrame, winnerColumns, looserColumns):
    from collections import namedtuple
    GS=namedtuple('GS', ['form', 'str', 'tact'])
    winnerIdx = dataFrame.groupby(winnerColumns).count()
    looserIdx = dataFrame.groupby(looserColumns).count()
    idx = {}
    for wrecord in winnerIdx.index.get_values():
        
        wc = int(winnerIdx.loc[wrecord].at1)
        
        lc = None      
        try:
            lc = int(looserIdx.loc[wrecord].at1)
        except:
            lc = 1
            wc = wc + 0.1
            pass
            
        #if wc < 3:
        #    continue
        ratio = wc / lc 
        key = GS(wrecord[0], wrecord[1], wrecord[2])
        v = idx.get(key)
                  
        if v == None or v[1] < ratio:
                  idx[key] = (wrecord[3], ratio)
                  continue

        if v[1]== ratio and wrecord[3]=='Mixed':
            idx[key] = (wrecord[3], ratio)
            print 'CAAAAAAASSSS'

    elements = []
    for k, v in idx.iteritems():
        element = """ # Confidence=%s
                      GameStrategy(formation = '%s', strategy = '%s', tactic = '%s' ) : '%s'"""
        formatted = element % (  v[1], k[0], k[1], k[2], v[0])
        elements.append(formatted)

    dt = ',\n'.join(elements)
    text = """
from collections import namedtuple
class PassingStyleFunction(object):
    GameStrategy=namedtuple('GameStrategy', ['formation', 'strategy', 'tactic'] )
    
    Data = { %s }
    
    def getPassingStyle( self, formation, strategy, tactic ):
        val = PassingStyleFunction.Data.get( PassingStyleFunction.GameStrategy(formation = formation, strategy = strategy, tactic = str(tactic) ) )
        if val == None:
            val = 'Mixed'
        return val
"""
    text = text % dt
    f = open('./Tactics/PassingStyle/Default.py', 'w')
    f.write(text)
    f.close()
def genCSV():
    import pickle
    import pandas as pd


    with open('finalX1.txt', 'r') as f:
        with open('pd2.csv','w') as o:
            enrichedOld = pickle.load( f )
            print('loaded')
            o.write('strategy,tactic,form,pstyle,lstrategy,ltactic,lform,lpstyle,gk,at1,at2,mid\n')
            for k, match in  enrichedOld.iteritems():
                o.write( str(match[0][0][0]) + ',' + str(int(match[0][0][1]/5) * 5) + ',' + str(match[0][0][2]) + ',' + str(match[0][0][3])
                         + ',' + str(match[1][0][0])  + ',' + str(int (match[1][0][1]/5) * 5) + ',' + str(match[1][0][2]) + ',' + str(match[1][0][3])
                         + ',' + str(match[2][0])  + ',' + str(match[2][1]) + ',' + str(match[2][2]) +',' + str(match[2][3])
                         + '\n')
            print('written')
            
        
        v= pd.read_csv('pd2.csv' , dtype = np.str)
    #v['lstrategy'] = 'Passing'
    #v['lform'] = '442'
    #v['ltactic']  = 5
    

    print(len(v))
    #v= v[ v['lform'] == 442]
    #v = v[v['lstrategy'] == 'LongShots'] 
    #v = v[ v['ltactic'] == 10]
 
    #v.sort(['lform', 'lstrategy','ltactic'])
    #v = v.set_index(['lform', 'lstrategy', 'ltactic'])
        


    #ser = v.sort(['strategy', 'lstrategy', 'form', 'lform']).groupby(['lform', 'lstrategy', 'ltactic' , 'form', 'strategy', 'tactic']).count()
        
    #v.sort_index(ascending=True, inplace=True)
        #v.sortlevel([0,1,2])
    z = v#v.loc[[442,'Dribbling', 5], : ]
    zx = z.groupby([ 'lform', 'lstrategy', 'ltactic','form', 'strategy', 'tactic']).count()

    z2 = z.groupby([ 'lform', 'lstrategy', 'ltactic']).count()

    z3 = z.groupby([ 'form', 'strategy', 'tactic', 'pstyle']).count()

    findBest(z, [ 'form', 'strategy', 'tactic', 'pstyle'], [ 'lform', 'lstrategy', 'ltactic', 'lpstyle'])

    

    from collections import namedtuple
    GameStrategy=namedtuple('GameStrategy', ['formation', 'strategy', 'tactic'] )

    d = {}
    u = {}
    text = """
from collections import namedtuple
class ContraDataFunction(object):
    GameStrategy=namedtuple('GameStrategy', ['formation', 'strategy', 'tactic'] )
    
    Data = { %s }
    
    def getContraData( self, formation, strategy, tactic ):
        val = ContraDataFunction.Data.get( ContraDataFunction.GameStrategy(formation = formation, strategy = strategy, tactic = str(tactic) ) )
        return val
    


"""
    sf = open('./Tactics/Main/Default.py', 'w')
    dd = []
    for r in z2.index.get_values():
        sub = zx.loc[r]
        m = 0.0
        bs = None
        for s in sub.index.get_values():

            c1 = sub.loc[s].pstyle
            c1 = float(c1)
            c2 = 1.0
            i = ( s[0], s[1], s[2], r[0], r[1], r[2] )
            
            try:
                fr = zx.loc[s[0], s[1], s[2] ]       
                kf = fr.loc[r[0], r[1], r[2]]
            
                c2 = float(kf.pstyle)
            except Exception as ex:
                c1 = c1 + 0.1
                #continue
                pass
 
            if s[0].endswith('4') or s[0].endswith('5'):
                #print (s)
                continue
            #if c1 < 3:
            #    continue
            if c1 / c2 > m:
                m = c1/c2
                bs = s
            elif c1/c2 == m and s[0] in ['442', '352']:
                
                bs = s

        if bs == None: 
            continue
        element = """
                      # Confidence %s
                      GameStrategy(formation = '%s', strategy = '%s', tactic = '%s' ) : GameStrategy(formation = '%s', strategy = '%s', tactic = '%s' )"""
        formatted = element % ( str(m), r[0], r[1], r[2], bs[0], bs[1], bs[2])
        
        u[bs[0]]=True
        #d[looser] =  winner
        dd.append(formatted)
    #ser.loc[['']]
        #v.to_csv('done.csv')
    #print (d[GameStrategy(formation = '442', strategy= 'Normal'  , tactic = '15' )])

    cont = '\n,'.join(dd)
    sf.write(text % cont)
    sf.close()
    print(u)

    
genCSV()








