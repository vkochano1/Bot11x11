import os
import imp
from Config import *

class ModuleCache (object):

    def __init__(self, cacheDir, cfClassName):
        self.modules = {}
        self.costFunctions = {}
        
        for fname in os.listdir(cacheDir):
            mname, ext = os.path.splitext(fname)
            if ext != '.py':
                continue
            
            p = os.path.join(cacheDir, fname)
            m = ModuleCache.importFromURI(p)
            self.modules[mname] = m

        for name, mod in self.modules.iteritems():
            try:
                self.costFunctions [name] = mod.__dict__[cfClassName]
            except:
                print 'failed to load ' + name
                pass

    def getCostFunction(self, name):
        costFunction =   self.costFunctions.get(name)
        if costFunction == None:
            return None
        return costFunction
    
    @staticmethod
    def importFromURI(uri):
        mod = None      
        path, fname = os.path.split(uri)
        mname, ext = os.path.splitext(fname)

        if os.path.exists(os.path.join(path,mname)+'.py'):
            try:
                return imp.load_source(mname, os.path.join(path,mname)+'.py')
            except:
                print 'failed to load ' + mname
                pass
        return mod
