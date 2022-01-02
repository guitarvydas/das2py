#!/usr/bin/env python3
# xworld.py
# cell_11
import mpos
import dispatcher

class _xworld (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['in']
        self.outputs=[]
    def react (self, inputMessage):
        xprint ("world")
        
        return super ().react (inputMessage)
