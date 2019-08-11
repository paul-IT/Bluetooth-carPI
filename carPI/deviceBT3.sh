x=cat file.txt | awk 'NR == 3' | awk '{print $2'}
coproc bluetoothctl
echo -e 'connect '$x '\nexit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]} > file.txt)
end=$(sed -n -e '/Device/p' file.txt)
echo $end

