from {project_name} import __version__
import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

requires = []

packages = [
    i
    for i in setuptools.find_packages()
    if i.startswith('{project_name}')
    ]

setuptools.setup(
    name='{project_name}',
    version=__version__,
    author='{author}',
    author_email='{email}',
    description='{description}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requires,{url_field}
    packages=packages,
    classifiers=[
        'Programming Language :: Python :: {ver.major}',
        {classifiers}
    ],
    python_requires='>={ver.major}.{ver.minor}',
)