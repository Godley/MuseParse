Module classes.Input.MxmlParser
-------------------------------

Functions
---------
- **CheckDynamics** (tag)

- **CheckID** (tag, attrs, string, id_name)

- **CreateNote** (tag, attrs, content, piece, data)

- **HandleArpeggiates** (tags, attrs, content, piece, data)

- **HandleDirections** (tags, attrs, chars, piece, data)

- **HandleFermata** (tags, attrs, chars, piece, data)

- **HandleMeasures** (tag, attrib, content, piece, data)

- **HandleMovementBetweenDurations** (tags, attrs, chars, piece, data)

- **HandleNoteheads** (tags, attrs, content, piece, data)

- **HandlePitch** (tags, attrs, text, piece, data)

- **HandleRepeatMarking** (tags, attrs, chars, piece, data)

- **HandleSlidesAndGliss** (tags, attrs, content, piece, data)

- **IdAsInt** (index)

- **SetupFormat** (tags, attrs, text, piece, data)

- **SetupPiece** (tag, attrib, content, piece, data)

- **UpdatePart** (tag, attrib, content, piece, data)

- **YesNoToBool** (entry)

    Method which takes in either yes or no and converts it to bool. Often found in MusicXML.

    * :param entry: the word to convert

    * :return: True/False

- **handleArticulation** (tag, attrs, content, piece, data)

- **handleBarline** (tag, attrib, content, piece, data)

- **handleClef** (tag, attrib, content, piece, data)

- **handleLyrics** (tags, attrs, chars, piece, data)

- **handleOrnaments** (tags, attrs, content, piece, data)

- **handleOtherNotations** (tag, attrs, content, piece, data)

- **handleTimeMod** (tags, attrs, chars, piece, data)

- **ignore_exception** (IgnoreException=<class 'Exception'>, DefaultVal=None)

    Decorator for ignoring exception from a function
e.g.   @ignore_exception(DivideByZero)
e.g.2. ignore_exception(DivideByZero)(Divide)(2/0)

    * borrowed from: http://stackoverflow.com/questions/2262333/is-there-a-built-in-or-more-pythonic-way-to-try-to-parse-a-string-to-an-integer

Classes
-------
#### MxmlParser 
This class encases a standard XML SAX parser in order to parse MusicXML into a tree of objects. Only one is needed for any parse job
and it can be reused for multiple files.

## Optional input

- excluded - a list of tags which the parser should ignore. functionality of this is not currently implemented.

##### Ancestors (in MRO)
- classes.Input.MxmlParser.MxmlParser

- builtins.object

##### Class variables
- **data**

    A dictionary holding data which needs to be tracked by the parser, but is specific to each piece

##### Static methods
- **__init__** (self, excluded=[])

- **CopyNote** (self, part, measure_id, new_note)

    handles copying the latest note into the measure note list.
done at end of note loading to make sure staff_id is right as staff id could be encountered
any point during the note tag

    * :param part: the part class to copy it into

    * :param measure_id: the id of the measure in which the note belongs

    * :param new_note: the new note class to be copied in

    * :return: None, side effects modifying the piece tree

- **EndTag** (self, name)

    Method called by the SAX parser when a tag is ended

    
* :param name: the name of the tag

    
* :return: None, side effects

- **NewData** (self, text)

    Method which is called by the SAX parser upon encountering text inside a tag

    * :param text: the text encountered

    * :return: None, has side effects modifying the class itself

- **ResetHandler** (self, name)

    Method which assigns handler to the tag encountered before the current, or else
sets it to None

    
* :param name: name of the latest tag

    :return:

- **StartTag** (self, name, attrs)

    A method which is called by the SAX parser when a new tag is encountered

    * :param name: name of the tag

    * :param attrs: the tag's attributes

    * :return: none, side effect of modifying bits of the current class

- **clear** (self)

    Method which resets any variables held by this class, so that the parser can be used again

    * :return: Nothing

- **parse** (self, file)

    Method the programmer should call when ready to parse a file.

    * :param file: exact file path of the file to be processed

    * :return: PieceTree object representing the file in memory

- **validateData** (self, text)

    Method which validates the data from each tag, to check whether it is an empty string

    * :param text: data to be validated

    * :return: True or False depending on the result

##### Instance variables
- **closed_tags**

    any tags which close instantly in here

- **end_tag**

- **excluded**

    this will be put in later, but parser can take in tags we want to ignore, e.g clefs, measures etc.

- **multiple_attribs**

    not sure this is needed anymore, but tags which we shouldn't clear the previous data for should be added here

- **structure**

    Dictionary indicating which tags link to which handler methods
