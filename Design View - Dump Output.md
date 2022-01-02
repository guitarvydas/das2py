![Dump Output](./design-Dump%20Output%20Bucket.svg)

The Dispatcher dumps output messages in four phases:
1. forEach output in the output bucket:
2. get the Receiver list associated with the output message, from the component's parent (a Container or nil)
3. forEach receiver in the Receiver list:
4. deliver the output message to the Receiver ; convert the output message to an appropriate input message (e.g. the Receiving Component plus the Receiving pin), then, enqueue it on the Receiver's input queue 