import os
import imp


class ModuleCache (object):

    def __init__(self, cacheDir, cfClassName):
        self.modules = {}
        self.costFunctions = {}
        print 'Listing directory' + cacheDir 
        for fname in os.listdir(cacheDir):
            mname, ext = os.path.splitext(fname)
            if ext != '.py':
                continue
            print 'Processing ' + fname
            p = os.path.join(cacheDir, fname)
            m = self.importFromURI(p)
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
    
    def importFromURI(self, uri):
        mod = None
        uri = os.path.normpath(os.path.join(os.path.dirname(__file__), uri))        
        path, fname = os.path.split(uri)
        mname, ext = os.path.splitext(fname)

        if os.path.exists(os.path.join(path,mname)+'.py'):
            try:
                return imp.load_source(mname, os.path.join(path,mname)+'.py')
            except:
                print 'failed to load ' + mname
                pass
        return mod
