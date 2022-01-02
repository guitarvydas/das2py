import mpos
import dispatcher
import samplehello

class World (mpos.Leaf):
    def __init__ (self, dispatcher, parent, debugID):
        super ().__init__ (dispatcher, parent, debugID)
        self.inputs = ["in"]

    def react (self, inputMessage):
        print ("world")
        return super ().react (inputMessage)

class HelloWorld (mpos.Container):
    def __init__ (self, dispatcher):
        super ().__init__ (dispatcher, None, "helloworld")
        obj1 = samplehello._hello (dispatcher, self, "hello")
        world = World (dispatcher, self, "world")
    
        sender = mpos.Sender (self, "start")
        rchild = mpos.Receiver (obj1, "start")
        receivers = [ rchild ]
        conn0 = mpos.Connector (sender, receivers)
    
        sender = mpos.Sender (obj1, "out")
        rworld = mpos.Receiver (world, "in")
        receivers = [ rworld ]
        conn1 = mpos.Connector (sender, receivers)

        self.children = { "hello": obj1, "world": world }
        self.connections = [ conn0, conn1 ]


disp = dispatcher.Dispatcher ()
hw = HelloWorld (disp)
hw.kickstart ()
disp.dispatch ()
