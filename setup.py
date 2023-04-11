#!/usr/bin/env python3

import subprocess
import os
from setuptools import setup
from setuptools.command.install import install
import shutil





# Install dependencies
subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'install', '-y', 'gobuster'])

destination_folder = '/usr/share/wordlists/'
wordlist_folder_path = './htbhound'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    for root, dirs, files in os.walk(wordlist_folder_path):
        for directory in dirs:
            # create the directory in the destination folder
            os.makedirs(os.path.join(destination_folder, root, directory), exist_ok=True)
        for file in files:
            # copy the file to the destination folder
            shutil.copy(os.path.join(root, file), os.path.join(destination_folder, root, file))
    setup(
        name='htbhound',
        version='1.0.0',
        #scripts=['htbhound.py'],
        py_modules=['htbhound'],
        description='HTBHound is a powerful Python-based tool designed to aid in the enumeration of subdomains, directories, and files for web machines on Hack The Box.',
        long_description= 'README.md',
        author='Danny LLi',
        author_email='dannylligithub@gmail.com',
        url='https://github.com/Danny-LLi/HTBHound',
        install_requires=[
#            'os-sys',
#            'subprocess.run',
#            'futures',
#            'pytest-shutil',
        ],
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        entry_points={
            'console_scripts': [
                'htbhound=htbhound:main'
            ]
        }
    )
else:
    try:
        for root, dirs, files in os.walk(wordlist_folder_path):
            for directory in dirs:
                # create the directory in the destination folder
                os.makedirs(os.path.join(destination_folder, root, directory), exist_ok=True)
            for file in files:
                # copy the file to the destination folder
                shutil.copy(os.path.join(root, file), os.path.join(destination_folder, root, file))
        setup(
            name='htbhound',
            version='1.0.0',
            #scripts=['htbhound.py'],
            py_modules=['htbhound'],
            description='HTBHound is a powerful Python-based tool designed to aid in the enumeration of subdomains, directories, and files for web machines on Hack The Box.',
            long_description= 'README.md',
            author='Danny LLi',
            author_email='dannylligithub@gmail.com',
            url='https://github.com/Danny-LLi/HTBHound',
            install_requires=[
#                'os-sys',
#                'subprocess.run',
#                'futures',
#                'pytest-shutil',
            ],
            classifiers=[
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
            ],
            entry_points={
                'console_scripts': [
                    'htbhound=htbhound:main'
                ]
            }
        )
    except:
    
        setup(
            name='htbhound',
            version='1.0.0',
            #scripts=['htbhound.py'],
            py_modules=['htbhound'],
            description='HTBHound is a powerful Python-based tool designed to aid in the enumeration of subdomains, directories, and files for web machines on Hack The Box.',
            long_description= 'README.md',
            author='Danny LLi',
            author_email='dannylligithub@gmail.com',
            url='https://github.com/Danny-LLi/HTBHound',
            install_requires=[
#                'os-sys',
#                'subprocess.run',
#                'futures',
#                'pytest-shutil',
            ],
            classifiers=[
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
            ],
            entry_points={
                'console_scripts': [
                    'htbhound=htbhound:main'
                ]
            }
        )


