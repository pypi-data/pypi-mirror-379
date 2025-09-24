import os
import pickle
import inspect
import re
import traceback
# from varname import nameof

def cache_obj(varible, var_name=None, cache_dir='./_cache_', max_count=10000, mode='w', pkg_name=None, print_on=True):

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    
    if mode == 'r':
        if pkg_name is None:
            
            pkl_path = f'{cache_dir}/{varible}.pkl'
        else:
            pkl_path = f'../{pkg_name}_pkg//{cache_dir[1:]}/{varible}.pkl'

        with open(pkl_path, 'rb') as file:
            var_value = pickle.load(file)
            return var_value
    
    if var_name is None: # get the variable name by looping the parent function
        # lcls = inspect.stack()[2][0].f_locals
        # for name in lcls:
        #     if id(varible) == id(lcls[name]):
        #         var_name = name

        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        var_name_raw = re.compile(r'\((.*?)\).*$').search(code).groups()[0] # the default name is everything in the bracket, like: 'None_0', mode='w'
        var_name = var_name_raw.split(',')[0] 
        pkl_path = f'{cache_dir}/{var_name}.pkl'

    if var_name is None: # get the name by adding incremental number on the default name
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        var_name = 'cached_variable'
        for count_of_cached_obj in range(max_count):
            pkl_path = f'{cache_dir}/{var_name}_{count_of_cached_obj}.pkl'
            if not os.path.exists(pkl_path):
                break
        
    with open(pkl_path, 'wb') as file:
        pickle.dump(varible, file)

    if print_on:
        print(var_name+": ", varible)

    print(f'[INFO]: the value of variable [{var_name}] has been cached under ./_cache_!')
