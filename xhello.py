#!/usr/bin/env python3
# xhello.py
# cell_7
import mpos
import dispatcher

class _xhello (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['_b']
        self.outputs=['out']
    def react (self, inputMessage):
        xprint ("hello")
        xself.send ("out", True)
        
        return super ().react (inputMessage)
