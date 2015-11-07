============
MuseParse: Music Parser
============
.. image:: https://travis-ci.org/Godley/MuseParse.svg?branch=master
    :target: https://travis-ci.org/Godley/MuseParse
Repository for a python music parser. This works with MusicXML as the input format which forms a tree of objects in memory representing the piece. This can be optionally outputted to lilypond which produces a PDF, or perused for your own uses. All classes are intentionally loosely coupled, so if you would like to put in another input or output format as may come later, please do suggest them in issues and if you want, work on it yourself. For now, MusicXML is a fairly standard format. 

Written for python 3 only, python 2.7 support may come later but I'm not intending on doing that unless everything else is done.

Tested against Mac OSX Yosemite, GNU/Linux Ubuntu 14.04 Desktop and Windows 8.1 64 bit.

Originally written as part of my Final Year Project (or dissertation project) at university. I earned 93% on this along with an application of this section so you'd hope it was good.

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

To use the Lilypond rendering classes, you will also need to `install lilypond.`_

.. _install lilypond: http://lilypond.org

Note that whilst lilypond is on apt-get, it is version 1.14 whilst this library uses 1.18, so even if you are a linux user I would still advise downloading directly from the lilypond website.
=======
Usage
=======
****************
Parsing music
****************
You can parse music from an xml file using the following code:

.. code-block:: python
   
   from MuseParse.classes.Input import MxmlParser
  
   parser = MxmlParser.MxmlParser()

   object_hierarchy = parser.parse(filename)

This will return a hierarchy of objects - please view the docs (link below) for more information on the objects in this hierarchy.

********************
Outputting to PDF
********************
To send it to lilypond:

.. code-block:: python

   from MuseParse.classes.Output import LilypondOutput

   render_obj = LilypondOutput.LilypondRenderer(object_hierarchy, filename)

   render_obj.run()

To provide the lilypond runner class with your own lilypond script (see http://lilypond.org installation page for more information on this):

.. code-block:: python

   from MuseParse.classes.Output import LilypondOutput

   render_obj = LilypondOutput.LilypondRenderer(object_hierarchy, filename, lyscript="path/to/script")

   render_obj.run()

2 example scripts, 1 for OSX and 1 for Windows 8.1, are provided in MuseParse/demo/lilypond_scripts. If no script is provided it will assume to use the default for that platform. Linux users do not need to provide a script in any circumstance so long as lilypond is already installed.

Demo python scripts of things you could do with this are located in MuseParse/demo

=======
Documentation
=======
Please see `Music-Parser @ docs.charlottegodley.co.uk`_

.. _MuseParse @ docs.charlottegodley.co.uk: http://docs.charlottegodley.co.uk/MuseParse

for the documentation of each class in this library, and do let me know if it could be improved or submit a pull request.
