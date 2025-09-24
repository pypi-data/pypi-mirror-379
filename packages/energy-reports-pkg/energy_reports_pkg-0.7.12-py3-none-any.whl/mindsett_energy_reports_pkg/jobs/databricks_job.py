
import sys

sys.path.append('../')

import libs
import mdl
import config as cf


param_list = sys.argv[1:]
param_dict = {}
for i in range(len(param_list)//2):
    param_dict[param_list[int(i*2)]] = param_list[int(i*2+1)]

# redo_from_start = bool(dbutils.widgets.get("redo_from_start"))

print('param_dict: ', param_dict)

mode_param = param_dict['mode']

print('mode_param: ', mode_param)

# mode = 'publish'
cache_directory = '/dbfs/FileStore/shared_uploads/x.yang@cloudfmgroup.com/cache_folder_for_jobs/'

mdl.prepare_and_email_reports(cf, 
                              mode=mode_param, 
                              sync_source=True,
                              cache_in_memory=True, 
                              cache_directory=cache_directory)