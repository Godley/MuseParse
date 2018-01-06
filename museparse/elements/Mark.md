Module classes.ObjectHierarchy.ItemClasses.Mark
-----------------------------------------------

Classes
-------
#### Accent 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Accent

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Bend 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Bend

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### BreathMark 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.BreathMark

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Mark.Caesura

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Caesura 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Caesura

- classes.ObjectHierarchy.ItemClasses.Mark.BreathMark

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    * :return: str of lilypond code

#### DetachedLegato 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.DetachedLegato

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Fermata 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Fermata

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Notation 
Notation parent class. Not generally instantiated anywhere

# Optional inputs

* placement: above/below I think. Not used.

* symbol: symbol to display.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Descendents
- classes.ObjectHierarchy.ItemClasses.Mark.Tenuto

- classes.ObjectHierarchy.ItemClasses.Mark.StrongAccent

- classes.ObjectHierarchy.ItemClasses.Mark.Fermata

- classes.ObjectHierarchy.ItemClasses.Mark.Staccatissimo

- classes.ObjectHierarchy.ItemClasses.Mark.Bend

- classes.ObjectHierarchy.ItemClasses.Mark.Technique

- classes.ObjectHierarchy.ItemClasses.Mark.Accent

- classes.ObjectHierarchy.ItemClasses.Mark.DetachedLegato

- classes.ObjectHierarchy.ItemClasses.Mark.BreathMark

- classes.ObjectHierarchy.ItemClasses.Mark.Staccato

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    * :return: str of lilypond code

#### Staccatissimo 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Staccatissimo

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Staccato 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Staccato

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### StrongAccent 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.StrongAccent

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Technique 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Technique

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)

#### Tenuto 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.Mark.Tenuto

- classes.ObjectHierarchy.ItemClasses.Mark.Notation

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **toLily** (self)
