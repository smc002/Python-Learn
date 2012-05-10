#!/usr/bin/python
# Filename: backup_ver2.py

import os
import time

source = ['~/Desktop', '~/Python-Learn', '/usr/local/bin']

target_dir = '/home/sunmengchao/Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
	comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
	print(today)
	os.mkdir(today)
	print ('Successfully created directory', today)


zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print(zip_command)
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')
