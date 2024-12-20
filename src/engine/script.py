class Script :

    parent:object

    invokeQueue = []

    def __init__(self, parent) :
        self.parent = parent

    def Start() :
        pass

    def Update() :
        pass

    def Invoke(method, time:float=0, args:list[any]=[]) :
        """
        Appelle method au bout de time secondes. Si time=0, method est exécutée à la prochaine frame
        args doit être dans le bon ordre
        """
        invokeQueue.append(((method,args), time))