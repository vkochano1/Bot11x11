import ModuleCache

class MainTacticCache(ModuleCache.ModuleCache):
    def __init__(self):
        super(MainTacticCache, self).__init__('Tactics\Main', 'ContraDataFunction')
        
class PassingStyleCache(ModuleCache.ModuleCache):
    def __init__(self):
        super(PassingStyleCache, self).__init__('Tactics\PassingStyle', 'PassingStyleFunction')

class TrainingTacicCache(ModuleCache.ModuleCache):
    def __init__(self):
        super(TrainingTacicCache, self).__init__('Tactics\Training', 'TrainingTacticFunction')
 
class GlobalTacticCache(object):
    Main = MainTacticCache()
    PassingStyle = PassingStyleCache()
    TrainingTactic = TrainingTacicCache()

