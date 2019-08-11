first=`cat file.txt | awk 'NR == 1' | awk '{print $2'} | sed 's/:/_/g'`
scd=`cat file.txt | awk 'NR == 2' | awk '{print $2'} | sed 's/:/_/g'`
tre=`cat file.txt | awk 'NR == 3' | awk '{print $3'} | sed 's/:/_/g'`
four=`cat file.txt | awk 'NR == 4' | awk '{print $2'} | sed 's/:/_/g'`
qdbus --system org.bluez /org/bluez/hci0/dev_$first/player0 org.bluez.MediaPlayer1.Track >> title.txt
qdbus --system org.bluez /org/bluez/hci0/dev_$scd/player0 org.bluez.MediaPlayer1.Track >> title.txt
qdbus --system org.bluez /org/bluez/hci0/dev_$tre/player0 org.bluez.MediaPlayer1.Track >> title.txt
qdbus --system org.bluez /org/bluez/hci0/dev_$four/player0 org.bluez.MediaPlayer1.Track >> title.txt
cat title.txt | awk 'NR == 1'
cat title.txt | awk 'NR == 2'
#cat title.txt | awk 'NR == 3'
#cat title.txt | awk 'NR == 4'
cat title.txt | awk 'NR == 6'
rm -rf ./title.txt
