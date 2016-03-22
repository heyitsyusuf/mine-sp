import urllib.request
import sys
import os
import re

raw_data_file_w=open('raw_data_file.txt', 'w')
raw_data_file_r=open('raw_data_file.txt', 'r')

def makefile():
	zone='60604'
	term='grooming'
	category=term.capitalize()
	radius='50'
	index='15'
	url=('http://yellowpages.superpages.com/listings.jsp?C='+term+'+near+'+zone+'&CTS='+category+'&R=D&RR='+radius+'&PI='+index)
	raw_data=urllib.request.urlopen(url).read()
	less_raw_data=str(raw_data)
	raw_data_file_w.write(less_raw_data.strip('\n'))
	raw_data_file_w.close()
	return


makefile()


contents=raw_data_file_r.read()
name=re.findall(r'\"name\": \"(.*?)\",\\n', contents)
telephone=re.findall(r'\"telephone\": \"(.*?)\"\\n}', contents)
streetaddress=re.findall(r'\"streetAddress\": \"(.*?)\"\\n}', contents)
addresslocality=re.findall(r'\"addressLocality\": \"(.*?)\",\\n', contents)
addressregion=re.findall(r'\"addressRegion\": \"(.*?)\",\\n', contents)
postalcode=re.findall(r'\"postalCode\": \"(.*?)\",\\n', contents)

index=len(name)-1

while index !=-1:
	fullcontact=name[index]+telephone[index]+streetaddress[index]+addressregion[index]+addresslocality[index]+postalcode[index]
	print(fullcontact)
	print(index)
	index=index-1



raw_data_file_r.close()
