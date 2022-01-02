convert diagram `helloworld.drawio` into a python program
then, run the python program

details:
- use draw.io (diagrams.net) to edit helloworld.drawio
- use run.bash to compile and execute the diagram
- (run.bash regenerates out.json every time, this might not be necessary during development)

Documentation
- see "Design View*.md" ...
- in examplar, all component id's are strings
- future optimization: convert string id's into tokens (or instance addresses), much like scanners converting strings into tokens
- self.children is a map from strings to instances
- messages contain component names - the names are local to the component (note that this implies that the Dispatcher must map sender names into receiver names)


