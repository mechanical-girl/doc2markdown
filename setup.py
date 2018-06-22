from distutils.core import setup

setup(  name='doc2markdown',
        version='1.00',
        description='Converts Python docstrings to GitHub-flavoured markdown',
        author='Pouncy Silverkitten',
        author_email='pouncy.sk@gmail.com',
        url='https://github.com/pouncysilverkitten/doc2markdown',
        entry_points = {
            'console_scripts': ['doc2markdown=main'],})
