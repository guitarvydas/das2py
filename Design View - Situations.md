![Situations](./design-Situations.svg)

Certain methods should only be used at certain times in the life of the system.

This diagram shows the lifecycle timing and validity of method:
1. during startup
2. during dispatching
3. during reaction.

This diagram shows, for example, that the Dispatcher can use the methods supplied by components:
- react (message)
- ready?
- busy?.

The diagram shows that the `react` method of components may use the `send` system method.