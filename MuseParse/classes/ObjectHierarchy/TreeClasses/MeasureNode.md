Module classes.ObjectHierarchy.TreeClasses.MeasureNode
------------------------------------------------------

Classes
-------
#### MeasureNode 
Class representing the tree node for a measure.

# Optional inputs:  

* - partial: bool. Represents whether the bar is partial i.e a pickup or something

# Optional attributes:  

* - newSystem: boolean indicating to create a new system for this bar

* - newPage: boolean indicating to create a new page for this bar

* - key: Key class entry representing key sig

* - meter: meter class entry representing meter/time sig

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.MeasureNode.MeasureNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.IndexedNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **AddBarline** (self, item, location)

- **AddChild** (self, item, index=-1)

- **AddRule** (self, rule)

- **Backup** (self, duration=0)

    method to use when a backup tag is encountered in musicXML. Moves back in the bar by <duration>
:param duration:  
:return:

- **CalculateTransposition** (self)

- **CheckDivisions** (self)

- **CopyDirectionsAndExpressions** (self, v_obj)

- **Forward** (self, duration=0)

    method to use when forward tag is encountered in musicXML. jumps forward in the bar by <duration>

    * :param duration: number of beats to move forward
:return:

- **GetBarline** (self, location)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **GetLastClef** (self, voice=1)

- **GetLastKey** (self, voice=1)

    key as in musical key, not index

- **GetTotalValue** (self)

    Gets the total value of the bar according to it's time signature

- **HandleAttributes** (self)

- **HandleClosingAttributes** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **PositionChild** (self, item, key, voice=1)

- **ReplaceChild** (self, key, item)

- **RunVoiceChecks** (self)

- **SetItem** (self, new_item)

- **addClef** (self, item, voice=1)

    method to use when adding a clef. will either add it to the node itself or add it onto the first voice's children
list
:param item:  
:param voice:  
:return:

- **addDirection** (self, item, voice=1)

- **addExpression** (self, item, voice=1)

- **addKey** (self, item, voice=1)

- **addNote** (self, item, voice=1, increment=1, chord=False)

- **addPlaceholder** (self, duration=0, voice=1)

- **addVoice** (self, item=None, id=1)

- **addWrapper** (self, item)

- **getPartialLength** (self)

    method to calculate how much to give the "partial" indicator where a measure is a pickup

    * :return: str which is the lilypond bar length

- **getVoice** (self, key)

- **getWrapper** (self, index)

- **toLily** (self)

    Method which converts the object instance, its attributes and children to a string of lilypond code

    
* :return: str of lilypond code

##### Instance variables
- **autoBeam**

- **barlines**

- **gap**

- **index**

- **items**
