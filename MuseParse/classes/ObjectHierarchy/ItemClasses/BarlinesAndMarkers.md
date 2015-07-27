Module classes.ObjectHierarchy.ItemClasses.BarlinesAndMarkers
-------------------------------------------------------------

Classes
-------
#### Barline 
Barline class.

# Optional inputs

* - style: style of barline to display

* - repeat: bool whether it's a repeat or not

* - ending: instance of the EndingMark class representing which ending number this barline is, see below

* - repeatNum: number of repeats. Default is 2

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.BarlinesAndMarkers.Barline

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### EndingMark 
Ending marker. Used particularly in lilypond where there are repeats with alternative endings.

# Optional inputs

* - number: the ending which this is, e.g ending 1 or 2

* - type: the type of ending marker it is. If it comes at the beginning of a bar, it's anything that isn't
discontinue or stop. If it's at the end, opposite is true.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.BarlinesAndMarkers.EndingMark

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Transposition 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.BarlinesAndMarkers.Transposition

- MuseParse.classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)
