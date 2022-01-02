![Connector](./design-Connector.svg)

A `sender` is
- component
- pin[^1][^2].

[^1]: A pin is a tag, usually a string.
[^2]: The nomenclature of *pins* comes from the pins on electronic ICs (integrated circuits).  In electronics, IC pins are usually labelled with small-integer indices, starting at 1.  For example, a 14-pin IC, would have pins labelled 1, 2, ... 14.  In Software, we are not limited to using small integers and can use strings as pin names.

A `receiver` is
- component
- pin.

Senders and Receivers look the same.

The `component` and `pin` of the Sender is different from the `component` and `pin` of the Receiver.

A Connector contains
- one Sender
- a list of Receivers

In other words, a message sent from the output of a component can be received by many different components on various pins.