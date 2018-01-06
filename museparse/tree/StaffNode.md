Module classes.ObjectHierarchy.TreeClasses.StaffNode
----------------------------------------------------

Classes
-------
#### StaffNode 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.StaffNode.StaffNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.IndexedNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self)

- **AddBarline** (self, item=None, measure_id=1, location='left')

- **AddChild** (self, item, index=-1)

- **AddRule** (self, rule)

- **CheckDivisions** (self)

- **CheckTotals** (self)

- **DoBarlineChecks** (self)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **NewBeam** (self, type)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **SetItem** (self, new_item)

- **SortedChildren** (self)

- **toLily** (self)

    Method which converts the object instance, its attributes and children to a string of lilypond code

    
* :return: str of lilypond code

##### Instance variables
- **autoBeam**
