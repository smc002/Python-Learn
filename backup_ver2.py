#!/usr/bin/python
# Filename: backup_ver2.py

import os
import time

source = ['~/Desktop', '~/Python-Learn']

target_dir = '~/Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print ('Successfully created directory', today)

target = today + os.sep + now + '.zip'


zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print(zip_command)
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')
