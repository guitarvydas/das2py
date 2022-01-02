#!/usr/bin/env python3
import dispatcher
import samplehelloworld
disp = dispatcher.Dispatcher ()
top = samplehelloworld._helloworld (disp, None, '')
top.kickstart ()
disp.dispatch ()
