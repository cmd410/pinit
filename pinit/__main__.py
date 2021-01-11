#!/usr/bin/env python3
from os import getcwd
from os.path import basename, exists, expanduser
from configparser import ConfigParser
from shutil import which
from subprocess import check_call

from licenses import License
from project import Project


def get_input(prompt: str, default='') -> str:
    return input(f'{prompt} [{default}] :') or default


def make_package():
    name = get_input('Package name', basename(getcwd()))
    project = Project(name)

    project.descr = get_input('Description', '')

    default_author = ''
    default_email = ''

    gitconfig_path = ''
    for i in ['~/.gitconfig', '~/.config/git/config']:
        path = expanduser(i)
        if exists(path):
            gitconfig_path = path
            break

    if gitconfig_path:
        config = ConfigParser()
        config.read(gitconfig_path)
        if 'user' in config:
            user_section = config['user']
            if 'name' in user_section:
                default_author = user_section['name']
            if 'email' in user_section:
                default_email = user_section['email']

    project.author = get_input('Author', default_author)
    project.email = get_input('Email', default_email)
    project.version = get_input('Version', '0.0.1')
    
    license = get_input('Licence(enter "list" to show available licenses)', 'MIT')

    while license == 'list':
        print(f'Key{" " * 18}Full name')
        print('-' * 30)
        for key, value in License._member_map_.items():
            print(f'{key} {" " * (20 - len(key))}{value.split("::")[-1].strip()}')
        print('\n')
        license = get_input('Licence(enter "list" to show available licenses)', 'MIT')
    
    license = license.strip()
    try:
        license = License[license]
    except KeyError:
        license = License(license)
    
    project.licence = license

    project.write_all()

    git_exec = which('git')

    if git_exec:
        check_call([git_exec, 'init'])

make_package()
