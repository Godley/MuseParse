Module classes.ObjectHierarchy.TreeClasses.PieceTree
----------------------------------------------------

Classes
-------
#### PieceTree 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.PieceTree.PieceTree

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Tree

- builtins.object

##### Static methods
- **__init__** (self)

- **AddNode** (self, node, index=-1)

- **AddToGroup** (self, name, index)

- **FindNode** (self, cls_type, index, id=None)

- **FindNodeByIndex** (self, index)

- **GetItem** (self)

- **GetSortedChildren** (self)

- **SetItem** (self, i)

- **SetValue** (self, item)

- **addPart** (self, item, index=-1)

- **getGroup** (self, name)

- **getLastPart** (self)

- **getPart** (self, key)

- **handleGroups** (self)

- **removePart** (self, id)

- **startGroup** (self, index)

- **stopGroup** (self, index)

- **toLily** (self)

    Method which converts the object instance, its attributes and children to a string of lilypond code

    
* :return: str of lilypond code

##### Instance variables
- **current**

- **groups**

- **item**

- **root**
