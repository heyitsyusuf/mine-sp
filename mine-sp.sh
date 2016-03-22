#!/bin/bash
category='Pet+Grooming'
term='grooming'
zone='30301'
radius='77'
folderpath='/home/yusuf/my-scripts/sp-mining/'$term'-'$zone
index=14
mkdir -p $folderpath
cd $folderpath
while [ $index -lt 777 ]
do
wget -O $folderpath/$index'.txt' 'http://yellowpages.superpages.com/listings.jsp?C='$term'+near+'$zone'&CTS='$category'&R=D&RR='$radius'&PI='$index
index=$(($index + 15))
cat $folderpath/* > $folderpath/$term'+stock.txt'
done
echo $(grep 'telephone\"' $folderpath/$term'+stock.txt' | cut -d\( -f2 | cut -d\< -f1 | sed -e 's/)\ //g' | sed -e 's/-//g' | sed -e 's/"/,/g') > $folderpath/$term'+'$zone'.txt'
exit

#category='Photography'
#category='Beauty+Salons'
#category='Manicures+Pedicures'
#category='Tailors'
#category='Barbers'
#category='Animal+Hospitals'
#category='Veterinarians'
