import ModuleCache

class SquadCostFunctionCache(ModuleCache.ModuleCache):
    def __init__(self):
        super(SquadCostFunctionCache, self).__init__('CostFunctions\Squad', 'SquadCostFunction')
        
class RolesCostFunctionCache(ModuleCache.ModuleCache):
    def __init__(self):
        super(RolesCostFunctionCache, self).__init__('CostFunctions\Roles', 'RolesCostFunction')

class RecoveryCostFunctionCache(ModuleCache.ModuleCache):
    def __init__(self):
        super(RecoveryCostFunctionCache, self).__init__('CostFunctions\Recovery', 'RecoveryCostFunction')

class GlobalCostFunctions(object):
    Squad = SquadCostFunctionCache()
    Roles = RolesCostFunctionCache()
    Recovery = RecoveryCostFunctionCache()
    


