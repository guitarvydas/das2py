# helloworld.bash
conn0=conn0_$RANDOM
mkfifo $conn0
./world.bash 3<$conn0  &
pid_world=$!
./hello.bash 4>$conn0  &
pid_hello=$!
wait $pid_world
wait $pid_hello
rm $conn0
