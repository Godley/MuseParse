Module classes.ObjectHierarchy.ItemClasses.BaseClass
----------------------------------------------------

Classes
-------
#### Base 
A class which ensures all subclasses have a basic override of the to string method, and a toLily method

##### Ancestors (in MRO)
- classes.ObjectHierarchy.ItemClasses.BaseClass.Base

- builtins.object

##### Static methods
- **__init__** (self)

- **toLily** (self)

    Method which in any sub classes produces a string, which is a line of lilypond scripting representing the class
and its variables.

    
* :return: None, but would normally return str.

##### Instance variables
- **indent**
