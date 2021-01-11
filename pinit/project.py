from os import getcwd, mkdir
from os.path import dirname, join, exists
from sys import version_info


class Project:
    def __init__(self, name=None, version='0.0.1'):
        self.name = name or dirname(getcwd())
        self.descr = ''
        self.url = ''
        self.author = ''
        self.email = ''
        self.requires = []
        self.version = version
        self.licence = ''

    @property
    def classifiers(self) -> str:
        return (',\n' + ' ' * 8).join(
            [
                f'\'{i}\''
                for i in [self.licence]
            ]
        )

    def get_setup(self):
        with open(
                  join(dirname(__file__), 'setup_template.pyi'), 'r'
                 ) as file:
            format_string = file.read()
            return format_string.format(
                project_name = self.name,
                author = self.author,
                email = self.email,
                description = self.descr,
                ver = version_info,
                classifiers = self.classifiers,
                url_field = '' if not self.url else f',\n    url=\'{self.url}\''
            )
    
    def get_readme(self):
        return f'''# {self.name}
                   \r{self.descr}'''
    
    def get_init(self):
        return f'__version__ = \'{self.version}\'\n'
    
    def write_all(self):
        proj_dir = getcwd()

        def path_to(*args):
            nonlocal proj_dir
            return join(proj_dir, *args)

        with open(path_to('setup.py'), 'w') as file:
            file.write(self.get_setup())
        
        with open(path_to('README.md'), 'w') as file:
            file.write(self.get_readme())
        
        if not exists(path_to(self.name)):
            mkdir(self.name)

        with open(path_to(self.name, '__init__.py'), 'w') as file:
            file.write(self.get_init())

        with open(path_to('.gitignore'), 'w') as file:
            file.write('__pycache__\n')
            file.write('.venv\n')
            file.write('.vscode\n')
            file.write('.idea\n')

        if not exists(path_to('tests')):
            mkdir('tests')
        
        with open(path_to('tests', '__init__.py'), 'w') as file:
            file.write('# TODO write some test code\n')