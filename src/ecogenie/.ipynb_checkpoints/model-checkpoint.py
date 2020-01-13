import os
from os import path
import pandas as pd
import numpy as np

def check_dirs(working_directories):

    notebooks_dir = os.path.dirname(os.path.realpath('__file__'))
    root_dir = path.abspath(path.join(notebooks_dir, '..'))

    critical_dirs = working_directories['critical_dirs'].values.tolist()

    list_and_check_dirs(root_dir, critical_dirs, working_directories)

# from: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def list_and_check_dirs(startpath, critical_dirs, working_directories):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        if os.path.basename(root) in critical_dirs:
#          print('{}/{}/'.format(os.path.dirname(root), os.path.basename(root)))
          working_directories.loc[working_directories['critical_dirs'] == os.path.basename(root),
                                  'absolute_path'] = os.path.dirname(root) +'/' + os.path.basename(root)
        subindent = ' ' * 4 * (level + 1)
# missing directories
    # ensure that empty fields are set to NaN
    working_directories['absolute_path'].replace('', np.nan, inplace=True)
    #create a list of indices
    missing_dirs=working_directories.iloc[np.where(pd.isnull(working_directories))].index.tolist()
    for i in missing_dirs:
        print('{} {}/'.format('Missing critical directory: ', working_directories.loc[i,'critical_dirs']))
    if not missing_dirs:
        print('All critical directories exist and are set in data frame: working_directories')
