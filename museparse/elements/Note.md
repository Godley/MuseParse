Module classes.ObjectHierarchy.ItemClasses.Note
-----------------------------------------------

Classes
-------
#### Arpeggiate 
Arpeggiate class
  
Optional inputs:  

* direction: direction the arrow head of the arpeggiate should put. Generally up or down I think

* type: whether this is start/stop/none. None indicates it's somewhere in the middle.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Arpeggiate

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Note.NonArpeggiate

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

##### Instance variables
- **wrapped**

#### Beam 
Class representing beam information. Normally this is automatic, but it comes in from MusicXML anyway
so may be useful at some stage.

# Optional input
- type - indicates whether this is a starting, continuing or ending beam.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Beam

- classes.ObjectHierarchy.ItemClasses.Note.Stem

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, type)

- **toLily** (self)

#### Glissando 
A glissando - like a slide, but it really only comes in "wavy" type so lineType is completely ignored.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Glissando

- classes.ObjectHierarchy.ItemClasses.Note.Slide

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### GraceNote 
Gracenotes.
  
Optional inputs:  

* slash: bool - indicates whether or not the gracenote should be slashed

* first: bool - indicates whether or not this is the first gracenote

attributes:  

* last: bool - indicates whether or not this is the last gracenote in a sequence of gracenotes.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.GraceNote

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### NonArpeggiate 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.NonArpeggiate

- classes.ObjectHierarchy.ItemClasses.Note.Arpeggiate

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Note 
Big class representing a note.
  
Optional inputs:  

* rest: bool as to whether this note is a rest or not.

* dots: int - number of dots after the note, indicating extended length

* pitch: a class representing the pitch of the note, see above

* chord: bool indicating this note is part of a chord

* type: string indicator of the length of note, like "quarter" or "half". Alternatively, duration may be given along with divisions

* duration: length of note. Where musicXML is concerned, divisions should also be known, indicating how many divisions there are in
a quarter note.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Note

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **AddSlur** (self, item)

    Very simple method which is used for adding slurs.
:param item:  
:return:

- **AddTie** (self, type)

- **CheckDivisions** (self, measure_div)

    Method which is called from voice/measure to update the divisions for each note which are stored at
measure level, but needed at lilypond time to figure out lilypond notation

    * :param measure_div: number of divisions per note. Indicator of how big or small a quarter note is

    * :return: None, side effect

- **FlushNotation** (self)

- **GetAllNotation** (self)

- **GetBeams** (self)

- **GetClosingNotationLilies** (self)

    Converts notation in closing_notation into a lilypond string.

    * :return: str

- **GetNotation** (self, id, type)

    method which searches for notation from <type> list at position <id>

    * :param id: the number to look for - i.e if you're looking for the first one in wrap notation, id will be 0

    * :param type: post, pre or wrap

    * :return: the notation class searched for or none

- **LilyWrap** (self, value)

    Method to fetch lilypond representation of wrap_notation

    * :param value: current lilypond string to wrap

    * :return: updated lilypond string

- **Search** (self, cls_type, list_id=-1)

    Method which looks for a particular class type in a particular list

    * :param cls_type: the type of object to find

    * :param list_id: the list it resides in

    * :return: the first object of cls_type, or None

- **SetType** (self, vtype)

    Sets the type, i.e duration of the note. Types are given as keys inside options

    * :param vtype: str - see keys in options for full list

    * :return: None, side effects modifying the class

- **addBeam** (self, id, beam)

- **addDot** (self)

- **addNotation** (self, obj)

    Method to add new notation. Use this rather than adding directly so new classes can be added automatically
without needing to know which list to add it to in the main code.

    * :param obj: the object to add

    * :return: None

- **getLilyDuration** (self)

    method to calculate duration of note in lilypond duration style
:return:

- **handlePostLilies** (self)

- **handlePreLilies** (self)

    Fetches all notation to come before the note as a lilypond string

    * :return: str

- **toLily** (self)

##### Instance variables
- **beams**

- **closing_notation**

    notation to be shown after post notation - list

- **has_tremolo**

- **postnotation**

    notation to be shown after the note - list

- **prenotation**

    any notation classes which come before the note is displayed - list

- **ties**

- **wrap_notation**

    any notation classes which have something to come before and something after the note is displayed - list

#### Notehead 
Class representing noteheads.  
Optional inputs:  

* filled: whether or not the notehead is filled. bool.

* type: type of notehead. str.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Notehead

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, filled=False, type='')

- **toLily** (self)

##### Instance variables
- **filled**

- **type**

#### Pitch 
Class representing the pitch of the note
  
Optional inputs:  

* alter: how many semi tones to raise or lower the pitch. Generally either 1 or -1, float.

* octave: number of the octave in which it resides in. int

* accidental: accidental to show. Used where alter is not accurate enough, may indicate any range of accidentals such as
double sharps etc.

* unpitched: bool representation of unpitchedness, aka a pitch which is like a clap or something rather than an actual note.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Pitch

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Slide 
Optional Inputs:  

* type: the type of gliss, i.e start or stop

* lineType: style of line to use

* number: something that comes in from MusicXML but isn't actually used at min.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Slide

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Note.Glissando

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

##### Instance variables
- **wrapped**

#### Stem 
Class representing the note's stem.
optional input:  

* type: type of stem to show

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Stem

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Note.Beam

##### Static methods
- **__init__** (self, type)

- **toLily** (self)

#### Tie 
Class representing a tie.
  
Optional inputs:  

* type: either start or stop. Stop isn't particularly useful to lilypond but may be used in other output formats.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Tie

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, type)

- **toLily** (self)

#### TimeModifier 

* Class representing a time mod: these sometimes appear in music xml where there are tuplets.
  
Optional inputs:  

* first: bool - indicates this is the first tuplet

* normal: what the note would normally split into

* actual: the modifier to actually use.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.TimeModifier

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

##### Instance variables
- **first**

#### Tuplet 
Tuplet class.
  
Optional inputs:  

* type: either start or stop. Represents that this is either the first or last tuplet in the group.

* bracket: bool, indicating whether or not to bracket the tuplets.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Note.Tuplet

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)
