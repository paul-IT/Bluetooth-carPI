first=`cat file.txt | awk 'NR == 1' | awk '{print $2'} | sed 's/:/_/g'`
scd=`cat file.txt | awk 'NR == 2' | awk '{print $2'} | sed 's/:/_/g'`
tre=`cat file.txt | awk 'NR == 3' | awk '{print $2'} | sed 's/:/_/g'`
four=`cat file.txt | awk 'NR == 4' | awk '{print $2'} | sed 's/:/_/g'`
dbus-send --system --print-reply --dest=org.bluez /org/bluez/hci0/dev_$first org.bluez.MediaControl1.Pause
dbus-send --system --print-reply --dest=org.bluez /org/bluez/hci0/dev_$scd org.bluez.MediaControl1.Pause
dbus-send --system --print-reply --dest=org.bluez /org/bluez/hci0/dev_$tre org.bluez.MediaControl1.Pause
dbus-send --system --print-reply --dest=org.bluez /org/bluez/hci0/dev_$four org.bluez.MediaControl1.Pause
