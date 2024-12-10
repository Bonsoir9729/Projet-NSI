class Variable: 

    def __init__(self, name:str) -> None:
        self.name = name
        self.value = None

    def __str__(self) :
        return self.value
    
    def set(self, value) :
        self.value = value

class Context :

    def __init__(self, *args) -> None:
        self.memory = {arg.name : arg.value for arg in args}

    def get(self, name) :
        try :
            return self.memory[name]
        except KeyError :
            raise Exception('Variable ' + name + ' does not exist in the given context')
        
    def set(self,name,value): 
        self.memory[name] = value

    def Resolve_Variables(self, *args) :
        return [self.get(arg.name) if isinstance(arg,Variable) else arg for arg in args]

class Block :

    def hasReturn(self) :
        if not self.next :
            return False
        return self.next.hasReturn()

class ReturnBlock(Block) :

    def __init__(self, func, *args) -> None :
        self.func = func
        self.args = args

    def __call__(self,context=None):
        return self.func(*context.Resolve_Variables(*self.args))
    
    def hasReturn(self) :
        return True

class DefBlock(Block) :

    def __init__(self, next, *args) -> None:
        self.next = next
        self.context = Context(*args)
    
    def __call__(self, *args):
        vars = [key for key in self.context.memory.keys()]
        for i in range(len(args)) :
            self.context.set(vars[i],args[i])
        return self.next(context=self.context)
    
class IfBlock(Block) :
    def __init__(self, inner, next, func, *args) -> None:
        self.inner = inner
        self.next = next
        self.func = func
        self.args = args

    def __call__(self, context):
        if self.func(*context.Resolve_Variables(*self.args)) :
            if self.inner.hasReturn() :
                return self.inner(context)
            self.inner(context)
        return self.next(context)
    
    def hasReturn(self) :
        return self.next.hasReturn() or self.inner.hasReturn()

class LoopBlock(Block) :
    def __init__(self, inner, next, n) -> None:
        self.inner = inner
        self.next = next
        self.n = n

    def __call__(self,context):
        for i in range(self.n) :
            self.inner(context)
        return self.next(context)
        

def main() :
    globalContext = Context()
    #Definition du multiplexer en blocks
    returnBlock2 = ReturnBlock(lambda x : x, Variable('B'))
    returnBlock1 = ReturnBlock(lambda x : x, Variable('A'))
    ifBlock1 = IfBlock(returnBlock1, returnBlock2, lambda x : x, Variable('S'))
    defBlock = DefBlock(ifBlock1, Variable('A'), Variable('B'), Variable('S'))
    #defBlock(1234, 5678, True) -> 1234
    #defBlock(1234, 5678, False) -> 5678

if __name__ == '__main__' :
    main()