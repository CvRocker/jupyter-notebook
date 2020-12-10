#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import json


def get_file_list(file_path, exts_list, depth=-1):        
    if depth == 0:
        return []
    
    if file_path is None or not os.path.exists(file_path):
        raise Exception("not found any img file in {}".format(file_path))
    
    files_list = []
    
    if os.path.isfile(file_path):
#         file_ext = file_path.spilt(.)[-1]
        file_ext = file_path[file_path.rfind('.'):]
#         print(f'file_ext:{file_ext}')

        if file_ext in exts_list:
            files_list.append(file_path)
    elif os.path.isdir(file_path):
        for file in os.listdir(file_path):
            sub_file_path = os.path.join(file_path, file)
#             print(f'sub_file_path:{sub_file_path}')
            # 下一级文件或目录
            if os.path.isfile(sub_file_path):
                _depth = depth
            elif os.path.isdir(sub_file_path):                
                _depth = depth - 1
            try:    
                files_list += get_file_list(sub_file_path, exts_list, _depth)
            except Exception as e: 
                print({e})
            else:
                pass
                
    if len(files_list) == 0:
        raise Exception("not found any img file in {}".format(file_path))
        
    return files_list


def main():
    try:
        files_list = get_file_list('../../test/', ('.mod', '.txt', '.cpp', '.o'), 1)
    except Exception as e: 
        print({e})
    else:
        pass
        
    
    for single_file in files_list:        
        print(f'file : {single_file}')

    
if __name__ == '__main__':
    main()

