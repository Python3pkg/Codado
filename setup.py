from inspect import cleandoc

from setuptools import setup

_version = {}
exec(compile(open('codado/_version.py').read(), 'codado/_version.py', 'exec'), _version)

setup(
    name = 'Codado',
    packages = ['codado', 'codado.kleinish'],
    version = _version['__version__'],
    description = 'A collection of system development utilities',
    author = 'Cory Dodt',
    author_email = 'corydodt@gmail.com',
    url = 'https://github.com/corydodt/Codado',
    keywords = ['twisted', 'utility'],
    classifiers = [],
    scripts = ['bin/urltool', 'bin/jentemplate'],
    install_requires=cleandoc('''
        attrs
        ftfy==4.4.3
        jinja2
        python-dateutil==2.4.0
        pytz==2015.4
        pyyaml
        werkzeug
        ''').split()
)
