Certain methods can only be called by certain objects (*timing* of such calls is described in the Situations section).

![Access](./design-Access.svg)

This diagram is similar to the Situations diagram, except that the diagram does not show the time contraints on the method calls.

This view is very similar in intent to the access control privileges bestowed on threads by operating systems.

It should be possible to mark each method, in the access view, with access privileges and to check this automatically with suitably-configured type checkers.

A function's type signature does not consist only of it input and output types, but also of its access privileges and timing constraints[^1].

[^1]: Attempting to flatten all of these dimensions down into 1 dimension (especially 1 text dimension) will result in accidental complexity.  The actual number of design dimensions in a given solution depends on the problem-to-be-solved.  A "one size fits all" methodology will make the solution appear to be more complicated.