from distutils.core import setup

setup(
    name='MuseParse',
    version='1.1.5',
    packages=['MuseParse', 'MuseParse.demo', 'MuseParse.classes',
              'MuseParse.classes.Input', 'MuseParse.classes.Output', 'MuseParse.classes.ObjectHierarchy',
              'MuseParse.classes.ObjectHierarchy.ItemClasses', 'MuseParse.classes.ObjectHierarchy.TreeClasses'],
    url='http://github.com/godley/MuseParse',
    license='MIT',
    author='charlottegodley',
    author_email='me@charlottegodley.co.uk',
    description='A package which takes an inputted music file (at the moment only MusicXML) and generates an object hierarchy in memory. This version fixes a bug in the music xml parser and provides lilypond setup methods for each operating system.'

)
