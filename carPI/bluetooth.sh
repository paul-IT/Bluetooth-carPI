#!/bin/bash

coproc bluetoothctl
echo -e 'devices\nexit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]} > file.txt)
i=$(sudo sed -n -e '/Device/p' file.txt)
echo "$i" > file.txt

while read line; do
  echo "${line}"
done < file.txt

#for i in `cat file.txt | awk '{print $2}'`; 
#	do echo $i > $i 
#done


