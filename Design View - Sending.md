![Sending](./design-Sending%20Deferred.svg)

A Component may call `send()` when its `react` method has been invoked.

A Component may call `send()` any number of times during a reaction.

A Component may choose not to call `send()` at all during a reaction.

Output messages are created by a call to `send()`.

Output messages are directed at specific output pins.  A Component may choose arbitrary output pins.

For example, a Component may send output to the `out` pin on success or send output to the `error` pin on failure.  Note that exceptions are not exceptional - exceptions are simply output messages.

For example, JavaScript's `readFileSync()` method can produce one of four different outputs[^1].  In Reactive Component Based components, each output can be sent to a different output pin, and, ultimately, each case can be handled differently.

[^1]: good, bad filename/file does not exist, timeout, user abort.