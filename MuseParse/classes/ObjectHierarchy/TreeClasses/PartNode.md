Module classes.ObjectHierarchy.TreeClasses.PartNode
---------------------------------------------------

Classes
-------
#### PartNode 
Class representing the node holding the part.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.PartNode.PartNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.IndexedNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self, index=0)

- **AddBarline** (self, staff=1, measure=1, location='left', item=None)

- **AddChild** (self, item, index=-1)

- **AddRule** (self, rule)

- **Backup** (self, measure_id, duration=0)

- **CalculateVariable** (self, name, staves)

- **CheckDivisions** (self)

- **CheckIfTabStaff** (self)

- **CheckMeasureDivisions** (self, measure)

- **CheckMeasureMeter** (self, measure)

- **CheckPreviousBarline** (self, staff)

    method which checks the bar before the current for changes we need to make to it's barlines

- **CheckTotals** (self)

    method to calculate the maximum total lilypond value for a measure without a time signature

- **DoBarlineChecks** (self)

- **Forward** (self, measure_id, duration=0)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **GetMeasureAtPosition** (self, index, staff=1)

- **GetMeasureIDAtPosition** (self, index, staff=1)

- **NewBeam** (self, type, staff)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **SetItem** (self, new_item)

- **addClef** (self, item, measure_id, staff_id, voice)

- **addEmptyMeasure** (self, measure=1, staff=1)

- **addKey** (self, item, measure_id)

- **addMeasure** (self, item, measure=1, staff=1)

- **getMeasure** (self, measure=1, staff=1)

- **getStaff** (self, key)

- **setDivisions** (self, measure=1, divisions=1)

- **toLily** (self)

    Method which converts the object instance, its attributes and children to a string of lilypond code

    
* :return: str of lilypond code

##### Instance variables
- **index**
