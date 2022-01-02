#!/bin/bash
clear
#../make.bash

# #das2j helloworld >out.json
# ./emit.py sample.json helloworld
# # echo
# # cat hello.py
# # echo
# # cat world.py
# echo
# cat helloworld.py

# # echo '** running top.'
# # chmod a+x top.py
# # ./top.py


das2j helloworld >out1.json
./emit.py out1.json helloworld

echo running result...
./top.py

