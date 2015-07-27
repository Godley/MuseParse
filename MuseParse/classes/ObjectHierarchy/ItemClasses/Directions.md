Module classes.ObjectHierarchy.ItemClasses.Directions
-----------------------------------------------------

Classes
-------
#### Bracket 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Bracket

- classes.ObjectHierarchy.ItemClasses.Directions.Line

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

#### CreditText 
Class which represents credits - anything which is to go at the bottom of the page, like copyrights,
authors etc. Essentially the same as text except it can be positioned

# Optional inputs

* - x: the x position of the text

* - y: the y position of the text

* - justify: left/right

* - valign: vertical alignment - top/bottom

* - page: unused, but the page to put this text on

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.CreditText

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

#### Direction 
Class representing directions - see sub classes for what these generally are. This class is used for
regular text directions such as "andante" or "cantabile"

# Optional inputs

* - placement: above or below the bar

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Directions.RepeatSign

- classes.ObjectHierarchy.ItemClasses.Directions.Forward

- classes.ObjectHierarchy.ItemClasses.Directions.Line

- classes.ObjectHierarchy.ItemClasses.Directions.Dynamic

- classes.ObjectHierarchy.ItemClasses.Directions.RehearsalMark

- classes.ObjectHierarchy.ItemClasses.Directions.Slur

- classes.ObjectHierarchy.ItemClasses.Directions.Metronome

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

#### Dynamic 
Dynamic marking class

# Optional inputs

* - mark: the mark to use in the dynamic

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Dynamic

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Directions.Wedge

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### Forward 
Probably an unused class - forwards arent what I thought they were.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Forward

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### Line 
Class representing lines over the bar, such as brackets or braces. Essentially I think this is a stub to be sub classed
so don't instantiate line on its own without some modification.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Line

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Directions.OctaveShift

- classes.ObjectHierarchy.ItemClasses.Directions.WavyLine

- classes.ObjectHierarchy.ItemClasses.Directions.Pedal

- classes.ObjectHierarchy.ItemClasses.Directions.Bracket

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### Lyric 
Text class representing lyrics. Unused because needs readjustment in order to fit lyrics into Lilypond's output.  
Essentially the same as text but 1 additional input

# Optional input

* - syllabic: whether this lyric is meant to fit syllables to each diff note

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Lyric

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### Metronome 
Class representing a metronome mark, which can be a combination of <note> = <number per minute> and text

# Optional inputs

* - beat: the beat marker. I.e <beat> = <bpm>

* - min: the number of beats per minute.

* - secondBeat: in place of min, could also have this representing another beat. Like crotchet = quaver

* - text: the text to display with the metronome mark

attributes:  

* - parentheses: this could also be optionally set later to indicate whether or not to put parentheses round the mark.
bool.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Metronome

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **get_detail** (self)

- **toLily** (self)

#### OctaveShift 
Class representing specifically octave shifts

# Optional inputs

* - amount: the amount to shift up/down octaves. Int, generally 8 or 15 depending on whether 1 or 2

* - type: type of shift - up/down.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.OctaveShift

- classes.ObjectHierarchy.ItemClasses.Directions.Line

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

#### Pedal 
A piano pedal marker class.

# Optional inputs

* - line: bool representing whether or not to display a line

* - type: start/stop

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Pedal

- classes.ObjectHierarchy.ItemClasses.Directions.Line

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

#### RehearsalMark 
Class representing rehearsal marks like A in a box above a bar.
  
Same as direction, except that text - generally "A" or "C" is used to figure out which number mark lilypond is expecting.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.RehearsalMark

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### RepeatSign 
Class representing coda symbols and DC symbols.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.RepeatSign

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

##### Instance variables
- **noquotes**

#### Slur 
Slur class

# Optional inputs

* - type: start/stop

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Slur

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### Text 
A class representing any kind of text

# Optional inputs

* - font: the font to use. If this isn't in the list of fonts in lilypond, a random one will be picked.

* - size: font size to use

* - text: the actual text to display

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Directions.CreditText

- classes.ObjectHierarchy.ItemClasses.Directions.Lyric

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### WavyLine 
Class representing a wavy line, such as the one used for an extended trill marking

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.WavyLine

- classes.ObjectHierarchy.ItemClasses.Directions.Line

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

#### Wedge 
Wedge - i.e crescendo line or decrescendo line

# Optional inputs

* - type: crescendo/diminuendo/stop. In Lilypond stop is an option because every wedge must end somewhere,
and this gives an indication to stop the wedge at x position.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Directions.Wedge

- classes.ObjectHierarchy.ItemClasses.Directions.Dynamic

- classes.ObjectHierarchy.ItemClasses.Directions.Direction

- classes.ObjectHierarchy.ItemClasses.Directions.Text

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **get** (self)

    method to fetch all contents as a list

    
* :return: list

- **toLily** (self)

##### Instance variables
- **type**
