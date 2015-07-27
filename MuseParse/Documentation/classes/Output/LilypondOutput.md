Module classes.Output.LilypondOutput
------------------------------------

Classes
-------
#### LilypondRenderer 
Class which handles output of a PieceTree class, or in fact, any other hierarchy where each object has its own toLily method.

# Required Inputs

* - piece_obj: the hierarchy of objects representing the piece in memory

* - fname: the location of the original file being represented. Extension not important, but should be there.

# Optional Inputs

* - lyscript: the location of the script which should be ran as the first argument in the command to execute lilypond. If none is given, the system will take the default script according to the command line instructions on the lilypond website.

##### Ancestors (in MRO)
- classes.Output.LilypondOutput.LilypondRenderer

- builtins.object

##### Static methods
- **__init__** (self, piece_obj, fname, lyscript='')

- **cleanup** (self, pdf=False)

- **run** (self, wrappers=['', ''])

    run the lilypond script on the hierarchy class

    
* :param wrappers: this is useful for testing: use wrappers to put something around the outputted "lilypond string" from the hierarchy class.  
For example if you're testing a pitch, you might put 
elative c {} around the note so that lilypond handles it properly without causing an error

    
* :return: doesn't return anything, side effect that a PDF should be created.

##### Instance variables
- **defaults**

- **file**

- **folder**

- **lyfile**

- **pdf**

- **piece_obj**
