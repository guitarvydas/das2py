![Classes](./design-Class%20inheritance.svg)

The main classes in `helloworld` are:
1. Component
	Leaf Component
	Container Component
1. Dispatcher

All Components have
- an input queue
- a parent (always a Container)
- an output queue (for deferred Send()s)

Container components also have:
- children
- connections.

Components are arranged in a hierarchy, like an ORG Chart.

A Leaf component is the bottom node, the worker-bee.  In traditional programming a Leaf is *code*.

A Container contains other components - Leaves or more Containers.

Children are referred to by-name and type[^1].

[^1]: analogy: children are like typed local variables in traditional programming languages.

A Container, also, contains a routing table called *connections*.  This routing table can refer only to children components and to the container itself.  When a child sends a message, the Container decides which other child the message will be delivered to[^2].

[^2] Messages can be routed to the Container itself, and, to the child itself (a feedback loop.  Feedback is different from recursion in traditional programming languages - the message is deferred and not delivered immediately as would happen with recursion.

A Container can send messages to its output by routing messages from children to its own output.  

In this case - a Container sending a message - the standard routing protocol is used.  The message is routed by the parent of the Container[^3].

[^3]: The parent of a Container does not care if the child is a Leaf or a Container.  Children are `black boxes` as far as the parent is concerned.

A Container can receive messages.  Received messages are routed to children of the container[^4].  The Dispatcher invokes the children when it feels like it (e.g. whenever it is a component's turn).

[^4]: or, simply dropped

The Dispatcher registers all components and invokes them in "random" order[^5].

[^5]: For example, a Dispatcher might keep *all* components on a flat list, or, it might keep the components in some sort of ORG Chart hierarchy.  The implementation of the Dispatcher is unspecified.

Components are **concurrent**[^6].  No implicit synchronization is provided by the system. If synchronization is required, it must be explicitly designed-in by the Software Architect.

[^6]: Concurrency only means that components cannot rely on implicit synchronization when sending messages.  Concurrency is a prerequisite for parallelism, but parallelism is not impliclty supplied by the system.  The implementation is unspecified.  The Dispatcher is free to dispatch components serially or in parallel.  Tuning the Dispatcher (e.g. by adding parallelism and other optimizatins) is the domain of Production Engineers and does not affect the Architecture of the system.  The only specified requirement is that components are designed to be inherently concurrent.

Components are invoked by calling their `react` methods with a single message as the parameter (self, this, etc. are implicitly supplied).

A component reacts to one message at a time and completes processing of that message before proceeding to process another message.

The Dispatcher may deliver messages after each input message has been processed.