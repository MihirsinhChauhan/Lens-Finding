import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s')

project_name = 'LenseClassifier'

# list of files to be created
list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'./{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'research/trails.ipynb',
    'setup.py',
]

for filepath in list_of_files:
    filepath = Path(filepath) # convert into windows path
    filedir, filename = os.path.split(filepath) # split into directory and filename

    if filedir != '':
        os.makedirs(filedir, exist_ok=True) # create directory
        logging.info(f'Creating directory : {filedir}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # check if file exists
        with open(filepath, 'w') as f: # create file
            pass
        logging.info(f' Creatinfg empty file : {filepath}')
    
    else:
        logging.info(f'{filepath} is already created')
