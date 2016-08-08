============
MuseParse: Music Parser
============
.. image:: https://travis-ci.org/Godley/MuseParse.svg?branch=master
    :target: https://travis-ci.org/Godley/MuseParse

.. image:: https://codeclimate.com/github/Godley/MuseParse/badges/gpa.svg
   :target: https://codeclimate.com/github/Godley/MuseParse
   :alt: Code Climate

.. image:: https://codeclimate.com/github/Godley/MuseParse/badges/coverage.svg
   :target: https://codeclimate.com/github/Godley/MuseParse/coverage
   :alt: Test Coverage

.. image:: https://codeclimate.com/github/Godley/MuseParse/badges/issue_count.svg
   :target: https://codeclimate.com/github/Godley/MuseParse
   :alt: Issue Count

Repository for a python music parser. This works with MusicXML as the input format which forms a tree of objects in memory representing the piece. This can be optionally outputted to lilypond which produces a PDF, or perused for your own uses. All classes are intentionally loosely coupled, so if you would like to put in another input or output format as may come later, please do suggest them in issues and if you want, work on it yourself. For now, MusicXML is a fairly standard format.

Written for python 3 only, python 2.7 support may come later but I'm not intending on doing that unless everything else is done.

Tested against Mac OSX Yosemite, GNU / Linux Ubuntu 14.04 Desktop and Windows 8.1 64 bit.

Originally written as part of my Final Year Project(or dissertation project) at university. I earned 93 % on this along with an application of this section so you'd hope it was good.

============
Installation
============
The current version is on pypi, so to get it you can just run:

.. code-block:: bash
    pip3 install MuseParse


Otherwise clone this repo and run these commands from inside the main folder:

.. code-block:: bash
    python3 setup.py build
    python3 setup.py install

To use the lilypond rendering portion, you will need to install lilypond from http://lilypond.org.

Please note, Linux users, that whilst lilypond is on apt - get, this library expects the version to be 1.18, whilst currently apt - get only has 1.14, so I would advise downloading from the website rather than using apt - get.
============
Usage
============
****************
Setting up
****************
To aid the process of setting up lilypond, a helper is provided which does the environment variable set up so that you can run lilypond from commandline without modifying the variables yourself. The following code provides an example:

.. code-block:: python

    from MuseParse.classes.Output.helpers import setupLilypondClean as setupLilypond

    import os

    default_path_to_lily = 'path/to/lilypond/install/bin'

    setupLilypond(default_path_to_lily)

    os.system('lilypond')

Assuming you provided the right path, you should see the default help text coming into STDOUT after os.system is ran. Various assumed paths for different operating systems are provided on the `lilypond install instructions page`_

.. _lilypond install instructions page:
    http://lilypond.org/download.html
****************
Parsing music
****************
You can parse music from an xml file using the following code:

.. code-block:: python

    from MuseParse.classes.Input import MxmlParser

    parser = MxmlParser.MxmlParser()

    object_hierarchy = parser.parse(filename)

This will return a hierarchy of objects - please view the docs(link below) for more information on the objects in this hierarchy.

********************
Outputting to PDF
********************
To send it to lilypond:

.. code-block:: python
    from MuseParse.classes.Output import LilypondOutput

    render_obj = LilypondOutput.LilypondRenderer(object_hierarchy, filename)

    render_obj.run()

To provide the lilypond runner class with your own lilypond script(see http: // lilypond.org installation page for more information on this):

.. code-block:: python

    from MuseParse.classes.Output import LilypondOutput

    render_obj = LilypondOutput.LilypondRenderer(
        object_hierarchy, filename, lyscript="path/to/script")

    render_obj.run()

2 example scripts, 1 for OSX and 1 for Windows 8.1, are provided in MuseParse / demo / lilypond_scripts. If no script is provided it will assume to use the default for that platform. Linux users do not need to provide a script in any circumstance so long as lilypond is already installed.

Demo python scripts of things you could do with this are located in MuseParse / demo

=======
Documentation
=======
Please see `MuseParse @ docs.charlottegodley.co.uk`_

.. _MuseParse @ docs.charlottegodley.co.uk:
    http://docs.charlottegodley.co.uk / MuseParse

for the documentation of each class in this library, and do let me know if it could be improved or submit a pull request.
