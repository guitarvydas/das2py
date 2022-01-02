![Invoke Component](./design-Invoke%20Component.svg)

The Dispatcher invokes a Component by calling the Component's `react` method.

A list of output messages is returned by the `react` method.

The Dispatcher queues these output messages in its output bucket.

See the "Dump Output" section for information about how the output bucket is emptied and each output message is delivered to corresponding Receivers.

