#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

source = ['~/Desktop', '~/Python-Learn']

target_dir = '~/Backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print(zip_command)
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')
