![Hello World](./design-Hello%20World.svg)

The Helloworld example consists of 5 entities:

1. Dispatcher
2. a helloworld component
3. a hello component 
4. a world component
5.  Startup

The components, 2, 3, and 4, are invoked by the Dispatcher.

Components cannot (must not) call each other - the Dispatcher is the only entity that can `call` components.

Components can send messages to other components.

The scoping rules for message-sending are:

- a Component can send messages to its parent
- a Component can send messages to its peers (via the router in the parent)
- messages between peers are routed by the Container (parent) of the components - i.e. Components cannot know where there messages are to be delivered, Components cannot know *if* their messages are delivered (the parent might decide to not-connect the output of a Component)
- all message-sending is asynchronous - the sender does not implicitly wait for a message to be delivered (if waiting is required, that must be explicitly drawn in the diagrams using the REQ/ACK protocol)
- all messages are sent in a deferred manner - the messages are distributed to their respective receivers only after the component has finished its reaction - all output messages are placed on an outgoing queue and meted out by the Dispatcher when it feels like it
- it is guaranteed that a message sent to two different receivers will arrive "at the same time" without interleaving with messages from other components.

Startup (5) is transitory and happens only once for a brief amount of time (the beginning of a run).

Startup (5) ensures that all components are instantiated and registered with the Dispatcher[^1].

[^1]: Startup is, probably, done recursively.

Messages can be sent during startup but are not delivered until the system has reached steady-state.

The system has 2 main states:
1. startup
2. steady-state - which is "normal operation".

