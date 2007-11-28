#
#  memlock.py
# 
#
#  Created by Andrew Hunter on 25/11/07.
#
# TODO: Add way to append the correct line if one does not exist.
# TODO: Backup conf file before overwriting :P
# TODO: Come up with better varriable names

import re

find_memlock = re.compile('@audio - memlock \d*')
limits_conf = open('/etc/security/limits.conf', 'r+')
limits_conf_read = open('/etc/security/limits.conf', 'r')
oldlines = limits_conf_read.read()

def ch_memlock(new_memlock):
  line_replacement = '@audio - memlock ' + new_memlock
  memlock_check = find_memlock.search(oldlines) #determine if an audio memlock already exists
  if memlock_check:
    print 'memlock_check is true'
    _update(line_replacement)
    limits_conf.close()
  else:
    _append(line_replacement)
    limits_conf.close()

def _update(line_replacement):
  newlines = []
  for item in limits_conf:
    line_memlock = find_memlock.search(item) #Is the current line the one we want?
    if line_memlock:
      newlines.append(find_memlock.sub(line_replacement, item))
    else:
      newlines.append(item)

  limits_conf.seek(0)
  limits_conf.writelines(newlines)

def _append(line_replacement):
  append_list = limits_conf.readlines()
  append_list[-1] = line_replacement + '\n\n#End of file' #Assumes that #End of file is the last line
  limits_conf.seek(0)
  limits_conf.writelines(append_list)

