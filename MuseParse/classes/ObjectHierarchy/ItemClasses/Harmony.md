Module classes.ObjectHierarchy.ItemClasses.Harmony
--------------------------------------------------

Classes
-------
#### Degree 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Harmony.Degree

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Frame 
Class representing a harmony frame chart for guitarists

# Optional inputs

* - strings: the number of strings to show on the chart

* - frets: the number of frets to show on the chart

* - notes: a dictionary of notes in the frame

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Harmony.Frame

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

##### Instance variables
- **notes**

#### FrameNote 
A note to be included in the Frame notes list.

# Optional inputs

* - string: the string this note is positioned on

* - fret: the fret this note is positioned on

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Harmony.FrameNote

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Harmony 
Class representing a harmonic chord for pianists/jazz musicians. Not currently implemented 100% correct in lilypond notation

# Optional inputs

* - root: the root note of the chord

* - kind: see MusicXML docs TODO write this up

* - bass: the bass note of the chord

* - degrees: any degrees to be included in the chord

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Harmony.Harmony

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

##### Instance variables
- **degrees**

#### Kind 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Harmony.Kind

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### harmonyPitch 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Harmony.harmonyPitch

- MuseParse.classes.ObjectHierarchy.ItemClasses.Note.Pitch

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)
