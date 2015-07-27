Module classes.ObjectHierarchy.TreeClasses.VoiceNode
----------------------------------------------------

Classes
-------
#### VoiceNode 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.VoiceNode.VoiceNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetAllNoteTypes** (self)

    method to collect all note values from each node

    
* :return: list of note values

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **RunNoteChecks** (self)

- **SetItem** (self, new_item)

- **addNoteDuration** (self, duration)

- **removeNoteDuration** (self, duration)

- **toLily** (self)

    Method which converts the object instance, its attributes and children to a string of lilypond code

    
* :return: str of lilypond code

##### Instance variables
- **note_total**

- **note_types**
