#!/usr/bin/env python3
# helloworld.py
import mpos
import dispatcher
import sampleworld
import samplehello

class _helloworld (mpos.Container):
    
    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['p_']
        self.outputs=[]

        child0 = sampleworld._world (dispatcher, self, 'world')
        child1 = samplehello._hello (dispatcher, self, 'hello')
        conn0 = mpos.Connector ([mpos.Sender ('', 'p_')], [mpos.Receiver ('hello', 'p_')])
        conn1 = mpos.Connector ([mpos.Sender ('hello', 'out')], [mpos.Receiver ('world', 'in')])
        self.connections = [ conn0, conn1 ]
        self.children = {'world':child0, 'hello':child1}
