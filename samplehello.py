import mpos
import dispatcher

class _hello (mpos.Leaf):
    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs = ['p_']
        self.outputs = ['out']

    def react (self, inputMessage):
        print ("hello")
        self.send ("out", True)
        return super ().react (inputMessage)

