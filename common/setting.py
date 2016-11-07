import os
import sys
root_dir = '/'.join(os.path.realpath(__file__).split('/')[:-1])
sys.path.append(root_dir)
# log等级,1:notset 2:debug  3:info 4:warning 5:error 6:critical
loglevel = 2
# 日志文件路径
logfile = os.path.join(root_dir, 'logs')